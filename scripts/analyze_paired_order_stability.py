#!/usr/bin/env python3
"""Analyze item-level paired-order stability for Task B."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


VALID_ORDER_VARIANTS = {"ab", "ba"}
VALID_LABELS = {"A", "B", "Same"}


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def remap_to_source(row: Dict[str, Any], label: str) -> str:
    if label == "Same":
        return "Same"
    if label == "A":
        return str(row["presented_case_a_source"])
    if label == "B":
        return str(row["presented_case_b_source"])
    raise ValueError(f"Unexpected label: {label}")


def row_correct(row: Dict[str, Any]) -> bool:
    return (
        row["response"]["task_b_worse_inward_orientation"]
        == row["gold"]["task_b_worse_inward_orientation"]
    )


def stable_group_key(row: Dict[str, Any]) -> Tuple[str, str, str]:
    return (
        row["model"],
        row["condition"],
        str(row.get("paired_order_group_id") or f"{row['item_id']}__{row['condition']}"),
    )


def summarize_group(rows: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    by_order = {row["order_variant"]: row for row in rows}
    if set(by_order) != VALID_ORDER_VARIANTS:
        raise ValueError(
            f"Expected paired-order group with both ab/ba variants, got {sorted(by_order)}"
        )
    ab_row = by_order["ab"]
    ba_row = by_order["ba"]
    ab_label = ab_row["response"]["task_b_worse_inward_orientation"]
    ba_label = ba_row["response"]["task_b_worse_inward_orientation"]
    if ab_label not in VALID_LABELS or ba_label not in VALID_LABELS:
        raise ValueError("Unexpected Task B label in paired-order analysis")
    ab_source = remap_to_source(ab_row, ab_label)
    ba_source = remap_to_source(ba_row, ba_label)
    return {
        "item_id": ab_row["item_id"],
        "pair_type": ab_row["pair_type"],
        "benchmark_source": ab_row["benchmark_source"],
        "condition": ab_row["condition"],
        "model": ab_row["model"],
        "ab_job_id": ab_row["job_id"],
        "ba_job_id": ba_row["job_id"],
        "task_b_label_ab": ab_label,
        "task_b_label_ba": ba_label,
        "task_b_source_ab": ab_source,
        "task_b_source_ba": ba_source,
        "task_b_correct_ab": row_correct(ab_row),
        "task_b_correct_ba": row_correct(ba_row),
        "task_b_order_flip": ab_source != ba_source,
        "task_b_accuracy_delta_ab_minus_ba": int(row_correct(ab_row)) - int(row_correct(ba_row)),
        "swapped_ab": ab_row["swapped"],
        "swapped_ba": ba_row["swapped"],
    }


def mean(values: Iterable[int | float]) -> float | None:
    values = list(values)
    if not values:
        return None
    return round(sum(values) / len(values), 4)


def render_markdown(groups: Sequence[Dict[str, Any]]) -> str:
    lines = [
        "# Paired-Order Stability Report",
        "",
    ]
    for group in groups:
        lines.extend(
            [
                f"## {group['model']} / {group['condition']}",
                "",
                "- complete pairs: `{}`".format(group["n_complete_pairs"]),
                "- order-flip rate: `{}`".format(group["task_b_order_flip_rate"]),
                "- Task B accuracy (`ab`): `{}`".format(group["task_b_accuracy_ab"]),
                "- Task B accuracy (`ba`): `{}`".format(group["task_b_accuracy_ba"]),
                "- paired accuracy gap: `{}`".format(group["task_b_accuracy_gap"]),
                "- correct both: `{}`".format(group["correct_both_count"]),
                "- `ab` only correct: `{}`".format(group["ab_only_correct_count"]),
                "- `ba` only correct: `{}`".format(group["ba_only_correct_count"]),
                "- wrong both: `{}`".format(group["wrong_both_count"]),
                "",
                "| Item | Pair type | Choice (`ab`) | Choice (`ba`) | Correct `ab` | Correct `ba` | Flip |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for item in group["items"]:
            lines.append(
                "| {item_id} | {pair_type} | {ab} | {ba} | {cab} | {cba} | {flip} |".format(
                    item_id=item["item_id"],
                    pair_type=item["pair_type"],
                    ab=item["task_b_source_ab"],
                    ba=item["task_b_source_ba"],
                    cab=item["task_b_correct_ab"],
                    cba=item["task_b_correct_ba"],
                    flip=item["task_b_order_flip"],
                )
            )
        lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", nargs="+", required=True, help="Run JSONL files")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md")
    args = parser.parse_args(argv)

    rows: List[Dict[str, Any]] = []
    for raw_path in args.input:
        rows.extend(load_jsonl(Path(raw_path)))

    paired_rows = [row for row in rows if row.get("order_variant") in VALID_ORDER_VARIANTS]
    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    item_groups: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = defaultdict(list)

    for row in paired_rows:
        item_groups[stable_group_key(row)].append(row)

    per_item: List[Dict[str, Any]] = []
    for (model, condition, _), group_rows in sorted(item_groups.items()):
        summary = summarize_group(group_rows)
        per_item.append(summary)
        grouped[(model, condition)].append(summary)

    output_groups: List[Dict[str, Any]] = []
    for (model, condition), items in sorted(grouped.items()):
        correct_both = sum(1 for item in items if item["task_b_correct_ab"] and item["task_b_correct_ba"])
        ab_only = sum(1 for item in items if item["task_b_correct_ab"] and not item["task_b_correct_ba"])
        ba_only = sum(1 for item in items if not item["task_b_correct_ab"] and item["task_b_correct_ba"])
        wrong_both = sum(1 for item in items if not item["task_b_correct_ab"] and not item["task_b_correct_ba"])
        accuracy_ab = mean(int(item["task_b_correct_ab"]) for item in items)
        accuracy_ba = mean(int(item["task_b_correct_ba"]) for item in items)
        gap = None if accuracy_ab is None or accuracy_ba is None else round(abs(accuracy_ab - accuracy_ba), 4)
        output_groups.append(
            {
                "model": model,
                "condition": condition,
                "n_complete_pairs": len(items),
                "task_b_order_flip_rate": mean(int(item["task_b_order_flip"]) for item in items),
                "task_b_accuracy_ab": accuracy_ab,
                "task_b_accuracy_ba": accuracy_ba,
                "task_b_accuracy_gap": gap,
                "correct_both_count": correct_both,
                "ab_only_correct_count": ab_only,
                "ba_only_correct_count": ba_only,
                "wrong_both_count": wrong_both,
                "items": items,
            }
        )

    report = {
        "groups": output_groups,
        "items": per_item,
    }

    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote paired-order JSON to {output_json}")

    if args.output_md:
        output_md = Path(args.output_md)
        output_md.parent.mkdir(parents=True, exist_ok=True)
        output_md.write_text(render_markdown(output_groups), encoding="utf-8")
        print(f"Wrote paired-order markdown to {output_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
