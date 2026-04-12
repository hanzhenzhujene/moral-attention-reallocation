#!/usr/bin/env python3
"""Evaluate paired-order Task B behavior for a diagnostic job pack."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def canonical_label(record: Dict[str, Any]) -> str:
    response = record["response"]["task_b_worse_inward_orientation"]
    if response == "Same":
        return "Same"
    if not record.get("swapped"):
        return "case_a" if response == "A" else "case_b"
    return "case_b" if response == "A" else "case_a"


def task_b_correct(record: Dict[str, Any]) -> int:
    return int(
        record["response"]["task_b_worse_inward_orientation"]
        == record["gold"]["task_b_worse_inward_orientation"]
    )


def safe_rate(values: Iterable[int]) -> float | None:
    values = list(values)
    if not values:
        return None
    return round(sum(values) / len(values), 4)


def compare_pair(
    rows: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    by_order = {("ba" if row.get("swapped") else "ab"): row for row in rows}
    ab = by_order.get("ab")
    ba = by_order.get("ba")
    if ab is None or ba is None:
        raise ValueError(f"Expected both ab and ba rows, got {[bool(row.get('swapped')) for row in rows]}")
    ab_choice = canonical_label(ab)
    ba_choice = canonical_label(ba)
    ab_correct = task_b_correct(ab)
    ba_correct = task_b_correct(ba)
    return {
        "paired_order_group_id": f"{ab['item_id']}__{ab['condition']}",
        "item_id": ab["item_id"],
        "model": ab["model"],
        "condition": ab["condition"],
        "pair_type": ab["pair_type"],
        "ab_task_b_presented_label": ab["response"]["task_b_worse_inward_orientation"],
        "ba_task_b_presented_label": ba["response"]["task_b_worse_inward_orientation"],
        "ab_task_b_canonical_choice": ab_choice,
        "ba_task_b_canonical_choice": ba_choice,
        "ab_task_b_correct": ab_correct,
        "ba_task_b_correct": ba_correct,
        "order_flip": ab_choice != ba_choice,
        "paired_correctness_delta": ba_correct - ab_correct,
    }


def render_markdown(summary_rows: Sequence[Dict[str, Any]], item_rows: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "# Paired-Order Diagnostic",
        "",
        "## Cell Summary",
        "",
        "| Model | Condition | n pairs | AB acc | BA acc | paired delta | order-flip rate | both correct | either correct |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in summary_rows:
        lines.append(
            "| {model} | {condition} | {n_pairs} | {ab_accuracy} | {ba_accuracy} | {paired_correctness_delta} | {order_flip_rate} | {both_correct_rate} | {either_correct_rate} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "## Item Detail",
            "",
            "| Model | Condition | Item | AB canonical | BA canonical | AB correct | BA correct | flip |",
            "| --- | --- | --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in item_rows:
        lines.append(
            "| {model} | {condition} | {item_id} | {ab_task_b_canonical_choice} | {ba_task_b_canonical_choice} | {ab_task_b_correct} | {ba_task_b_correct} | {order_flip} |".format(
                **row
            )
        )
    lines.append("")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", nargs="+", required=True, help="Run JSONL files from paired-order jobs")
    parser.add_argument("--output-json", required=True, help="JSON output path")
    parser.add_argument("--output-md", required=True, help="Markdown output path")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    rows: List[Dict[str, Any]] = []
    for raw_path in args.input:
        rows.extend(load_jsonl(Path(raw_path)))

    grouped: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (row["model"], row["condition"], row["item_id"])
        grouped[key].append(row)

    item_rows = [compare_pair(group_rows) for _, group_rows in sorted(grouped.items())]

    summary_groups: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in item_rows:
        summary_groups[(row["model"], row["condition"])].append(row)

    summary_rows: List[Dict[str, Any]] = []
    for (model, condition), group_rows in sorted(summary_groups.items()):
        summary_rows.append(
            {
                "model": model,
                "condition": condition,
                "n_pairs": len(group_rows),
                "ab_accuracy": safe_rate(row["ab_task_b_correct"] for row in group_rows),
                "ba_accuracy": safe_rate(row["ba_task_b_correct"] for row in group_rows),
                "paired_correctness_delta": safe_rate(row["paired_correctness_delta"] for row in group_rows),
                "order_flip_rate": safe_rate(int(row["order_flip"]) for row in group_rows),
                "both_correct_rate": safe_rate(
                    int(row["ab_task_b_correct"] == 1 and row["ba_task_b_correct"] == 1)
                    for row in group_rows
                ),
                "either_correct_rate": safe_rate(
                    int(row["ab_task_b_correct"] == 1 or row["ba_task_b_correct"] == 1)
                    for row in group_rows
                ),
            }
        )

    payload = {
        "summary": summary_rows,
        "items": item_rows,
    }

    output_json = Path(args.output_json)
    output_md = Path(args.output_md)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    output_md.write_text(render_markdown(summary_rows, item_rows), encoding="utf-8")

    for row in summary_rows:
        print(
            f"{row['model']} | {row['condition']} | n={row['n_pairs']} | "
            f"AB={row['ab_accuracy']} | BA={row['ba_accuracy']} | "
            f"flip={row['order_flip_rate']} | delta={row['paired_correctness_delta']}"
        )
    print(f"Wrote paired-order diagnostic JSON to {output_json}")
    print(f"Wrote paired-order diagnostic markdown to {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
