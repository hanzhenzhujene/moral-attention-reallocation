#!/usr/bin/env python3
"""Summarize text-anchored conditions against baseline and heart-focused references."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence

import condition_registry


SUMMARY_METRICS = (
    "task_a_accuracy",
    "task_b_accuracy",
    "heart_sensitivity_score",
    "p_reason_motive",
    "same_heart_control_accuracy",
    "heart_overreach_rate",
    "mean_explanation_chars",
)

FAMILY_MEAN_METRICS = (
    "task_b_accuracy",
    "heart_sensitivity_score",
    "p_reason_motive",
    "same_heart_control_accuracy",
    "heart_overreach_rate",
)


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def point(metrics: Dict[str, Any], metric_name: str) -> float | None:
    value = metrics.get(metric_name, {}).get("point")
    return None if value is None else float(value)


def round_or_none(value: float | None) -> float | None:
    return None if value is None else round(value, 4)


def render_markdown(report: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "# Text-Anchor Family Summary",
        "",
    ]
    for model_report in report:
        lines.extend(
            [
                f"## {model_report['model']}",
                "",
                "| Condition | vs baseline Task B | vs baseline HSS | vs heart-focused HSS | Same-heart stable | Overreach non-increase |",
                "| --- | ---: | ---: | ---: | --- | --- |",
            ]
        )
        for row in model_report["per_condition"]:
            lines.append(
                f"| {row['display_name']} | {row['delta_vs_baseline']['task_b_accuracy']} | {row['delta_vs_baseline']['heart_sensitivity_score']} | {row['delta_vs_heart_focused']['heart_sensitivity_score']} | {row['stable_same_heart_controls']} | {row['non_increased_overreach']} |"
            )
        lines.extend(
            [
                "",
                "| Family mean delta vs baseline | Task B | HSS | P(reason=motive) | Same-heart control | Overreach |",
                "| --- | ---: | ---: | ---: | ---: | ---: |",
                "| Mean | {task_b_accuracy} | {heart_sensitivity_score} | {p_reason_motive} | {same_heart_control_accuracy} | {heart_overreach_rate} |".format(
                    **model_report["family_mean_delta_vs_baseline"]
                ),
                "",
                "- supportive text anchors: `{supportive_text_anchor_count}`".format(**model_report),
                "- non-increased overreach anchors: `{non_increased_overreach_count}`".format(**model_report),
                "- stable same-heart anchors: `{stable_same_heart_control_count}`".format(**model_report),
                "",
            ]
        )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--baseline", default="baseline")
    parser.add_argument("--reference", default="heart_focused")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md")
    args = parser.parse_args(argv)

    summary = load_json(Path(args.summary))
    grouped: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for row in summary["summaries"]:
        grouped.setdefault(row["model"], {})[row["condition"]] = row["metrics"]

    report: List[Dict[str, Any]] = []
    for model, condition_map in sorted(grouped.items()):
        baseline_metrics = condition_map.get(args.baseline)
        reference_metrics = condition_map.get(args.reference)
        if baseline_metrics is None or reference_metrics is None:
            continue

        per_condition: List[Dict[str, Any]] = []
        family_means: Dict[str, List[float]] = {metric_name: [] for metric_name in FAMILY_MEAN_METRICS}
        supportive_count = 0
        non_increased_overreach_count = 0
        stable_same_heart_control_count = 0

        for condition in condition_registry.TEXT_ANCHOR_CONDITIONS:
            metrics = condition_map.get(condition)
            if metrics is None:
                continue

            delta_vs_baseline: Dict[str, float | None] = {}
            delta_vs_reference: Dict[str, float | None] = {}
            for metric_name in SUMMARY_METRICS:
                baseline_value = point(baseline_metrics, metric_name)
                reference_value = point(reference_metrics, metric_name)
                condition_value = point(metrics, metric_name)
                delta_vs_baseline[metric_name] = (
                    None if baseline_value is None or condition_value is None else round(condition_value - baseline_value, 4)
                )
                delta_vs_reference[metric_name] = (
                    None if reference_value is None or condition_value is None else round(condition_value - reference_value, 4)
                )
            for metric_name in FAMILY_MEAN_METRICS:
                delta_value = delta_vs_baseline[metric_name]
                if delta_value is not None:
                    family_means[metric_name].append(float(delta_value))

            baseline_same_heart = point(baseline_metrics, "same_heart_control_accuracy")
            baseline_overreach = point(baseline_metrics, "heart_overreach_rate")
            condition_same_heart = point(metrics, "same_heart_control_accuracy")
            condition_overreach = point(metrics, "heart_overreach_rate")
            hss_delta = delta_vs_baseline["heart_sensitivity_score"]

            stable_same_heart_controls = (
                baseline_same_heart is not None
                and condition_same_heart is not None
                and condition_same_heart >= baseline_same_heart
            )
            non_increased_overreach = (
                baseline_overreach is not None
                and condition_overreach is not None
                and condition_overreach <= baseline_overreach
            )
            supportive_anchor = (
                hss_delta is not None
                and hss_delta > 0
                and non_increased_overreach
                and stable_same_heart_controls
            )
            if supportive_anchor:
                supportive_count += 1
            if non_increased_overreach:
                non_increased_overreach_count += 1
            if stable_same_heart_controls:
                stable_same_heart_control_count += 1

            per_condition.append(
                {
                    "condition": condition,
                    "display_name": condition_registry.display_name(condition),
                    "delta_vs_baseline": delta_vs_baseline,
                    "delta_vs_heart_focused": delta_vs_reference,
                    "stable_same_heart_controls": stable_same_heart_controls,
                    "non_increased_overreach": non_increased_overreach,
                    "supportive_anchor": supportive_anchor,
                }
            )

        family_mean_delta_vs_baseline = {
            metric_name: round_or_none(sum(values) / len(values) if values else None)
            for metric_name, values in family_means.items()
        }
        report.append(
            {
                "model": model,
                "baseline_condition": args.baseline,
                "reference_condition": args.reference,
                "per_condition": per_condition,
                "family_mean_delta_vs_baseline": family_mean_delta_vs_baseline,
                "supportive_text_anchor_count": supportive_count,
                "non_increased_overreach_count": non_increased_overreach_count,
                "stable_same_heart_control_count": stable_same_heart_control_count,
            }
        )

    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote text-anchor family summary to {output_json}")

    if args.output_md:
        output_md = Path(args.output_md)
        output_md.parent.mkdir(parents=True, exist_ok=True)
        output_md.write_text(render_markdown(report), encoding="utf-8")
        print(f"Wrote markdown family summary to {output_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
