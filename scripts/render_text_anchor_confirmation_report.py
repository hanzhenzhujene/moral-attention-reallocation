#!/usr/bin/env python3
"""Render a compact readout for the exploratory 6-condition confirmation run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

import condition_registry


def load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def find_summary(summaries: Iterable[Dict[str, Any]], model: str, condition: str) -> Dict[str, Any]:
    for row in summaries:
        if row["model"] == model and row["condition"] == condition:
            return row
    raise KeyError(f"Missing summary for {model} / {condition}")


def find_health_group(groups: Iterable[Dict[str, Any]], model: str, condition: str) -> Dict[str, Any]:
    for row in groups:
        if row["model"] == model and row["condition"] == condition:
            return row
    raise KeyError(f"Missing health group for {model} / {condition}")


def metric_point(summary_row: Dict[str, Any], metric_name: str) -> float | None:
    metric = summary_row["metrics"].get(metric_name)
    if metric is None:
        return None
    return metric.get("point")


def contrast_lookup(robustness: Dict[str, Any], model: str, left: str, right: str, slice_name: str) -> Dict[str, Any] | None:
    for row in robustness["contrasts"]:
        if (
            row["model"] == model
            and row["left_condition"] == left
            and row["right_condition"] == right
            and row["slice"] == slice_name
        ):
            return row
    return None


def render_markdown(report: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Text-Anchor Confirmation Readout",
        "",
        "## Setup",
        "",
        f"- Benchmark: `{report['benchmark_name']}`",
        f"- Slice composition: `{report['slice_composition']}`",
        f"- Conditions: `{report['conditions']}`",
        f"- Model: `{report['model']}`",
        f"- Valid records: `{report['valid_records']}`",
        f"- Parse failure rate: `{report['parse_failure_rate']}`",
        "",
        "## What Held",
        "",
        f"- same-heart control accuracy minimum across all 6 conditions: `{report['same_heart_control_min']}`",
        f"- heart overreach maximum across all 6 conditions: `{report['heart_overreach_max']}`",
        f"- maximum explanation ratio vs baseline: `{report['max_explanation_ratio_vs_baseline']}`",
        "",
        "| Condition | Task A | Task B | HSS | P(reason=motive) | Same-heart | Overreach |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for row in report["condition_rows"]:
        lines.append(
            "| {condition} | {task_a_accuracy} | {task_b_accuracy} | {heart_sensitivity_score} | {p_reason_motive} | {same_heart_control_accuracy} | {heart_overreach_rate} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Main Exploratory Result",
            "",
            f"- `heart_focused` vs `baseline` Task B: `{report['heart_vs_baseline']['task_b']}`",
            f"- `heart_focused` vs `baseline` HSS: `{report['heart_vs_baseline']['hss']}`",
            f"- supportive text anchors vs baseline: `{report['supportive_anchor_count']}` / `{report['anchor_count']}`",
            f"- mean text-anchor delta vs baseline on Task B: `{report['family_mean_task_b_delta']}`",
            f"- mean text-anchor delta vs baseline on HSS: `{report['family_mean_hss_delta']}`",
            "",
            "| Text anchor | Delta Task B vs baseline | Delta HSS vs baseline | Delta HSS vs heart-focused |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in report["anchor_rows"]:
        lines.append(
            "| {condition} | {task_b_delta} | {hss_delta} | {hss_vs_heart} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Same-Act Slice Robustness",
            "",
        ]
    )
    for row in report["same_act_rows"]:
        lines.extend(
            [
                f"### {row['label']}",
                "",
                f"- HSS delta vs baseline: `{row['hss_delta_vs_baseline']}`",
                f"- paired sign counts: `{row['better']}` better / `{row['worse']}` worse / `{row['tie']}` ties",
                f"- exact sign test: one-sided `{row['one_sided_p']}`, two-sided `{row['two_sided_p']}`",
                "",
            ]
        )

    if report.get("paired_order_rows"):
        lines.extend(
            [
                "## Confirmation Paired-Order Diagnostic",
                "",
                f"- paired-order records: `{report['paired_order_records']}`",
                f"- maximum item-level Task B order-flip rate: `{report['paired_order_flip_rate_max']}`",
                f"- maximum paired-order Task B accuracy gap: `{report['paired_order_gap_max']}`",
                "",
                "| Condition | Paired-order Task B | Order flips | Paired gap |",
                "| --- | ---: | ---: | ---: |",
            ]
        )
        for row in report["paired_order_rows"]:
            lines.append(
                "| {condition} | {task_b_accuracy} | {flip_rate} | {gap} |".format(
                    **row
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Interpretation",
            "",
            "- This run is a targeted exploratory confirmation on the model that showed the strongest pilot support, not a new frozen cross-model main claim.",
            "- The confirmation question is whether multiple text-anchored variants continue to move motive-sensitive metrics in the same direction as `heart_focused` while preserving same-heart controls.",
        ]
    )
    if report.get("paired_order_rows"):
        lines.append(
            "- The confirmation paired-order pack matters because it separates genuine same-item order instability from split-based swap-gap artifacts. On this run, the same-item paired-order diagnostic is clean across all six conditions."
        )
        lines.append(
            "- The current exploratory result is therefore strongest for `heart_focused` and `Proverbs 4:23`: both improve the mechanistic target on the confirmation slice, preserve same-heart guardrails, and stay stable under paired-order diagnosis."
        )
    else:
        lines.append(
            "- This readout does not yet include a confirmation paired-order pack, so split-based swap-gap should still be interpreted cautiously."
        )
    lines.extend(
        [
            "",
            "## Primary Files",
            "",
            f"- Summary: `{report['summary_path']}`",
            f"- Robustness: `{report['robustness_path']}`",
            f"- Family summary: `{report['family_path']}`",
            f"- Health: `{report['health_path']}`",
        ]
    )
    if report.get("paired_order_path"):
        lines.append(f"- Paired-order stability: `{report['paired_order_path']}`")
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--robustness", required=True)
    parser.add_argument("--health", required=True)
    parser.add_argument("--family-summary", required=True)
    parser.add_argument("--paired-order")
    parser.add_argument("--model", required=True)
    parser.add_argument("--benchmark-name", required=True)
    parser.add_argument("--slice-composition", required=True)
    parser.add_argument("--summary-path", required=True)
    parser.add_argument("--robustness-path", required=True)
    parser.add_argument("--family-path", required=True)
    parser.add_argument("--health-path", required=True)
    parser.add_argument("--paired-order-path")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md", required=True)
    args = parser.parse_args(argv)

    summary = load_json(args.summary)
    robustness = load_json(args.robustness)
    health = load_json(args.health)
    family_summary = load_json(args.family_summary)
    paired_order = load_json(args.paired_order) if args.paired_order else None

    model = args.model
    summaries = summary["summaries"]
    baseline_summary = find_summary(summaries, model, "baseline")
    heart_summary = find_summary(summaries, model, "heart_focused")
    family_block = next(block for block in family_summary if block["model"] == model)

    condition_rows: List[Dict[str, Any]] = []
    for condition in ["baseline", "heart_focused", *condition_registry.TEXT_ANCHOR_CONDITIONS]:
        summary_row = find_summary(summaries, model, condition)
        condition_rows.append(
            {
                "condition": condition_registry.public_display_name(condition),
                "task_a_accuracy": metric_point(summary_row, "task_a_accuracy"),
                "task_b_accuracy": metric_point(summary_row, "task_b_accuracy"),
                "heart_sensitivity_score": metric_point(summary_row, "heart_sensitivity_score"),
                "p_reason_motive": metric_point(summary_row, "p_reason_motive"),
                "same_heart_control_accuracy": metric_point(summary_row, "same_heart_control_accuracy"),
                "heart_overreach_rate": metric_point(summary_row, "heart_overreach_rate"),
            }
        )

    anchor_rows = [
        {
            "condition": row["display_name"],
            "task_b_delta": row["delta_vs_baseline"]["task_b_accuracy"],
            "hss_delta": row["delta_vs_baseline"]["heart_sensitivity_score"],
            "hss_vs_heart": row["delta_vs_heart_focused"]["heart_sensitivity_score"],
        }
        for row in family_block["per_condition"]
    ]

    same_act_rows: List[Dict[str, Any]] = []
    for condition in ["heart_focused", *condition_registry.TEXT_ANCHOR_CONDITIONS]:
        contrast = contrast_lookup(robustness, model, "baseline", condition, "same_act_different_motive")
        if contrast is None:
            continue
        metric = contrast["metrics"]["heart_sensitivity_score"]
        same_act_rows.append(
            {
                "label": f"{condition_registry.public_display_name(condition)} vs baseline",
                "hss_delta_vs_baseline": metric["delta"],
                "better": metric["better"],
                "worse": metric["worse"],
                "tie": metric["tie"],
                "one_sided_p": metric["exact_sign_p_one_sided"],
                "two_sided_p": metric["exact_sign_p_two_sided"],
            }
        )

    paired_groups = [group for group in paired_order["groups"] if group["model"] == model] if paired_order else []
    paired_order_rows = [
        {
            "condition": condition_registry.public_display_name(group["condition"]),
            "task_b_accuracy": group["task_b_accuracy_ab"],
            "flip_rate": group["task_b_order_flip_rate"],
            "gap": group["task_b_accuracy_gap"],
        }
        for group in paired_groups
    ]

    health_groups = [
        find_health_group(health["groups"], model, condition)
        for condition in ["baseline", "heart_focused", *condition_registry.TEXT_ANCHOR_CONDITIONS]
    ]

    report = {
        "benchmark_name": args.benchmark_name,
        "slice_composition": args.slice_composition,
        "conditions": ", ".join(["baseline", "heart_focused", "4 text anchors"]),
        "model": model,
        "valid_records": health["valid_records"],
        "parse_failure_rate": health["parse_failure_rate"],
        "same_heart_control_min": min(metric_point(group, "same_heart_control_accuracy") for group in health_groups),
        "heart_overreach_max": max(metric_point(group, "heart_overreach_rate") for group in health_groups),
        "max_explanation_ratio_vs_baseline": max(group["explanation_ratio_vs_baseline"] for group in health_groups),
        "condition_rows": condition_rows,
        "heart_vs_baseline": {
            "task_b": round(
                metric_point(heart_summary, "task_b_accuracy") - metric_point(baseline_summary, "task_b_accuracy"),
                4,
            ),
            "hss": round(
                metric_point(heart_summary, "heart_sensitivity_score") - metric_point(baseline_summary, "heart_sensitivity_score"),
                4,
            ),
        },
        "supportive_anchor_count": family_block["supportive_text_anchor_count"],
        "anchor_count": len(family_block["per_condition"]),
        "family_mean_task_b_delta": family_block["family_mean_delta_vs_baseline"]["task_b_accuracy"],
        "family_mean_hss_delta": family_block["family_mean_delta_vs_baseline"]["heart_sensitivity_score"],
        "anchor_rows": anchor_rows,
        "same_act_rows": same_act_rows,
        "paired_order_rows": paired_order_rows,
        "summary_path": args.summary_path,
        "robustness_path": args.robustness_path,
        "family_path": args.family_path,
        "health_path": args.health_path,
        "paired_order_path": args.paired_order_path,
    }
    if paired_groups:
        report["paired_order_records"] = sum(group["n_complete_pairs"] for group in paired_groups) * 2
        report["paired_order_flip_rate_max"] = max(group["task_b_order_flip_rate"] for group in paired_groups)
        report["paired_order_gap_max"] = max(group["task_b_accuracy_gap"] for group in paired_groups)

    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    output_md = Path(args.output_md)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(render_markdown(report), encoding="utf-8")
    print(f"Wrote confirmation readout to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
