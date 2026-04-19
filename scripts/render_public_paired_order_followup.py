#!/usr/bin/env python3
"""Render a compact paired-order follow-up summary for the public confirmation slice."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence

import condition_registry


def load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def render_markdown(report: Dict[str, Any]) -> str:
    lines: List[str] = [
        "# Public Confirmation Paired-Order Follow-Up",
        "",
        "## Setup",
        "",
        f"- Model: `{report['model']}`",
        f"- Slice: `{report['slice_description']}`",
        f"- Conditions: `{report['conditions']}`",
        f"- Complete paired-order records: `{report['paired_order_records']}`",
        "",
        "## Main Result",
        "",
        f"- Maximum item-level Task B order-flip rate: `{report['max_flip_rate']}`",
        f"- Maximum paired-order Task B accuracy gap: `{report['max_gap']}`",
        "",
        "| Condition | Paired-order Task B | Order flips | Paired gap | Correct both orders | Wrong both orders |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for row in report["rows"]:
        lines.append(
            "| {condition} | {task_b_accuracy} | {flip_rate} | {gap} | {correct_both} | {wrong_both} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- On this same-act follow-up, the public `baseline` and `heart_focused` conditions show no item-level Task B order flips.",
            "- The paired-order accuracy gap is zero in both public conditions, so the earlier split-based swap-gap should not be read as same-item order instability on this slice.",
            "",
            "## Primary File",
            "",
            f"- Source paired-order stability file: `{report['source_path']}`",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paired-order", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument(
        "--conditions",
        nargs="+",
        default=["baseline", "heart_focused"],
        help="Conditions to retain in the summary",
    )
    parser.add_argument("--source-path", required=True)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md", required=True)
    args = parser.parse_args(argv)

    paired_order = load_json(args.paired_order)
    groups = [
        row
        for row in paired_order["groups"]
        if row["model"] == args.model and row["condition"] in args.conditions
    ]
    groups.sort(key=lambda row: args.conditions.index(row["condition"]))

    if not groups:
        raise SystemExit("No paired-order groups matched the requested model and conditions.")

    report = {
        "model": args.model,
        "slice_description": "23 same_act_different_motive items in both A/B orders",
        "conditions": ", ".join(args.conditions),
        "paired_order_records": sum(group["n_complete_pairs"] for group in groups) * 2,
        "max_flip_rate": max(group["task_b_order_flip_rate"] for group in groups),
        "max_gap": max(group["task_b_accuracy_gap"] for group in groups),
        "rows": [
            {
                "condition": condition_registry.display_name(group["condition"]),
                "task_b_accuracy": group["task_b_accuracy_ab"],
                "flip_rate": group["task_b_order_flip_rate"],
                "gap": group["task_b_accuracy_gap"],
                "correct_both": group["correct_both_count"],
                "wrong_both": group["wrong_both_count"],
            }
            for group in groups
        ],
        "source_path": args.source_path,
    }

    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    output_md = Path(args.output_md)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(render_markdown(report), encoding="utf-8")
    print(f"Wrote paired-order follow-up to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
