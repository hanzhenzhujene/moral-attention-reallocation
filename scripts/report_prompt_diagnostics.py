#!/usr/bin/env python3
"""Report prompt scaffold length by condition."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Sequence

from transformers import AutoTokenizer

import condition_registry


PLACEHOLDER_RE = re.compile(r"\{\{[^{}]+\}\}")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_placeholders(text: str) -> str:
    return PLACEHOLDER_RE.sub("", text)


def token_count(tokenizer: AutoTokenizer, text: str) -> int:
    return len(tokenizer(text, add_special_tokens=False)["input_ids"])


def build_rows(prompt_dir: Path, conditions: Sequence[str], tokenizer: AutoTokenizer) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    prompt_kinds = (
        ("single_pass", condition_registry.single_pass_prompt_filename),
        ("task_ac", condition_registry.task_ac_prompt_filename),
        ("task_b", condition_registry.task_b_prompt_filename),
    )
    for condition in conditions:
        spec = condition_registry.get_condition_spec(condition)
        for prompt_kind, filename_fn in prompt_kinds:
            try:
                filename = filename_fn(condition)
            except ValueError:
                continue
            path = prompt_dir / filename
            if not path.exists():
                continue
            raw_text = load_text(path)
            scaffold = strip_placeholders(raw_text)
            rows.append(
                {
                    "condition": condition,
                    "display_name": spec["display_name"],
                    "family": spec["family"],
                    "prompt_kind": prompt_kind,
                    "prompt_path": str(path),
                    "scaffold_chars": len(scaffold),
                    "scaffold_tokens": token_count(tokenizer, scaffold),
                }
            )
    return rows


def render_markdown(rows: Sequence[Dict[str, Any]], model_id: str) -> str:
    lines = [
        "# Prompt Diagnostics",
        "",
        f"Tokenizer model: `{model_id}`",
        "",
        "| Condition | Family | Prompt kind | Chars | Tokens |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['display_name']} | {row['family']} | {row['prompt_kind']} | {row['scaffold_chars']} | {row['scaffold_tokens']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt-dir", required=True)
    parser.add_argument("--conditions", nargs="+", required=True)
    parser.add_argument("--model-id", default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md")
    args = parser.parse_args(argv)

    tokenizer = AutoTokenizer.from_pretrained(args.model_id)
    rows = build_rows(Path(args.prompt_dir), args.conditions, tokenizer)

    output_json = Path(args.output_json)
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"Wrote prompt diagnostics to {output_json}")

    if args.output_md:
        output_md = Path(args.output_md)
        output_md.parent.mkdir(parents=True, exist_ok=True)
        output_md.write_text(render_markdown(rows, args.model_id), encoding="utf-8")
        print(f"Wrote markdown diagnostics to {output_md}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
