#!/usr/bin/env python3
"""Render the same-act confirmation overview as a clean two-panel argument figure."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence


WIDTH = 1440
HEIGHT = 1080

BG = "#f4f7fb"
PANEL = "#ffffff"
PANEL_STROKE = "#d6deea"
TEXT = "#16253d"
MUTED = "#617287"
LINE = "#c7d3e2"

SLATE_FILL = "#e9eef6"
SLATE_STROKE = "#c5d0e0"
TEAL = "#0f766e"
TEAL_FILL = "#dff3ee"
TEAL_STROKE = "#bee4da"
ORANGE = "#b65f1f"
ORANGE_FILL = "#fbe9db"
ORANGE_STROKE = "#f0d1b9"
AMBER = "#b45309"
AMBER_FILL = "#fff0e0"
AMBER_STROKE = "#f0d5b3"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def fmt_point(value: float) -> str:
    if value in (0.0, 1.0):
        return f"{value:.1f}"
    if abs(value) >= 100:
        return f"{value:.1f}"
    return f"{value:.4f}"


def wrap_text(text: str, max_width: int, font_size: int) -> List[str]:
    avg_char_width = max(6.0, font_size * 0.52)
    max_chars = max(10, int(max_width / avg_char_width))
    words = text.split()
    if not words:
        return [""]
    lines: List[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) <= max_chars:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def multiline_text(
    x: int,
    y: int,
    lines: Sequence[str],
    font_size: int,
    line_gap: int,
    fill: str,
    weight: int | None = None,
    anchor: str | None = None,
) -> str:
    weight_attr = f' font-weight="{weight}"' if weight is not None else ""
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ""
    tspans = []
    for idx, line in enumerate(lines):
        dy = 0 if idx == 0 else line_gap
        tspans.append(f'<tspan x="{x}" dy="{dy}">{esc(line)}</tspan>')
    return (
        f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}"{weight_attr}{anchor_attr}>'
        f'{"".join(tspans)}</text>'
    )


def rounded_rect(x: int, y: int, w: int, h: int, rx: int, fill: str, stroke: str, stroke_width: int = 1) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'
    )


def pill(
    x: int,
    y: int,
    w: int,
    h: int,
    text: str,
    fill: str,
    stroke: str,
    text_fill: str,
    font_size: int = 13,
    weight: int = 800,
) -> str:
    return (
        f'{rounded_rect(x, y, w, h, h // 2, fill, stroke)}'
        f'<text x="{x + w / 2}" y="{y + h / 2 + font_size / 2 - 2}" '
        f'font-size="{font_size}" font-weight="{weight}" fill="{text_fill}" text-anchor="middle">{esc(text)}</text>'
    )


def panel_shell(x: int, y: int, w: int, h: int, title: str, subtitle: str) -> str:
    subtitle_lines = wrap_text(subtitle, w - 56, 16)
    return (
        f'{rounded_rect(x, y, w, h, 26, PANEL, PANEL_STROKE)}'
        f'<text x="{x + 28}" y="{y + 48}" font-size="32" font-weight="800" fill="{TEXT}">{esc(title)}</text>'
        f'{multiline_text(x + 28, y + 82, subtitle_lines, 16, 20, MUTED)}'
    )


def flow_arrow(center_x: int, y1: int, y2: int) -> str:
    return (
        f'<line x1="{center_x}" y1="{y1}" x2="{center_x}" y2="{y2 - 14}" stroke="{LINE}" stroke-width="3" />'
        f'<polygon points="{center_x - 8},{y2 - 16} {center_x + 8},{y2 - 16} {center_x},{y2}" fill="{LINE}" />'
    )


def field_box(
    x: int,
    y: int,
    w: int,
    h: int,
    text: str,
    fill: str,
    stroke: str,
    text_fill: str = TEXT,
    font_size: int = 14,
) -> str:
    lines = wrap_text(text, w - 22, font_size)
    text_y = y + h / 2 - ((len(lines) - 1) * 16) / 2 + font_size / 2 - 2
    return (
        f'{rounded_rect(x, y, w, h, 16, fill, stroke)}'
        f'{multiline_text(x + 14, int(text_y), lines, font_size, 16, text_fill, 800)}'
    )


def task_box(x: int, y: int, w: int, h: int, task: str, question: str, active: bool = False) -> str:
    fill = "#f7fbfa" if active else SLATE_FILL
    stroke = TEAL if active else PANEL_STROKE
    stroke_width = 2 if active else 1
    return (
        f'{rounded_rect(x, y, w, h, 18, fill, stroke, stroke_width)}'
        f'<text x="{x + 16}" y="{y + 24}" font-size="13" font-weight="800" fill="{TEXT}">{esc(task)}</text>'
        f'{multiline_text(x + 16, y + 52, wrap_text(question, w - 24, 15), 15, 16, TEXT, 800)}'
    )


def stage_setup(x: int, y: int, w: int, h: int) -> str:
    col_a = x + 108
    col_b = x + 352
    return (
        f'{rounded_rect(x, y, w, h, 22, "#fbfdff", PANEL_STROKE)}'
        f'{pill(x + 20, y + 18, 104, 28, "1. Setup", SLATE_FILL, SLATE_STROKE, TEXT)}'
        f'<text x="{x + 144}" y="{y + 38}" font-size="24" font-weight="800" fill="{TEXT}">Same act, different motive</text>'
        f'{pill(x + w - 244, y + 52, 104, 28, "Act matched", SLATE_FILL, SLATE_STROKE, TEXT, 12)}'
        f'{pill(x + w - 128, y + 52, 108, 28, "Motive changed", TEAL_FILL, TEAL_STROKE, TEAL, 12)}'
        f'{pill(col_a, y + 88, 96, 26, "Case A", "#f4f7fb", PANEL_STROKE, MUTED, 12)}'
        f'{pill(col_b, y + 88, 96, 26, "Case B", "#f4f7fb", PANEL_STROKE, MUTED, 12)}'
        f'<text x="{x + 24}" y="{y + 132}" font-size="13" font-weight="800" fill="{MUTED}">Act</text>'
        f'{field_box(col_a, y + 110, 196, 36, "Help a classmate", SLATE_FILL, SLATE_STROKE)}'
        f'{field_box(col_b, y + 110, 196, 36, "Help a classmate", SLATE_FILL, SLATE_STROKE)}'
        f'<text x="{x + 24}" y="{y + 182}" font-size="13" font-weight="800" fill="{MUTED}">Motive</text>'
        f'{field_box(col_a, y + 160, 196, 38, "to look good", ORANGE_FILL, ORANGE_STROKE, ORANGE)}'
        f'{field_box(col_b, y + 160, 196, 38, "to care", TEAL_FILL, TEAL_STROKE, TEAL)}'
        f'{multiline_text(x + 24, y + h - 16, ["Act fixed. Motive shifts."], 15, 18, MUTED)}'
    )


def stage_tasks(x: int, y: int, w: int, h: int) -> str:
    return (
        f'{rounded_rect(x, y, w, h, 22, "#fbfdff", PANEL_STROKE)}'
        f'{pill(x + 20, y + 18, 96, 28, "2. Test", SLATE_FILL, SLATE_STROKE, TEXT)}'
        f'<text x="{x + 136}" y="{y + 38}" font-size="24" font-weight="800" fill="{TEXT}">Three tasks, distinct roles</text>'
        f'{pill(x + w - 126, y + 52, 106, 28, "B is key", TEAL_FILL, TEAL_STROKE, TEAL, 12)}'
        f'{task_box(x + 24, y + 78, 170, 74, "Task A", "overall wrong?")}'
        f'{task_box(x + 207, y + 78, 170, 74, "Task B", "worse heart?", True)}'
        f'{task_box(x + 390, y + 78, 170, 74, "Task C", "why that answer?")}'
        f'{multiline_text(x + 24, y + h - 16, ["Task B is the key test."], 15, 18, MUTED)}'
    )


def stage_guardrail(x: int, y: int, w: int, h: int) -> str:
    col_a = x + 108
    col_b = x + 352
    return (
        f'{rounded_rect(x, y, w, h, 22, "#fbfdff", PANEL_STROKE)}'
        f'{pill(x + 20, y + 18, 110, 28, "3. Guardrail", SLATE_FILL, SLATE_STROKE, TEXT)}'
        f'<text x="{x + 150}" y="{y + 38}" font-size="24" font-weight="800" fill="{TEXT}">Same-heart control</text>'
        f'{pill(x + w - 244, y + 52, 100, 28, "Act changed", SLATE_FILL, SLATE_STROKE, TEXT, 12)}'
        f'{pill(x + w - 132, y + 52, 112, 28, "Heart matched", TEAL_FILL, TEAL_STROKE, TEAL, 12)}'
        f'{pill(col_a, y + 88, 96, 26, "Case A", "#f4f7fb", PANEL_STROKE, MUTED, 12)}'
        f'{pill(col_b, y + 88, 96, 26, "Case B", "#f4f7fb", PANEL_STROKE, MUTED, 12)}'
        f'{pill(x + w - 152, y + 88, 128, 26, "Task B = Same", TEAL_FILL, TEAL_STROKE, TEAL, 12, 900)}'
        f'<text x="{x + 24}" y="{y + 132}" font-size="13" font-weight="800" fill="{MUTED}">Act</text>'
        f'{field_box(col_a, y + 110, 196, 36, "Gentle correction", SLATE_FILL, SLATE_STROKE)}'
        f'{field_box(col_b, y + 110, 196, 36, "Blunt correction", SLATE_FILL, SLATE_STROKE)}'
        f'<text x="{x + 24}" y="{y + 182}" font-size="13" font-weight="800" fill="{MUTED}">Motive</text>'
        f'{field_box(col_a, y + 160, 196, 38, "to help", TEAL_FILL, TEAL_STROKE, TEAL)}'
        f'{field_box(col_b, y + 160, 196, 38, "to help", TEAL_FILL, TEAL_STROKE, TEAL)}'
        f'{multiline_text(x + 24, y + h - 16, wrap_text("Prevents fake wins from over-reading bad hearts.", w - 48, 15), 15, 18, MUTED)}'
    )


CONDITION_LABEL = "Heart-focused"


def compare_card(
    x: int,
    y: int,
    w: int,
    h: int,
    title: str,
    baseline_value: str,
    christian_value: str,
    delta: str,
    footer: str,
) -> str:
    return (
        f'{rounded_rect(x, y, w, h, 20, PANEL, PANEL_STROKE)}'
        f'{multiline_text(x + 18, y + 30, wrap_text(title, w - 36, 18), 18, 20, TEXT, 800)}'
        f'<text x="{x + 18}" y="{y + 82}" font-size="12" font-weight="800" fill="{MUTED}">Baseline</text>'
        f'<text x="{x + 18}" y="{y + 126}" font-size="34" font-weight="900" fill="{TEXT}">{esc(baseline_value)}</text>'
        f'<text x="{x + w - 18}" y="{y + 82}" font-size="12" font-weight="800" fill="{MUTED}" text-anchor="end">{CONDITION_LABEL}</text>'
        f'<text x="{x + w - 18}" y="{y + 126}" font-size="34" font-weight="900" fill="{TEAL}" text-anchor="end">{esc(christian_value)}</text>'
        f'<line x1="{x + 98}" y1="{y + 112}" x2="{x + w - 98}" y2="{y + 112}" stroke="{LINE}" stroke-width="3" />'
        f'<polygon points="{x + w / 2 + 16},{y + 112} {x + w / 2 - 4},{y + 100} {x + w / 2 - 4},{y + 124}" fill="{LINE}" />'
        f'{pill(x + 18, y + 142, 86, 30, "Delta", SLATE_FILL, SLATE_STROKE, TEXT)}'
        f'{pill(x + 112, y + 142, 98, 30, delta, TEAL_FILL, TEAL_STROKE, TEAL, 14, 900)}'
        f'{multiline_text(x + 18, y + 188, wrap_text(footer, w - 36, 13), 13, 16, MUTED)}'
    )


def trust_card(x: int, y: int, w: int, h: int, title: str, baseline_value: str, christian_value: str, footer: str) -> str:
    return (
        f'{rounded_rect(x, y, w, h, 18, PANEL, PANEL_STROKE)}'
        f'{multiline_text(x + 16, y + 26, wrap_text(title, w - 24, 15), 15, 16, TEXT, 800)}'
        f'<text x="{x + 16}" y="{y + 66}" font-size="12" font-weight="800" fill="{MUTED}">Baseline</text>'
        f'<text x="{x + 16}" y="{y + 102}" font-size="30" font-weight="900" fill="{TEXT}">{esc(baseline_value)}</text>'
        f'<text x="{x + w - 16}" y="{y + 66}" font-size="12" font-weight="800" fill="{MUTED}" text-anchor="end">{CONDITION_LABEL}</text>'
        f'<text x="{x + w - 16}" y="{y + 102}" font-size="30" font-weight="900" fill="{TEAL}" text-anchor="end">{esc(christian_value)}</text>'
        f'{pill(x + 16, y + 114, w - 32, 28, footer, TEAL_FILL, TEAL_STROKE, TEAL, 13, 800)}'
    )


def claim_box(x: int, y: int, w: int, h: int, better: int, worse: int, tie: int, one_sided: float, two_sided: float) -> str:
    return (
        f'{rounded_rect(x, y, w, h, 22, "#fffaf3", AMBER_STROKE)}'
        f'{pill(x + 18, y + 18, 214, 32, "Directional, not yet decisive", AMBER_FILL, AMBER_STROKE, AMBER, 14, 900)}'
        f'<text x="{x + 18}" y="{y + 84}" font-size="19" font-weight="800" fill="{TEXT}">Paired test on 23 same-act motive pairs</text>'
        f'{pill(x + 18, y + 102, 106, 32, f"{better} better", TEAL_FILL, TEAL_STROKE, TEAL, 14, 900)}'
        f'{pill(x + 136, y + 102, 102, 32, f"{worse} worse", ORANGE_FILL, ORANGE_STROKE, ORANGE, 14, 900)}'
        f'{pill(x + 250, y + 102, 84, 32, f"{tie} ties", SLATE_FILL, SLATE_STROKE, TEXT, 14, 900)}'
        f'<text x="{x + 18}" y="{y + 164}" font-size="16" fill="{TEXT}">one-sided p = {one_sided:.4f}</text>'
        f'<text x="{x + 220}" y="{y + 164}" font-size="16" fill="{TEXT}">two-sided p = {two_sided:.3f}</text>'
        f'{multiline_text(x + 18, y + 194, wrap_text("Honest claim: improved inward-motive judgment with clean same-heart controls.", w - 36, 15), 15, 18, MUTED)}'
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--health", required=True)
    parser.add_argument("--robustness", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    summary = load_json(Path(args.summary))
    load_json(Path(args.health))  # kept for interface stability
    robustness = load_json(Path(args.robustness))

    by_condition = {row["condition"]: row for row in summary["summaries"]}
    baseline = by_condition["baseline"]["metrics"]
    christian = by_condition["christian_heart"]["metrics"]
    contrast = summary["contrasts"][0]["metrics"]
    same_act = next(row for row in robustness["contrasts"] if row["slice"] == "same_act_different_motive")["metrics"]

    subtitle_lines = wrap_text(
        "Current confirmation slice: a Christian heart-focused condition may reallocate moral attention toward inward motive without increasing same-heart overreach.",
        WIDTH - 112,
        22,
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">Moral attention reallocation in language models overview</title>
  <desc id="desc">Two-panel figure showing benchmark logic on the left and the confirmation result summary on the right.</desc>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}" />
  <text x="56" y="68" font-size="50" font-weight="900" fill="{TEXT}">Moral Attention Reallocation in Language Models</text>
  {multiline_text(56, 106, subtitle_lines, 22, 26, MUTED, 600)}

  {panel_shell(56, 186, 648, 842, "Benchmark Logic", "What is held fixed, what changes, and why the guardrail matters.")}
  {stage_setup(84, 286, 592, 228)}
  {flow_arrow(380, 520, 548)}
  {stage_tasks(84, 548, 592, 176)}
  {flow_arrow(380, 730, 760)}
  {stage_guardrail(84, 760, 592, 236)}

  {panel_shell(736, 186, 648, 842, "Result Summary", "Qwen-1.5B-Instruct · 63-item same-act confirmation slice.")}
  <text x="764" y="286" font-size="20" font-weight="800" fill="{TEXT}">What improved</text>
  {pill(1010, 268, 142, 28, "Task A flat", SLATE_FILL, PANEL_STROKE, MUTED, 12)}
  {compare_card(764, 306, 286, 224, "Task B: motive judgment", fmt_point(baseline["task_b_accuracy"]["point"]), fmt_point(christian["task_b_accuracy"]["point"]), f"+{contrast['task_b_accuracy']['delta']:.4f}", "63-item confirmation pack")}
  {compare_card(1070, 306, 286, 224, "Heart-sensitivity score", fmt_point(baseline["heart_sensitivity_score"]["point"]), fmt_point(christian["heart_sensitivity_score"]["point"]), f"+{contrast['heart_sensitivity_score']['delta']:.4f}", "23 same-act motive pairs")}

  <text x="764" y="596" font-size="20" font-weight="800" fill="{TEXT}">Why trust it</text>
  {trust_card(764, 616, 188, 156, "Same-heart control", fmt_point(baseline["same_heart_control_accuracy"]["point"]), fmt_point(christian["same_heart_control_accuracy"]["point"]), "accuracy stayed perfect")}
  {trust_card(976, 616, 168, 156, "Heart overreach", fmt_point(baseline["heart_overreach_rate"]["point"]), fmt_point(christian["heart_overreach_rate"]["point"]), "no increase")}
  {trust_card(1168, 616, 188, 156, "Explanation length", fmt_point(baseline["mean_explanation_chars"]["point"]), fmt_point(christian["mean_explanation_chars"]["point"]), "no verbosity jump")}

  <text x="764" y="814" font-size="20" font-weight="800" fill="{TEXT}">Honest claim</text>
  {claim_box(764, 834, 592, 188, same_act['heart_sensitivity_score']['better'], same_act['heart_sensitivity_score']['worse'], same_act['heart_sensitivity_score']['tie'], same_act['heart_sensitivity_score']['exact_sign_p_one_sided'], same_act['heart_sensitivity_score']['exact_sign_p_two_sided'])}
</svg>
"""

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(line.rstrip() for line in svg.splitlines()) + "\n", encoding="utf-8")
    print(f"Wrote confirmation SVG to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
