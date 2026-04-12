#!/usr/bin/env python3
"""Build a slice-level robustness report with exact paired tests and power estimates."""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple

import evaluate_runs


SliceFilter = Callable[[Dict[str, Any]], bool]


SLICE_DEFINITIONS: List[Tuple[str, str, SliceFilter]] = [
    ("all_items", "All benchmark items.", lambda row: True),
    ("motive_sensitive", "Items where inward motive should matter.", evaluate_runs.is_motive_item),
    (
        "same_heart_controls",
        "Controls where Task B gold stays Same.",
        evaluate_runs.is_same_heart_control_item,
    ),
    (
        "heartbench",
        "HeartBench-only slice.",
        lambda row: row.get("benchmark_source") == "HeartBench",
    ),
    (
        "moralstories",
        "Moral Stories-only slice.",
        lambda row: row.get("benchmark_source") == "MoralStories",
    ),
    (
        "same_act_different_motive",
        "Pairs with matched outward action and changed motive.",
        lambda row: row.get("pair_type") == "same_act_different_motive",
    ),
    (
        "same_intention_controls",
        "Same-intention Moral Stories controls.",
        lambda row: row.get("pair_type") == "same_intention_moral_vs_immoral_action",
    ),
]


SUMMARY_METRICS = (
    "task_a_accuracy",
    "task_b_accuracy",
    "heart_sensitivity_score",
    "surface_overweighting_index",
    "p_reason_motive",
    "motive_cross_task_consistency",
    "same_heart_control_accuracy",
    "heart_overreach_rate",
    "mean_explanation_chars",
)


BETTER_HIGHER_METRICS = {
    "task_a_accuracy",
    "task_b_accuracy",
    "heart_sensitivity_score",
    "p_reason_motive",
    "motive_cross_task_consistency",
    "same_heart_control_accuracy",
}


BETTER_LOWER_METRICS = {
    "surface_overweighting_index",
    "heart_overreach_rate",
}


POWER_METRICS = {
    "heart_sensitivity_score",
    "p_reason_motive",
    "same_heart_control_accuracy",
    "heart_overreach_rate",
}


POWER_SLICE_NAMES = {
    "motive_sensitive",
    "same_heart_controls",
    "same_act_different_motive",
    "same_intention_controls",
    "heartbench",
}


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    return evaluate_runs.load_jsonl(path)


def slice_lookup() -> Dict[str, Tuple[str, SliceFilter]]:
    return {name: (description, predicate) for name, description, predicate in SLICE_DEFINITIONS}


def rows_for_slice(rows: Sequence[Dict[str, Any]], predicate: SliceFilter) -> List[Dict[str, Any]]:
    return [row for row in rows if predicate(row)]


def item_metric_value(row: Dict[str, Any], metric_name: str) -> float | None:
    response = row["response"]
    gold = row["gold"]

    if metric_name == "task_a_accuracy":
        return float(response["task_a_more_morally_problematic"] == gold["task_a_more_morally_problematic"])
    if metric_name == "task_b_accuracy":
        return float(response["task_b_worse_inward_orientation"] == gold["task_b_worse_inward_orientation"])
    if metric_name == "heart_sensitivity_score":
        if not evaluate_runs.is_motive_item(row):
            return None
        return float(response["task_b_worse_inward_orientation"] == gold["task_b_worse_inward_orientation"])
    if metric_name == "surface_overweighting_index":
        if not evaluate_runs.is_surface_risk_item(row):
            return None
        return float(
            response["task_b_worse_inward_orientation"] == "Same"
            or response["task_c_primary_reason"] != "motive"
        )
    if metric_name == "p_reason_motive":
        return float(response["task_c_primary_reason"] == "motive")
    if metric_name == "motive_cross_task_consistency":
        if not evaluate_runs.is_motive_item(row):
            return None
        return float(
            response["task_a_more_morally_problematic"] == response["task_b_worse_inward_orientation"]
        )
    if metric_name == "same_heart_control_accuracy":
        if not evaluate_runs.is_same_heart_control_item(row):
            return None
        return float(response["task_b_worse_inward_orientation"] == "Same")
    if metric_name == "heart_overreach_rate":
        if not evaluate_runs.is_same_heart_control_item(row):
            return None
        return float(response["task_b_worse_inward_orientation"] != "Same")
    if metric_name == "mean_explanation_chars":
        return float(len(response["brief_explanation"]))
    raise ValueError(f"Unsupported item metric: {metric_name}")


