#!/usr/bin/env python3
"""Render a compact stage-status report for the 6-condition text-anchor pilot."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


def load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def find_group(groups: Iterable[Dict[str, Any]], model: str, condition: str) -> Dict[str, Any]:
    for group in groups:
        if group["model"] == model and group["condition"] == condition:
            return group
    raise KeyError(f"Missing group for {model} / {condition}")


def metric_point(group: Dict[str, Any], metric_name: str) -> float | None:
    metric = group["metrics"].get(metric_name)
    if metric is None:
        return None
    return metric.get("point")


def render_markdown(report: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Text-Anchor Extension Stage Report",
        "",
        "## Executive Summary",
        "",
        f"- Pilot matrix completed: `{report['pilot_calls']}` valid records across `{report['pilot_models']}` models and `{report['pilot_conditions']}` conditions.",
        f"- Paired-order diagnostic completed: `{report['paired_order_calls']}` valid records on the held-out `same_act_different_motive` slice.",
        f"- Parse failure rate: `{report['parse_failure_rate']}`.",
        f"- Same-heart control accuracy stayed `{report['same_heart_control_min']}` in every pilot cell.",
        f"- Heart overreach stayed `{report['heart_overreach_max']}` in every pilot cell.",
        f"- Paired-order Task B flip rate: `{report['paired_order_flip_rate_max']}` maximum across all model-condition cells.",
        f"- Paired-order Task B gap: `{report['paired_order_gap_max']}` maximum across all model-condition cells.",
        "",
        "## Formal Blockers Under The Original Pilot-Health Contract",
        "",
    ]
    for failure in report["pilot_failures"]:
        lines.append(f"- {failure}")
    lines.extend(
        [
            "",
        "## What The Pilot Supports",
        "",
        ]
    )

    for block in report["model_blocks"]:
        lines.extend(
            [
                f"### {block['model']}",
                "",
                f"- `baseline` Task B / HSS: `{block['baseline_task_b']}` / `{block['baseline_hss']}`",
                f"- `heart_focused` Task B / HSS: `{block['heart_task_b']}` / `{block['heart_hss']}`",
                f"- supportive text anchors: `{block['supportive_anchor_count']}` / `{block['anchor_count']}`",
                f"- stable same-heart controls across anchors: `{block['stable_control_count']}` / `{block['anchor_count']}`",
                f"- non-increased overreach across anchors: `{block['non_increased_overreach_count']}` / `{block['anchor_count']}`",
                "",
                "| Condition | Task B | HSS | Delta vs baseline HSS | Pilot split swap-gap | Paired-order gap | Order flips |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in block["rows"]:
            lines.append(
                "| {condition} | {task_b} | {hss} | {delta_hss} | {split_gap} | {paired_gap} | {flip_rate} |".format(
                    **row
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Diagnostic Interpretation",
            "",
            "- The held-out paired-order pack shows no item-level Task B order flips on the `same_act_different_motive` pilot slice.",
            "- That means the residual pilot swap-gap is better interpreted as a split-composition artifact in the balanced-job pilot, not as genuine same-item order instability on this slice.",
            "- The remaining substantive weakness is not guardrail failure. It is model dependence: the 4 text anchors help `Qwen-1.5B-Instruct`, but they hurt `Qwen-0.5B-Instruct`.",
            "- The current 6-condition extension is therefore stronger as an exploratory family result than as a freeze-grade cross-model main claim.",
            "",
            "## Recommended Next Step",
            "",
            "- Keep the 6-condition prompt package and benchmark fixed.",
            "- Do not do another broad prompt rewrite purely to chase the old split-based swap-gap metric.",
            "- Do not launch a freeze-grade 63-item six-condition confirmation run yet.",
            "- First update the decision memo to distinguish split-based swap-gap from paired-order instability; after that, the clean exploratory next run is a `Qwen-1.5B-Instruct` 63-item family confirmation, explicitly labeled non-frozen.",
            "",
            "## Primary Files",
            "",
            f"- Pilot readout: `{report['pilot_readout_path']}`",
            f"- Text-anchor family summary: `{report['family_summary_path']}`",
            f"- Paired-order stability report: `{report['paired_order_report_path']}`",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pilot-health", required=True)
    parser.add_argument("--pilot-summary", required=True)
    parser.add_argument("--family-summary", required=True)
    parser.add_argument("--pilot-swap-gap", required=True)
    parser.add_argument("--paired-order", required=True)
    parser.add_argument("--pilot-readout-path", required=True)
    parser.add_argument("--family-summary-path", required=True)
    parser.add_argument("--paired-order-report-path", required=True)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md", required=True)
    args = parser.parse_args()

    pilot_health = load_json(args.pilot_health)
    pilot_summary = load_json(args.pilot_summary)
    family_summary = load_json(args.family_summary)
    pilot_swap_gap = load_json(args.pilot_swap_gap)
    paired_order = load_json(args.paired_order)

    summary_groups = pilot_summary["summaries"]
    swap_gap_lookup: Dict[Tuple[str, str], float | None] = {}
    for group in pilot_swap_gap:
        same_act_bucket = next(
            (bucket for bucket in group["buckets"] if bucket["bucket"] == "same_act_different_motive"),
            None,
        )
        swap_gap_lookup[(group["model"], group["condition"])] = (
            None if same_act_bucket is None else same_act_bucket["task_b_swap_accuracy_gap"]
        )

    paired_lookup = {
        (group["model"], group["condition"]): group
        for group in paired_order["groups"]
    }

    model_blocks: List[Dict[str, Any]] = []
    for model_block in family_summary:
        model = model_block["model"]
        baseline = find_group(summary_groups, model, "baseline")
        heart = find_group(summary_groups, model, "heart_focused")
        rows: List[Dict[str, Any]] = []
        for anchor in model_block["per_condition"]:
            condition = anchor["condition"]
            summary = find_group(summary_groups, model, condition)
            paired = paired_lookup[(model, condition)]
            rows.append(
                {
                    "condition": anchor["display_name"],
                    "task_b": metric_point(summary, "task_b_accuracy"),
                    "hss": metric_point(summary, "heart_sensitivity_score"),
                    "delta_hss": anchor["delta_vs_baseline"]["heart_sensitivity_score"],
                    "split_gap": swap_gap_lookup[(model, condition)],
                    "paired_gap": paired["task_b_accuracy_gap"],
                    "flip_rate": paired["task_b_order_flip_rate"],
                }
            )
        heart_paired = paired_lookup[(model, "heart_focused")]
        model_blocks.append(
            {
                "model": model,
                "baseline_task_b": metric_point(baseline, "task_b_accuracy"),
                "baseline_hss": metric_point(baseline, "heart_sensitivity_score"),
                "heart_task_b": metric_point(heart, "task_b_accuracy"),
                "heart_hss": metric_point(heart, "heart_sensitivity_score"),
                "supportive_anchor_count": model_block["supportive_text_anchor_count"],
                "stable_control_count": model_block["stable_same_heart_control_count"],
                "non_increased_overreach_count": model_block["non_increased_overreach_count"],
                "anchor_count": len(model_block["per_condition"]),
                "rows": [
                    {
                        "condition": "heart_focused",
                        "task_b": metric_point(heart, "task_b_accuracy"),
                        "hss": metric_point(heart, "heart_sensitivity_score"),
                        "delta_hss": round(
                            metric_point(heart, "heart_sensitivity_score")
                            - metric_point(baseline, "heart_sensitivity_score"),
                            4,
                        ),
                        "split_gap": swap_gap_lookup[(model, "heart_focused")],
                        "paired_gap": heart_paired["task_b_accuracy_gap"],
                        "flip_rate": heart_paired["task_b_order_flip_rate"],
                    },
                    *rows,
                ],
            }
        )

    paired_groups = paired_order["groups"]
    report = {
        "pilot_calls": pilot_health["valid_records"],
        "pilot_models": len(pilot_health["expected_models"]),
        "pilot_conditions": len({group["condition"] for group in pilot_health["groups"]}),
        "paired_order_calls": sum(group["n_complete_pairs"] for group in paired_groups) * 2,
        "parse_failure_rate": pilot_health["parse_failure_rate"],
        "same_heart_control_min": min(
            metric_point(group, "same_heart_control_accuracy") for group in pilot_health["groups"]
        ),
        "heart_overreach_max": max(
            metric_point(group, "heart_overreach_rate") for group in pilot_health["groups"]
        ),
        "paired_order_flip_rate_max": max(group["task_b_order_flip_rate"] for group in paired_groups),
        "paired_order_gap_max": max(group["task_b_accuracy_gap"] for group in paired_groups),
        "pilot_failures": pilot_health["failures"],
        "model_blocks": model_blocks,
        "pilot_readout_path": args.pilot_readout_path,
        "family_summary_path": args.family_summary_path,
        "paired_order_report_path": args.paired_order_report_path,
    }

    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    output_md = Path(args.output_md)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(render_markdown(report), encoding="utf-8")
    print(f"Wrote stage report to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
