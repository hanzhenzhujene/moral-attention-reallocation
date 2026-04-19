#!/usr/bin/env python3
"""Render full exploratory 6-condition comparison tables for README and paper."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

import condition_registry


CONDITION_ORDER: Tuple[str, ...] = (
    "baseline",
    "heart_focused",
    "proverbs_4_23",
    "dhammapada_34",
    "bhagavad_gita_15_15",
    "quran_26_88_89",
)


ABSOLUTE_METRICS: Tuple[Tuple[str, str, int, str], ...] = (
    ("Task A overall verdict", "task_a_accuracy", 4, "summary"),
    ("Task B inward-orientation judgment", "task_b_accuracy", 4, "summary"),
    ("Task C motive as primary reason", "p_reason_motive", 4, "summary"),
    ("Heart-sensitivity score", "heart_sensitivity_score", 4, "summary"),
    ("Same-heart control accuracy", "same_heart_control_accuracy", 4, "summary"),
    ("Heart overreach rate", "heart_overreach_rate", 4, "summary"),
    ("Mean explanation chars", "mean_explanation_chars", 1, "summary"),
    ("Paired-order Task B", "task_b_accuracy_ab", 4, "paired"),
    ("Order-flip rate", "task_b_order_flip_rate", 4, "paired"),
    ("Paired-order Task B gap", "task_b_accuracy_gap", 4, "paired"),
)


DELTA_METRICS: Tuple[Tuple[str, str, int], ...] = (
    ("Delta Task A", "task_a_accuracy", 4),
    ("Delta Task B", "task_b_accuracy", 4),
    ("Delta Task C", "p_reason_motive", 4),
    ("Delta HSS", "heart_sensitivity_score", 4),
    ("Delta explanation chars", "mean_explanation_chars", 1),
)


def load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def find_row(rows: Iterable[Dict[str, Any]], *, model: str, condition: str) -> Dict[str, Any]:
    for row in rows:
        if row["model"] == model and row["condition"] == condition:
            return row
    raise KeyError(f"Missing row for model={model}, condition={condition}")


def format_value(value: float, digits: int) -> str:
    return f"{value:.{digits}f}"


def format_delta(value: float, digits: int) -> str:
    return f"{value:+.{digits}f}"


def markdown_condition_label(condition: str) -> str:
    spec = condition_registry.get_condition_spec(condition)
    label = spec.get("display_name", condition)
    tradition = spec.get("tradition_label")
    if tradition:
        return f"{label}<br><sub>{tradition}</sub>"
    if condition == "heart_focused":
        return "Heart-focused<br><sub>Generic scaffold</sub>"
    return "Baseline<br><sub>No religious text</sub>"


def latex_escape(text: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def latex_condition_label(condition: str) -> str:
    spec = condition_registry.get_condition_spec(condition)
    label = latex_escape(spec.get("display_name", condition))
    tradition = spec.get("tradition_label")
    if tradition:
        return r"\shortstack[c]{" + f"{label}\\\\{{\\footnotesize {latex_escape(tradition)}}}" + "}"
    if condition == "heart_focused":
        return r"\shortstack[c]{" + f"{label}\\\\{{\\footnotesize Generic scaffold}}" + "}"
    return r"\shortstack[c]{" + f"{label}\\\\{{\\footnotesize No religious text}}" + "}"


def paired_status(flip_rate: float, gap: float) -> str:
    if abs(flip_rate) < 1e-9 and abs(gap) < 1e-9:
        return "yes"
    return f"flip={flip_rate:.4f}, gap={gap:.4f}"


def build_tables(summary: Dict[str, Any], paired_order: Dict[str, Any], model: str) -> Dict[str, Any]:
    summary_map = {
        condition: find_row(summary["summaries"], model=model, condition=condition)
        for condition in CONDITION_ORDER
    }
    paired_map = {
        condition: find_row(paired_order["groups"], model=model, condition=condition)
        for condition in CONDITION_ORDER
    }

    baseline_metrics = summary_map["baseline"]["metrics"]
    absolute_rows: List[List[str]] = []
    for label, metric_key, digits, source in ABSOLUTE_METRICS:
        row = [label]
        for condition in CONDITION_ORDER:
            if source == "summary":
                value = float(summary_map[condition]["metrics"][metric_key]["point"])
            else:
                value = float(paired_map[condition][metric_key])
            row.append(format_value(value, digits))
        absolute_rows.append(row)

    delta_rows: List[List[str]] = []
    for condition in CONDITION_ORDER[1:]:
        metrics = summary_map[condition]["metrics"]
        paired = paired_map[condition]
        delta_rows.append(
            [
                condition_registry.get_condition_spec(condition)["display_name"],
                condition_registry.tradition_label(condition) or "Generic scaffold",
                format_delta(float(metrics["task_a_accuracy"]["point"]) - float(baseline_metrics["task_a_accuracy"]["point"]), 4),
                format_delta(float(metrics["task_b_accuracy"]["point"]) - float(baseline_metrics["task_b_accuracy"]["point"]), 4),
                format_delta(float(metrics["p_reason_motive"]["point"]) - float(baseline_metrics["p_reason_motive"]["point"]), 4),
                format_delta(float(metrics["heart_sensitivity_score"]["point"]) - float(baseline_metrics["heart_sensitivity_score"]["point"]), 4),
                format_delta(float(metrics["mean_explanation_chars"]["point"]) - float(baseline_metrics["mean_explanation_chars"]["point"]), 1),
                format_value(float(metrics["same_heart_control_accuracy"]["point"]), 4),
                format_value(float(metrics["heart_overreach_rate"]["point"]), 4),
                paired_status(float(paired["task_b_order_flip_rate"]), float(paired["task_b_accuracy_gap"])),
            ]
        )

    return {
        "absolute_headers": ["Metric", *[markdown_condition_label(condition) for condition in CONDITION_ORDER]],
        "absolute_rows": absolute_rows,
        "delta_headers": [
            "Condition",
            "Tradition / frame",
            "Delta Task A",
            "Delta Task B",
            "Delta Task C",
            "Delta HSS",
            "Delta chars",
            "Same-heart",
            "Overreach",
            "Paired-order stable",
        ],
        "delta_rows": delta_rows,
        "summary_map": summary_map,
    }


def write_csv(path: str, headers: Sequence[str], rows: Sequence[Sequence[str]]) -> None:
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[str]], alignments: Sequence[str]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(alignments) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def render_markdown(tables: Dict[str, Any]) -> str:
    lines = [
        "# Complete 6-Condition Comparison Tables",
        "",
        "Full exploratory matrix for `Qwen-1.5B-Instruct` on the 63-item confirmation slice.",
        "Task A, Task B, and Task C are evaluated on all 63 items; HSS and paired-order Task B are evaluated on the 23 same-act pairs.",
        "",
        "## Table 1. Metric-by-condition matrix",
        "",
        markdown_table(
            tables["absolute_headers"],
            tables["absolute_rows"],
            ["---", "---:", "---:", "---:", "---:", "---:", "---:"],
        ),
        "",
        "## Table 2. Condition-by-delta matrix vs baseline",
        "",
        markdown_table(
            tables["delta_headers"],
            tables["delta_rows"],
            ["---", "---", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---"],
        ),
        "",
        "## Notes",
        "",
        "- Identical percentages here reflect identical discrete counts on a small slice, not a rendering bug.",
        "- Example: `Bhagavad Gita 15.15` and `Qur'an 26:88-89` both score `58/63` on Task B and `18/23` on HSS.",
        "- `heart_focused` and `Proverbs 4:23` tie at `61/63` on Task B and `21/23` on HSS.",
        "- `baseline` and `Dhammapada 34` tie at `56/63` on Task B and `16/23` on HSS.",
        "",
    ]
    return "\n".join(lines)


def render_latex(tables: Dict[str, Any]) -> str:
    absolute_header_cells = [latex_escape("Metric"), *[latex_condition_label(condition) for condition in CONDITION_ORDER]]
    absolute_body = "\n".join(
        "    " + " & ".join([latex_escape(row[0]), *row[1:]]) + r" \\"
        for row in tables["absolute_rows"]
    )
    delta_body = "\n".join(
        "    " + " & ".join(latex_escape(cell) if idx < 2 or cell == "yes" else cell for idx, cell in enumerate(row)) + r" \\"
        for row in tables["delta_rows"]
    )
    return rf"""