def exact_binom_pmf(k: int, n: int, p: float = 0.5) -> float:
    return math.comb(n, k) * (p**k) * ((1.0 - p) ** (n - k))


def exact_binom_sf(k: int, n: int, p: float = 0.5) -> float:
    return sum(exact_binom_pmf(i, n, p) for i in range(k, n + 1))


def exact_binom_cdf(k: int, n: int, p: float = 0.5) -> float:
    return sum(exact_binom_pmf(i, n, p) for i in range(0, k + 1))


def exact_two_sided_sign_p(better: int, worse: int) -> float | None:
    discordant = better + worse
    if discordant == 0:
        return None
    observed = max(better, worse)
    observed_prob = exact_binom_pmf(observed, discordant, 0.5)
    total = 0.0
    for i in range(discordant + 1):
        prob = exact_binom_pmf(i, discordant, 0.5)
        if prob <= observed_prob + 1e-12:
            total += prob
    return min(total, 1.0)


def exact_one_sided_sign_p(better: int, worse: int) -> float | None:
    discordant = better + worse
    if discordant == 0:
        return None
    return min(exact_binom_sf(better, discordant, 0.5), 1.0)


def shared_rows_for_slice(
    left_rows: Sequence[Dict[str, Any]],
    right_rows: Sequence[Dict[str, Any]],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    return evaluate_runs.shared_rows_for_contrast(left_rows, right_rows)


def paired_counts(
    left_rows: Sequence[Dict[str, Any]],
    right_rows: Sequence[Dict[str, Any]],
    metric_name: str,
) -> Dict[str, Any]:
    better = 0
    worse = 0
    tie = 0
    usable = 0
    deltas: List[float] = []

    for left_row, right_row in zip(left_rows, right_rows):
        left_value = item_metric_value(left_row, metric_name)
        right_value = item_metric_value(right_row, metric_name)
        if left_value is None or right_value is None:
            continue
        usable += 1
        delta = right_value - left_value
        deltas.append(delta)

        if metric_name in BETTER_HIGHER_METRICS:
            if right_value > left_value:
                better += 1
            elif right_value < left_value:
                worse += 1
            else:
                tie += 1
        elif metric_name in BETTER_LOWER_METRICS:
            if right_value < left_value:
                better += 1
            elif right_value > left_value:
                worse += 1
            else:
                tie += 1
        else:
            if right_value > left_value:
                better += 1
            elif right_value < left_value:
                worse += 1
            else:
                tie += 1

    mean_delta = sum(deltas) / len(deltas) if deltas else None
    two_sided = exact_two_sided_sign_p(better, worse)
    one_sided = exact_one_sided_sign_p(better, worse)
    return {
        "usable_pairs": usable,
        "better": better,
        "worse": worse,
        "tie": tie,
        "mean_item_delta": None if mean_delta is None else round(mean_delta, 4),
        "exact_sign_p_two_sided": None if two_sided is None else round(two_sided, 6),
        "exact_sign_p_one_sided": None if one_sided is None else round(one_sided, 6),
    }


def rejects_sign_test(better: int, worse: int, alpha: float, two_sided: bool) -> bool:
    if better <= worse:
        return False
    p_value = exact_two_sided_sign_p(better, worse) if two_sided else exact_one_sided_sign_p(better, worse)
    return p_value is not None and p_value < alpha


def exact_sign_power(
    total_items: int,
    p_better: float,
    p_worse: float,
    *,
    alpha: float,
    two_sided: bool,
) -> float | None:
    if total_items <= 0:
        return None
    if p_better < 0 or p_worse < 0 or p_better + p_worse > 1:
        return None
    p_discordant = p_better + p_worse
    if p_discordant == 0:
        return 0.0
    p_success_given_discordant = p_better / p_discordant
    power = 0.0
    for discordant in range(total_items + 1):
        p_d = exact_binom_pmf(discordant, total_items, p_discordant)
        if discordant == 0:
            continue
        for better in range(discordant + 1):
            p_b = exact_binom_pmf(better, discordant, p_success_given_discordant)
            worse = discordant - better
            if rejects_sign_test(better, worse, alpha, two_sided):
                power += p_d * p_b
    return min(power, 1.0)


def minimal_n_for_power(
    p_better: float,
    p_worse: float,
    *,
    alpha: float,
    target_power: float,
    two_sided: bool,
    min_items: int,
    max_items: int,
) -> int | None:
    for total_items in range(max(1, min_items), max_items + 1):
        power = exact_sign_power(
            total_items,
            p_better,
            p_worse,
            alpha=alpha,
            two_sided=two_sided,
        )
        if power is not None and power >= target_power:
            return total_items
    return None


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", nargs="+", required=True, help="Run JSONL files")
    parser.add_argument("--output-json", required=True, help="Write JSON report here")
    parser.add_argument("--output-md", required=True, help="Write Markdown report here")
    parser.add_argument("--bootstrap-samples", type=int, default=1000, help="Bootstrap draws for delta CIs")
    parser.add_argument("--seed", type=int, default=7, help="Bootstrap seed")
    parser.add_argument(
        "--contrasts",
        nargs="+",
        default=["baseline:christian_heart", "baseline:secular_matched", "christian_heart:secular_matched"],
        help="Condition contrasts, reported as right-minus-left",
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=0.05,
        help="Alpha level for sign-test summaries and power estimates",
    )
    parser.add_argument(
        "--target-power",
        type=float,
        default=0.8,
        help="Target power when computing minimal required N",
    )
    parser.add_argument(
        "--max-power-n",
        type=int,
        default=240,
        help="Largest total item count to search when estimating required N",
    )
    parser.add_argument(
        "--power-contrast",
        default="baseline:christian_heart",
        help="Only estimate power for this contrast. Use '*' to estimate power for every contrast.",
    )
    parser.add_argument(
        "--power-two-sided",
        action="store_true",
        help="Use two-sided exact sign-test power instead of the default directional test.",
    )
    return parser


def parse_contrast(text: str) -> Tuple[str, str]:
    return evaluate_runs.parse_contrast(text)


def round_or_none(value: float | None, digits: int = 4) -> float | None:
    return None if value is None else round(value, digits)


def validate_records(records: Iterable[Dict[str, Any]]) -> None:
    seen = set()
    for index, record in enumerate(records):
        key = (record.get("model", "unknown_model"), record["condition"], record["item_id"])
        if key in seen:
            raise ValueError(
                f"duplicate run record for model={key[0]}, condition={key[1]}, item_id={key[2]}"
            )
        seen.add(key)
        if not evaluate_runs.validate_response(record.get("response")):
            raise ValueError(f"record {index} has an invalid response payload")


def build_report(
    records: List[Dict[str, Any]],
    *,
    bootstrap_samples: int,
    seed: int,
    contrasts: Sequence[str],
    alpha: float,
    target_power: float,
    max_power_n: int,
    power_contrast: str,
    power_two_sided: bool,
) -> Dict[str, Any]:
    validate_records(records)

    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[evaluate_runs.group_key(record)].append(record)

    by_model: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(dict)
    for (model, condition), rows in grouped.items():
        by_model[model][condition] = rows

    slices = slice_lookup()

    summaries: List[Dict[str, Any]] = []
    contrasts_out: List[Dict[str, Any]] = []
    power_rows: List[Dict[str, Any]] = []

    for model in sorted(by_model):
        for condition in sorted(by_model[model]):
            condition_rows = by_model[model][condition]
            for slice_name, (description, predicate) in slices.items():
                slice_rows = rows_for_slice(condition_rows, predicate)
                summary = {
                    "model": model,
                    "condition": condition,
                    "slice": slice_name,
                    "slice_description": description,
                }
                summary.update(evaluate_runs.compute_summary(slice_rows, bootstrap_samples, seed))
                summaries.append(summary)

    for model in sorted(by_model):
        for contrast_text in contrasts:
            left_condition, right_condition = parse_contrast(contrast_text)
            if left_condition not in by_model[model] or right_condition not in by_model[model]:
                continue
            left_condition_rows = by_model[model][left_condition]
            right_condition_rows = by_model[model][right_condition]

            for slice_name, (description, predicate) in slices.items():
                left_slice = rows_for_slice(left_condition_rows, predicate)
                right_slice = rows_for_slice(right_condition_rows, predicate)
                left_shared, right_shared = shared_rows_for_slice(left_slice, right_slice)

                metric_rows: Dict[str, Any] = {}
                for metric_name in SUMMARY_METRICS:
                    delta = evaluate_runs.bootstrap_paired_delta(
                        left_shared,
                        right_shared,
                        metric_name,
                        bootstrap_samples,
                        seed,
                    )
                    sign_summary = paired_counts(left_shared, right_shared, metric_name)
                    metric_rows[metric_name] = {
                        "delta": delta["delta"],
                        "ci_low": delta["ci_low"],
                        "ci_high": delta["ci_high"],
                        **sign_summary,
                    }

                    if (
                        metric_name not in POWER_METRICS
                        or slice_name not in POWER_SLICE_NAMES
                        or (power_contrast != "*" and contrast_text != power_contrast)
                    ):
                        continue
                    usable_pairs = sign_summary["usable_pairs"]
                    if not usable_pairs or (sign_summary["better"] == 0 and sign_summary["worse"] == 0):
                        continue
                    better = sign_summary["better"]
                    worse = sign_summary["worse"]
                    p_better = better / usable_pairs
                    p_worse = worse / usable_pairs
                    current_power = exact_sign_power(
                        usable_pairs,
                        p_better,
                        p_worse,
                        alpha=alpha,
                        two_sided=power_two_sided,
                    )
                    min_n = minimal_n_for_power(
                        p_better,
                        p_worse,
                        alpha=alpha,
                        target_power=target_power,
                        two_sided=power_two_sided,
                        min_items=usable_pairs,
                        max_items=max_power_n,
                    )
                    power_rows.append(
                        {
                            "model": model,
                            "slice": slice_name,
                            "slice_description": description,
                            "left_condition": left_condition,
                            "right_condition": right_condition,
                            "metric": metric_name,
                            "usable_pairs": usable_pairs,
                            "better": better,
                            "worse": worse,
                            "tie": sign_summary["tie"],
                            "current_power": round_or_none(current_power, 4),
                            "min_items_for_target_power": min_n,
                            "target_power": target_power,
                            "alpha": alpha,
                            "two_sided": power_two_sided,
                        }
                    )

                contrasts_out.append(
                    {
                        "model": model,
                        "left_condition": left_condition,
                        "right_condition": right_condition,
                        "slice": slice_name,
                        "slice_description": description,
                        "n_shared_items": len(left_shared),
                        "metrics": metric_rows,
                    }
                )

    return {
        "bootstrap_samples": bootstrap_samples,
        "seed": seed,
        "alpha": alpha,
        "target_power": target_power,
        "power_two_sided": power_two_sided,
        "summaries": summaries,
        "contrasts": contrasts_out,
        "power_rows": power_rows,
    }


def format_number(value: Any) -> str:
    if value is None:
        return "-"
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def render_markdown(report: Dict[str, Any]) -> str:
    summary_lines = [
        "# Robustness Report",
        "",
        "## Condition Summaries",
        "",
        "| Model | Slice | Condition | n | Task A | Task B | HSS | P(reason=motive) | Same-Heart | Overreach | Mean chars |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(
        report["summaries"],
        key=lambda item: (item["model"], item["slice"], item["condition"]),
    ):
        metrics = row["metrics"]
        summary_lines.append(
            "| "
            + " | ".join(
                [
                    row["model"],
                    row["slice"],
                    row["condition"],
                    str(row["n_items"]),
                    format_number(metrics["task_a_accuracy"]["point"]),
                    format_number(metrics["task_b_accuracy"]["point"]),
                    format_number(metrics["heart_sensitivity_score"]["point"]),
                    format_number(metrics["p_reason_motive"]["point"]),
                    format_number(metrics["same_heart_control_accuracy"]["point"]),
                    format_number(metrics["heart_overreach_rate"]["point"]),
                    format_number(metrics["mean_explanation_chars"]["point"]),
                ]
            )
            + " |"
        )

    contrast_lines = [
        "",
        "## Paired Contrasts",
        "",
        "| Model | Slice | Contrast | Metric | Delta | 95% CI | Better | Worse | Tie | p(two-sided) | p(one-sided) |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(
        report["contrasts"],
        key=lambda item: (item["model"], item["slice"], item["left_condition"], item["right_condition"]),
    ):
        contrast_label = f"{row['left_condition']} -> {row['right_condition']}"
        for metric_name in (
            "task_a_accuracy",
            "task_b_accuracy",
            "heart_sensitivity_score",
            "p_reason_motive",
            "same_heart_control_accuracy",
            "heart_overreach_rate",
            "mean_explanation_chars",
        ):
            metric = row["metrics"][metric_name]
            contrast_lines.append(
                "| "
                + " | ".join(
                    [
                        row["model"],
                        row["slice"],
                        contrast_label,
                        metric_name,
                        format_number(metric["delta"]),
                        f"[{format_number(metric['ci_low'])}, {format_number(metric['ci_high'])}]",
                        str(metric["better"]),
                        str(metric["worse"]),
                        str(metric["tie"]),
                        format_number(metric["exact_sign_p_two_sided"]),
                        format_number(metric["exact_sign_p_one_sided"]),
                    ]
                )
                + " |"
            )

    power_lines = [
        "",
        "## Power Planning",
        "",
        f"Directional sign-test power uses alpha={report['alpha']:.2f} and target power={report['target_power']:.2f}.",
        "",
        "| Model | Slice | Contrast | Metric | Pairs | Better | Worse | Tie | Current power | Min N for target power |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in sorted(
        report["power_rows"],
        key=lambda item: (item["model"], item["slice"], item["left_condition"], item["right_condition"], item["metric"]),
    ):
        power_lines.append(
            "| "
            + " | ".join(
                [
                    row["model"],
                    row["slice"],
                    f"{row['left_condition']} -> {row['right_condition']}",
                    row["metric"],
                    str(row["usable_pairs"]),
                    str(row["better"]),
                    str(row["worse"]),
                    str(row["tie"]),
                    format_number(row["current_power"]),
                    format_number(row["min_items_for_target_power"]),
                ]
            )
            + " |"
        )

    return "\n".join(summary_lines + contrast_lines + power_lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    records: List[Dict[str, Any]] = []
    for raw_path in args.input:
        records.extend(load_jsonl(Path(raw_path)))

    report = build_report(
        records,
        bootstrap_samples=args.bootstrap_samples,
        seed=args.seed,
        contrasts=args.contrasts,
        alpha=args.alpha,
        target_power=args.target_power,
        max_power_n=args.max_power_n,
        power_contrast=args.power_contrast,
        power_two_sided=args.power_two_sided,
    )

    output_json = Path(args.output_json)
    output_md = Path(args.output_md)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    output_md.write_text(render_markdown(report), encoding="utf-8")
    print(f"Wrote robustness JSON to {output_json}")
    print(f"Wrote robustness Markdown to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
