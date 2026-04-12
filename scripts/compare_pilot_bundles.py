#!/usr/bin/env python3
"""Compare two pilot result bundles and summarize metric deltas."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


KEY_METRICS = [
    "task_b_accuracy",
    "heart_sensitivity_score",
    "surface_overweighting_index",
    "p_reason_motive",
    "motive_cross_task_consistency",
    "same_heart_control_accuracy",
    "heart_overreach_rate",
    "mean_explanation_chars",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def metric_point(record: Dict[str, Any], name: str) -> float | int | None:
    entry = record.get("metrics", {}).get(name)
    if isinstance(entry, dict):
        return entry.get("point")
    return entry


def round_delta(left: Any, right: Any) -> float | None:
    if left is None or right is None:
        return None
    return round(right - left, 4)


def swap_gap_index(rows: List[Dict[str, Any]]) -> Dict[Tuple[str, str, str], float | None]:
    index: Dict[Tuple[str, str, str], float | None] = {}
    for row in rows:
        model = row["model"]
        condition = row["condition"]
        for bucket in row.get("buckets", []):
            index[(model, condition, bucket["bucket"])] = bucket.get("task_b_swap_accuracy_gap")
    return index


def bundle_index(
    summary_path: Path,
    health_path: Path,
    swap_gap_path: Path,
) -> Dict[Tuple[str, str], Dict[str, Any]]:
    summary = load_json(summary_path)
    health = load_json(health_path)
    swap_gap = swap_gap_index(load_json(swap_gap_path))

    summary_rows = {
        (row["model"], row["condition"]): row
        for row in summary["summaries"]
    }
    health_rows = {
        (row["model"], row["condition"]): row
        for row in health["groups"]
    }

    index: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for key, row in summary_rows.items():
        health_row = health_rows.get(key, {})
        merged: Dict[str, Any] = {
            "parse_failure_rate": health.get("parse_failure_rate"),
            "task_b_swap_accuracy_gap": health_row.get("task_b_swap_accuracy_gap"),
            "same_act_swap_gap": swap_gap.get((*key, "same_act_different_motive")),
        }
        for metric in KEY_METRICS:
            merged[metric] = metric_point(row, metric)
        index[key] = merged
    return index


def build_rows(
    left_label: str,
    left_index: Dict[Tuple[str, str], Dict[str, Any]],
    right_label: str,
    right_index: Dict[Tuple[str, str], Dict[str, Any]],
) -> List[Dict[str, Any]]:
    keys = sorted(set(left_index) | set(right_index))
    rows: List[Dict[str, Any]] = []
    for model, condition in keys:
        left = left_index.get((model, condition), {})
        right = right_index.get((model, condition), {})
        row: Dict[str, Any] = {
            "model": model,
            "condition": condition,
            "left_label": left_label,
            "right_label": right_label,
        }
        for field in ("parse_failure_rate", "task_b_swap_accuracy_gap", "same_act_swap_gap", *KEY_METRICS):
            left_value = left.get(field)
            right_value = right.get(field)
            row[f"{left_label}_{field}"] = left_value
            row[f"{right_label}_{field}"] = right_value
            row[f"delta_{field}"] = round_delta(left_value, right_value)
        rows.append(row)
    return rows


def format_value(value: Any) -> str:
    if value is None:
        return "-"
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def build_markdown(rows: List[Dict[str, Any]], left_label: str, right_label: str) -> str:
    columns = [
        "model",
        "condition",
        f"{left_label}_heart_sensitivity_score",
        f"{right_label}_heart_sensitivity_score",
        "delta_heart_sensitivity_score",
        f"{left_label}_same_act_swap_gap",
        f"{right_label}_same_act_swap_gap",
        "delta_same_act_swap_gap",
        f"{left_label}_same_heart_control_accuracy",
        f"{right_label}_same_heart_control_accuracy",
        "delta_same_heart_control_accuracy",
        f"{left_label}_heart_overreach_rate",
        f"{right_label}_heart_overreach_rate",
        "delta_heart_overreach_rate",
        f"{left_label}_p_reason_motive",
        f"{right_label}_p_reason_motive",
        "delta_p_reason_motive",
        f"{left_label}_mean_explanation_chars",
        f"{right_label}_mean_explanation_chars",
        "delta_mean_explanation_chars",
    ]
    lines = [
        "# Pilot Bundle Comparison",
        "",
        f"Comparing `{left_label}` against `{right_label}`.",
        "",
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(format_value(row.get(column)) for column in columns) + " |")
    lines.append("")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--left-label", required=True, help="Short label for the first bundle")
    parser.add_argument("--left-summary", required=True, help="Summary JSON for the first bundle")
    parser.add_argument("--left-health", required=True, help="Health JSON for the first bundle")
    parser.add_argument("--left-swap-gap", required=True, help="Swap-gap JSON for the first bundle")
    parser.add_argument("--right-label", required=True, help="Short label for the second bundle")
    parser.add_argument("--right-summary", required=True, help="Summary JSON for the second bundle")
    parser.add_argument("--right-health", required=True, help="Health JSON for the second bundle")
    parser.add_argument("--right-swap-gap", required=True, help="Swap-gap JSON for the second bundle")
    parser.add_argument("--output-json", required=True, help="Write comparison rows as JSON")
    parser.add_argument("--output-md", required=True, help="Write comparison rows as Markdown")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    left_index = bundle_index(
        Path(args.left_summary),
        Path(args.left_health),
        Path(args.left_swap_gap),
    )
    right_index = bundle_index(
        Path(args.right_summary),
        Path(args.right_health),
        Path(args.right_swap_gap),
    )
    rows = build_rows(args.left_label, left_index, args.right_label, right_index)

    output_json = Path(args.output_json)
    output_md = Path(args.output_md)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    output_md.write_text(build_markdown(rows, args.left_label, args.right_label), encoding="utf-8")
    print(f"Wrote {len(rows)} comparison rows to {output_json}")
    print(f"Wrote markdown comparison to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
