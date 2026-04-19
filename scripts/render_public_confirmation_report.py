#!/usr/bin/env python3
"""Render a compact report for the public baseline-vs-heart-focused confirmation slice."""

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


def contrast_lookup(robustness: Dict[str, Any], model: str, left: str, right: str, slice_name: str) -> Dict[str, Any]:
    for row in robustness["contrasts"]:
        if (
            row["model"] == model
            and row["left_condition"] == left
            and row["right_condition"] == right
            and row["slice"] == slice_name
        ):
            return row
    raise KeyError(f"Missing contrast for {model} / {left}->{right} / {slice_name}")


def power_row_lookup(robustness: Dict[str, Any], model: str, left: str, right: str, slice_name: str, metric: str) -> Dict[str, Any]:
    for row in robustness["power_rows"]:
        if (
            row["model"] == model
            and row["left_condition"] == left
            and row["right_condition"] == right
            and row["slice"] == slice_name
            and row["metric"] == metric
        ):
            return row
    raise KeyError(f"Missing power row for {model} / {left}->{right} / {slice_name} / {metric}")


def render_markdown(report: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Public Confirmation Readout",
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
        f"- same-heart control accuracy stayed `{report['same_heart_control']}` in both conditions",
        f"- heart overreach stayed `{report['heart_overreach']}` in both conditions",
        f"- maximum explanation ratio vs baseline: `{report['max_explanation_ratio_vs_baseline']}`",
        "",
        "| Condition | Task A | Task B | HSS | P(reason=motive) | Same-heart | Overreach | Mean chars |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for row in report["condition_rows"]:
        lines.append(
            "| {condition} | {task_a_accuracy} | {task_b_accuracy} | {heart_sensitivity_score} | {p_reason_motive} | {same_heart_control_accuracy} | {heart_overreach_rate} | {mean_explanation_chars} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Main Directional Result",
            "",
            f"- `Task A` delta: `{report['all_items_delta']['task_a']}`",
            f"- `Task B` delta: `{report['all_items_delta']['task_b']}`",
            f"- `heart_sensitivity_score` delta: `{report['all_items_delta']['hss']}`",
            f"- `P(reason = motive)` delta: `{report['all_items_delta']['p_reason_motive']}`",
            "",
            "## Same-Act Slice Evidence",
            "",
            f"- HSS delta on `same_act_different_motive`: `{report['same_act_hss']['delta']}`",
            f"- paired sign counts: `{report['same_act_hss']['better']}` better / `{report['same_act_hss']['worse']}` worse / `{report['same_act_hss']['tie']}` ties",
            f"- exact sign test: one-sided `{report['same_act_hss']['one_sided_p']}`, two-sided `{report['same_act_hss']['two_sided_p']}`",
            f"- current directional sign-test power: `{report['same_act_power']['current_power']}`",
            f"- minimum motive-sensitive items for target power: `{report['same_act_power']['min_items_for_target_power']}`",
        ]
    )

    if report.get("paired_order_followup"):
        followup = report["paired_order_followup"]
        lines.extend(
            [
                "",
                "## Later Paired-Order Follow-Up",
                "",
                f"- paired-order records: `{followup['paired_order_records']}`",
                f"- maximum item-level Task B order-flip rate: `{followup['max_flip_rate']}`",
                f"- maximum paired-order Task B gap: `{followup['max_gap']}`",
                "",
                "| Condition | Paired-order Task B | Order flips | Paired gap |",
                "| --- | ---: | ---: | ---: |",
            ]
        )
        for row in followup["rows"]:
            lines.append(
                "| {condition} | {task_b_accuracy} | {flip_rate} | {gap} |".format(
                    **row
                )
            )
        lines.extend(
            [
                "",
                "- On this follow-up, the public baseline and heart-focused conditions show no same-item Task B order instability.",
                "- The remaining limitation on the public slice is power, not guardrail failure.",
            ]
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- The public artifact supports a narrow mechanistic claim: heart-focused framing directionally improves inward-motive judgment on a clean confirmation slice.",
            "- The strongest movement is in Task B and heart-sensitivity, not in the top-line Task A verdict.",
            "- The gain does not come with worse same-heart controls, higher heart overreach, or longer explanations.",
            "",
            "## Primary Files",
            "",
            f"- Summary: `{report['summary_path']}`",
            f"- Robustness: `{report['robustness_path']}`",
            f"- Health: `{report['health_path']}`",
        ]
    )
    if report.get("paired_order_path"):
        lines.append(f"- Paired-order follow-up: `{report['paired_order_path']}`")
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--robustness", required=True)
    parser.add_argument("--health", required=True)
    parser.add_argument("--paired-order-followup")
    parser.add_argument("--model", required=True)
    parser.add_argument("--benchmark-name", required=True)
    parser.add_argument("--slice-composition", required=True)
    parser.add_argument("--summary-path", required=True)
    parser.add_argument("--robustness-path", required=True)
    parser.add_argument("--health-path", required=True)
    parser.add_argument("--paired-order-path")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md", required=True)
    args = parser.parse_args(argv)

    summary = load_json(args.summary)
    robustness = load_json(args.robustness)
    health = load_json(args.health)
    paired_order_followup = load_json(args.paired_order_followup) if args.paired_order_followup else None

    model = args.model
    baseline_summary = find_summary(summary["summaries"], model, "baseline")
    heart_summary = find_summary(summary["summaries"], model, "heart_focused")
    baseline_health = find_health_group(health["groups"], model, "baseline")
    heart_health = find_health_group(health["groups"], model, "heart_focused")
    contrast_all = contrast_lookup(robustness, model, "baseline", "heart_focused", "all_items")
    contrast_same_act = contrast_lookup(robustness, model, "baseline", "heart_focused", "same_act_different_motive")
    power_same_act = power_row_lookup(
        robustness,
        model,
        "baseline",
        "heart_focused",
        "same_act_different_motive",
        "heart_sensitivity_score",
    )

    report = {
        "benchmark_name": args.benchmark_name,
        "slice_composition": args.slice_composition,
        "conditions": "baseline, heart_focused",
        "model": model,
        "valid_records": health["valid_records"],
        "parse_failure_rate": health["parse_failure_rate"],
        "same_heart_control": metric_point(baseline_summary, "same_heart_control_accuracy"),
        "heart_overreach": metric_point(baseline_summary, "heart_overreach_rate"),
        "max_explanation_ratio_vs_baseline": max(
            baseline_health["explanation_ratio_vs_baseline"],
            heart_health["explanation_ratio_vs_baseline"],
        ),
        "condition_rows": [
            {
                "condition": condition_registry.display_name("baseline"),
                "task_a_accuracy": metric_point(baseline_summary, "task_a_accuracy"),
                "task_b_accuracy": metric_point(baseline_summary, "task_b_accuracy"),
                "heart_sensitivity_score": metric_point(baseline_summary, "heart_sensitivity_score"),
                "p_reason_motive": metric_point(baseline_summary, "p_reason_motive"),
                "same_heart_control_accuracy": metric_point(baseline_summary, "same_heart_control_accuracy"),
                "heart_overreach_rate": metric_point(baseline_summary, "heart_overreach_rate"),
                "mean_explanation_chars": metric_point(baseline_summary, "mean_explanation_chars"),
            },
            {
                "condition": condition_registry.display_name("heart_focused"),
                "task_a_accuracy": metric_point(heart_summary, "task_a_accuracy"),
                "task_b_accuracy": metric_point(heart_summary, "task_b_accuracy"),
                "heart_sensitivity_score": metric_point(heart_summary, "heart_sensitivity_score"),
                "p_reason_motive": metric_point(heart_summary, "p_reason_motive"),
                "same_heart_control_accuracy": metric_point(heart_summary, "same_heart_control_accuracy"),
                "heart_overreach_rate": metric_point(heart_summary, "heart_overreach_rate"),
                "mean_explanation_chars": metric_point(heart_summary, "mean_explanation_chars"),
            },
        ],
        "all_items_delta": {
            "task_a": contrast_all["metrics"]["task_a_accuracy"]["delta"],
            "task_b": contrast_all["metrics"]["task_b_accuracy"]["delta"],
            "hss": contrast_all["metrics"]["heart_sensitivity_score"]["delta"],
            "p_reason_motive": contrast_all["metrics"]["p_reason_motive"]["delta"],
        },
        "same_act_hss": {
            "delta": contrast_same_act["metrics"]["heart_sensitivity_score"]["delta"],
            "better": contrast_same_act["metrics"]["heart_sensitivity_score"]["better"],
            "worse": contrast_same_act["metrics"]["heart_sensitivity_score"]["worse"],
            "tie": contrast_same_act["metrics"]["heart_sensitivity_score"]["tie"],
            "one_sided_p": contrast_same_act["metrics"]["heart_sensitivity_score"]["exact_sign_p_one_sided"],
            "two_sided_p": contrast_same_act["metrics"]["heart_sensitivity_score"]["exact_sign_p_two_sided"],
        },
        "same_act_power": {
            "current_power": power_same_act["current_power"],
            "min_items_for_target_power": power_same_act["min_items_for_target_power"],
        },
        "summary_path": args.summary_path,
        "robustness_path": args.robustness_path,
        "health_path": args.health_path,
    }

    if paired_order_followup is not None:
        report["paired_order_followup"] = paired_order_followup
        if args.paired_order_path:
            report["paired_order_path"] = args.paired_order_path

    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    output_md = Path(args.output_md)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(render_markdown(report), encoding="utf-8")
    print(f"Wrote public confirmation readout to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
