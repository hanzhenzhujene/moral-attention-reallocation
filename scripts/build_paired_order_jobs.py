#!/usr/bin/env python3
"""Build a paired-order diagnostic job pack with both A/B presentations for each item."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

import build_prompt_jobs


def load_all_items(paths: Iterable[str]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for raw_path in paths:
        items.extend(build_prompt_jobs.load_items(Path(raw_path)))
    return items


def match_filters(item: Dict[str, Any], pair_types: Sequence[str], item_ids: Sequence[str]) -> bool:
    if pair_types and item["pair_type"] not in pair_types:
        return False
    if item_ids and item["item_id"] not in item_ids:
        return False
    return True


def build_jobs(
    items: Sequence[Dict[str, Any]],
    conditions: Sequence[str],
    scripture_block: str,
    prompt_dir: Path,
) -> List[Dict[str, Any]]:
    jobs: List[Dict[str, Any]] = []
    for item in items:
        for condition in conditions:
            template_path = build_prompt_jobs.condition_prompt_path(condition, prompt_dir)
            template_text = template_path.read_text(encoding="utf-8")
            for order_variant, swap in (("ab", False), ("ba", True)):
                presented_case_a = item["case_b"] if swap else item["case_a"]
                presented_case_b = item["case_a"] if swap else item["case_b"]
                gold_a = (
                    build_prompt_jobs.flip_ab(item["gold"]["task_a_more_morally_problematic"])
                    if swap
                    else item["gold"]["task_a_more_morally_problematic"]
                )
                gold_b = (
                    build_prompt_jobs.flip_ab(item["gold"]["task_b_worse_inward_orientation"])
                    if swap
                    else item["gold"]["task_b_worse_inward_orientation"]
                )
                jobs.append(
                    {
                        "job_id": f"{item['item_id']}__{condition}__{order_variant}",
                        "paired_order_group_id": f"{item['item_id']}__{condition}",
                        "order_variant": order_variant,
                        "item_id": item["item_id"],
                        "benchmark_source": item["benchmark_source"],
                        "condition": condition,
                        "pair_type": item["pair_type"],
                        "primary_diagnostic_dimension": item["primary_diagnostic_dimension"],
                        "domain": item["domain"],
                        "difficulty": item["difficulty"],
                        "swapped": swap,
                        "prompt_template_path": str(template_path),
                        "presented_case_a_source": "case_b" if swap else "case_a",
                        "presented_case_b_source": "case_a" if swap else "case_b",
                        "gold": {
                            "task_a_more_morally_problematic": gold_a,
                            "task_b_worse_inward_orientation": gold_b,
                            "task_c_primary_reason": item["gold"]["task_c_primary_reason"],
                            "adjudication_note": item["gold"]["adjudication_note"],
                        },
                        "prompt": build_prompt_jobs.rendered_prompt(
                            template_text,
                            presented_case_a,
                            presented_case_b,
                            scripture_block,
                        ),
                    }
                )
    return jobs


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--items", nargs="+", required=True, help="Benchmark JSON files to include")
    parser.add_argument(
        "--conditions",
        nargs="+",
        default=["baseline", "christian_heart", "secular_matched"],
        help="Prompt conditions to render",
    )
    parser.add_argument(
        "--pair-types",
        nargs="+",
        default=["same_act_different_motive"],
        help="Only include these pair types",
    )
    parser.add_argument(
        "--item-ids",
        nargs="*",
        default=[],
        help="Optional explicit item ids to include after pair-type filtering",
    )
    parser.add_argument(
        "--scripture-block",
        default=build_prompt_jobs.DEFAULT_SCRIPTURE_BLOCK,
        help="Replacement text for the scripture block placeholder",
    )
    parser.add_argument(
        "--prompt-dir",
        default=str(build_prompt_jobs.DEFAULT_PROMPT_DIR),
        help="Directory containing prompt template files",
    )
    parser.add_argument("--output", required=True, help="Output JSONL path")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    raw_items = load_all_items(args.items)
    filtered_items = [
        item for item in raw_items if match_filters(item, args.pair_types, args.item_ids)
    ]
    filtered_items.sort(key=lambda item: item["item_id"])

    jobs = build_jobs(
        filtered_items,
        args.conditions,
        args.scripture_block,
        Path(args.prompt_dir),
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_path, jobs)
    print(f"Wrote {len(jobs)} paired-order jobs to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