\begin{{table}}[H]
\centering
\small
\caption{{Exploratory six-condition metric-by-condition matrix on Qwen-1.5B-Instruct. Task A, Task B, and Task C use all 63 confirmation items; HSS and paired-order Task B use the 23 same-act pairs.}}
\label{{tab:text-anchor-matrix}}
\resizebox{{\textwidth}}{{!}}{{%
\begin{{tabular}}{{lrrrrrr}}
\toprule
{" & ".join(absolute_header_cells)} \\
\midrule
{absolute_body}
\bottomrule
\end{{tabular}}%
}}
\end{{table}}

\begin{{table}}[H]
\centering
\small
\caption{{Exploratory six-condition delta matrix relative to baseline on the same Qwen-1.5B confirmation slice.}}
\label{{tab:text-anchor-deltas}}
\resizebox{{\textwidth}}{{!}}{{%
\begin{{tabular}}{{llrrrrrrrr}}
\toprule
Condition & Tradition / frame & $\Delta$ Task A & $\Delta$ Task B & $\Delta$ Task C & $\Delta$ HSS & $\Delta$ chars & Same-heart & Overreach & Paired-order stable \\
\midrule
{delta_body}
\bottomrule
\end{{tabular}}%
}}
\vspace{{0.25em}}

\parbox{{0.97\textwidth}}{{\footnotesize
Identical percentages reflect identical discrete counts on a small slice rather than a plotting bug.
For example, Bhagavad Gita 15.15 and Qur'an 26:88--89 both score 58/63 on Task B and 18/23 on HSS.
}}
\end{{table}}
""".strip() + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--paired-order", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--output-md", required=True)
    parser.add_argument("--output-tex", required=True)
    parser.add_argument("--output-absolute-csv", required=True)
    parser.add_argument("--output-delta-csv", required=True)
    args = parser.parse_args(argv)

    summary = load_json(args.summary)
    paired_order = load_json(args.paired_order)
    tables = build_tables(summary, paired_order, args.model)

    Path(args.output_md).write_text(render_markdown(tables), encoding="utf-8")
    Path(args.output_tex).write_text(render_latex(tables), encoding="utf-8")
    write_csv(args.output_absolute_csv, tables["absolute_headers"], tables["absolute_rows"])
    write_csv(args.output_delta_csv, tables["delta_headers"], tables["delta_rows"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
