#!/usr/bin/env python3
"""Render the main same-act confirmation overview as a 2-panel argument figure."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence


WIDTH = 1440
HEIGHT = 1060

BG = "#f4f7fb"
PANEL = "#ffffff"
PANEL_STROKE = "#d6deea"
TEXT = "#15253d"
MUTED = "#617287"
BASELINE = "#6b7280"
BASELINE_SOFT = "#e6ebf2"
CHRISTIAN = "#0f766e"
CHRISTIAN_SOFT = "#d7f2ec"
WARN = "#b45309"
WARN_SOFT = "#fff0e0"
ACT = "#dfe7f4"
ACT_STROKE = "#b9c6dd"
TASK = "#edf2f8"
CONTROL = "#d9eef6"
CONTROL_STROKE = "#99c8da"
GOOD = "#1f8a70"
BAD = "#c26a2d"
LINE = "#c4d0df"


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
) -> str:
    weight_attr = f' font-weight="{weight}"' if weight is not None else ""
    tspans = []
    for idx, line in enumerate(lines):
        dy = 0 if idx == 0 else line_gap
        tspans.append(f'<tspan x="{x}" dy="{dy}">{esc(line)}</tspan>')
    return (
        f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}"{weight_attr}>'
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
    font_size: int = 14,
    weight: int = 700,
) -> str:
    return (
        f'{rounded_rect(x, y, w, h, h // 2, fill, stroke)}'
        f'<text x="{x + w / 2}" y="{y + h / 2 + font_size / 2 - 2}" '
        f'font-size="{font_size}" font-weight="{weight}" fill="{text_fill}" text-anchor="middle">{esc(text)}</text>'
    )


def panel_shell(x: int, y: int, w: int, h: int, title: str, subtitle: str) -> str:
    subtitle_lines = wrap_text(subtitle, w - 56, 16)
    return (
        f'{rounded_rect(x, y, w, h, 26, PANEL, PANEL_STROKE, 1)}'
        f'<text x="{x + 28}" y="{y + 44}" font-size="30" font-weight="800" fill="{TEXT}">{esc(title)}</text>'
        f'{multiline_text(x + 28, y + 74, subtitle_lines, 16, 20, MUTED)}'
    )


def stage_block(x: int, y: int, w: int, h: int, step: str, title: str, note: str, inner_svg: str) -> str:
    note_lines = wrap_text(note, w - 48, 15)
    return (
        f'{rounded_rect(x, y, w, h, 22, "#fbfdff", PANEL_STROKE, 1)}'
        f'{pill(x + 20, y + 18, 112, 28, step, "#eef4fb", ACT_STROKE, TEXT, 13, 800)}'
        f'<text x="{x + 148}" y="{y + 38}" font-size="24" font-weight="800" fill="{TEXT}">{esc(title)}</text>'
        f'{inner_svg}'
        f'{multiline_text(x + 24, y + h - 10, note_lines, 15, 18, MUTED)}'
    )


def flow_arrow(center_x: int, y1: int, y2: int) -> str:
    return (
        f'<line x1="{center_x}" y1="{y1}" x2="{center_x}" y2="{y2 - 14}" stroke="{LINE}" stroke-width="3" />'
        f'<polygon points="{center_x - 8},{y2 - 16} {center_x + 8},{y2 - 16} {center_x},{y2}" fill="{LINE}" />'
    )


def case_card(
    x: int,
    y: int,
    w: int,
    h: int,
    act_text: str,
    motive_text: str,
    motive_fill: str,
    motive_stroke: str,
    motive_text_fill: str,
) -> str:
    act_lines = wrap_text(act_text, w - 36, 14)
    motive_lines = wrap_text(motive_text, w - 36, 14)
    body = [
        rounded_rect(x, y, w, h, 18, PANEL, PANEL_STROKE, 1),
        rounded_rect(x + 14, y + 14, w - 28, 26, 13, ACT, ACT_STROKE, 1),
        multiline_text(x + 26, y + 33, act_lines, 14, 16, TEXT, 700),
        '<text x="{}" y="{}" font-size="12" font-weight="700" fill="{}">Motive</text>'.format(
            x + 16, y + 56, MUTED
        ),
        rounded_rect(x + 14, y + 62, w - 28, 30, 15, motive_fill, motive_stroke, 1),
        multiline_text(x + 26, y + 82, motive_lines, 14, 16, motive_text_fill, 700),
    ]
    return "".join(body)


def task_card(x: int, y: int, w: int, h: int, task: str, label: str, prompt: str, highlight: bool = False) -> str:
    stroke = CHRISTIAN if highlight else PANEL_STROKE
    fill = "#f7fbfa" if highlight else TASK
    label_lines = wrap_text(label, w - 24, 16)
    prompt_lines = wrap_text(prompt, w - 24, 13)
    return (
        f'{rounded_rect(x, y, w, h, 18, fill, stroke, 2 if highlight else 1)}'
        f'<text x="{x + 16}" y="{y + 24}" font-size="13" font-weight="800" fill="{TEXT}">{esc(task)}</text>'
        f'{multiline_text(x + 16, y + 50, label_lines, 16, 18, TEXT, 800)}'
        f'{multiline_text(x + 16, y + 82, prompt_lines, 13, 16, MUTED)}'
    )


def compare_card(
    x: int,
    y: int,
    w: int,
    h: int,
    title: str,
    left_label: str,
    left_value: str,
    right_label: str,
    right_value: str,
    delta_label: str,
    delta_value: str,
    delta_fill: str,
    delta_text_fill: str,
    footer: str,
) -> str:
    title_lines = wrap_text(title, w - 36, 18)
    footer_lines = wrap_text(footer, w - 36, 13)
    return (
        f'{rounded_rect(x, y, w, h, 20, PANEL, PANEL_STROKE, 1)}'
        f'{multiline_text(x + 18, y + 28, title_lines, 18, 20, TEXT, 800)}'
        f'<text x="{x + 20}" y="{y + 78}" font-size="12" font-weight="700" fill="{MUTED}">{esc(left_label)}</text>'
        f'<text x="{x + 20}" y="{y + 122}" font-size="34" font-weight="900" fill="{TEXT}">{esc(left_value)}</text>'
        f'<text x="{x + w - 18}" y="{y + 78}" font-size="12" font-weight="700" fill="{MUTED}" text-anchor="end">{esc(right_label)}</text>'
        f'<text x="{x + w - 18}" y="{y + 122}" font-size="34" font-weight="900" fill="{CHRISTIAN}" text-anchor="end">{esc(right_value)}</text>'
        f'<line x1="{x + 90}" y1="{y + 108}" x2="{x + w - 90}" y2="{y + 108}" stroke="{LINE}" stroke-width="3" />'
        f'<polygon points="{x + w / 2 + 16},{y + 108} {x + w / 2 - 4},{y + 96} {x + w / 2 - 4},{y + 120}" fill="{LINE}" />'
        f'{pill(x + 18, y + 142, 110, 30, delta_label, "#eef4fb", ACT_STROKE, TEXT, 13, 800)}'
        f'{pill(x + 136, y + 142, 96, 30, delta_value, delta_fill, delta_fill, delta_text_fill, 14, 900)}'
        f'{multiline_text(x + 18, y + 188, footer_lines, 13, 16, MUTED)}'
    )


def trust_card(
    x: int,
    y: int,
    w: int,
    h: int,
    title: str,
    baseline_value: str,
    christian_value: str,
    footer: str,
    tone: str,
) -> str:
    title_lines = wrap_text(title, w - 24, 15)
    accent_fill = CHRISTIAN_SOFT if tone == "good" else WARN_SOFT
    accent_text = CHRISTIAN if tone == "good" else WARN
    footer_lines = wrap_text(footer, w - 24, 13)
    return (
        f'{rounded_rect(x, y, w, h, 18, PANEL, PANEL_STROKE, 1)}'
        f'{multiline_text(x + 16, y + 26, title_lines, 15, 16, TEXT, 800)}'
        f'<text x="{x + 16}" y="{y + 64}" font-size="12" font-weight="700" fill="{MUTED}">Baseline</text>'
        f'<text x="{x + 16}" y="{y + 100}" font-size="30" font-weight="900" fill="{TEXT}">{esc(baseline_value)}</text>'
        f'<text x="{x + w - 16}" y="{y + 64}" font-size="12" font-weight="700" fill="{MUTED}" text-anchor="end">Christian</text>'
        f'<text x="{x + w - 16}" y="{y + 100}" font-size="30" font-weight="900" fill="{CHRISTIAN}" text-anchor="end">{esc(christian_value)}</text>'
        f'{pill(x + 16, y + 112, w - 32, 28, footer, accent_fill, accent_fill, accent_text, 13, 800)}'
    )


def honest_claim_card(
    x: int,
    y: int,
    w: int,
    h: int,
    better: int,
    worse: int,
    tie: int,
    one_sided_p: float,
    two_sided_p: float,
) -> str:
    return (
        f'{rounded_rect(x, y, w, h, 20, "#fffaf3", "#f0d5b3", 1)}'
        f'{pill(x + 18, y + 18, 214, 32, "Directional, not yet decisive", WARN_SOFT, "#f0d5b3", WARN, 14, 900)}'
        f'<text x="{x + 18}" y="{y + 82}" font-size="18" font-weight="800" fill="{TEXT}">Paired test on 23 same-act motive pairs</text>'
        f'{pill(x + 18, y + 102, 106, 32, f"{better} better", "#eef8f3", "#d3ebdf", CHRISTIAN, 14, 900)}'
        f'{pill(x + 136, y + 102, 102, 32, f"{worse} worse", "#fbf1ea", "#efd6bf", BAD, 14, 900)}'
        f'{pill(x + 250, y + 102, 84, 32, f"{tie} ties", "#eef3f8", "#d6deea", TEXT, 14, 900)}'
        f'<text x="{x + 18}" y="{y + 166}" font-size="16" fill="{TEXT}">one-sided p = {one_sided_p:.4f}</text>'
        f'<text x="{x + 220}" y="{y + 166}" font-size="16" fill="{TEXT}">two-sided p = {two_sided_p:.3f}</text>'
        f'<text x="{x + 18}" y="{y + 196}" font-size="15" fill="{MUTED}">Honest claim: improved inward-motive judgment with clean same-heart controls.</text>'
    )


def section_title(x: int, y: int, title: str, badge: str | None = None) -> str:
    badge_svg = ""
    if badge:
        badge_svg = pill(x + 246, y - 18, 142, 28, badge, "#eef3f8", PANEL_STROKE, MUTED, 12, 800)
    return f'<text x="{x}" y="{y}" font-size="20" font-weight="800" fill="{TEXT}">{esc(title)}</text>{badge_svg}'


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--health", required=True)
    parser.add_argument("--robustness", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    summary = load_json(Path(args.summary))
    health = load_json(Path(args.health))
    robustness = load_json(Path(args.robustness))

    summary_by_condition = {row["condition"]: row for row in summary["summaries"]}
    health_by_condition = {row["condition"]: row for row in health["groups"]}
    contrast = summary["contrasts"][0]["metrics"]
    same_act_contrast = next(row for row in robustness["contrasts"] if row["slice"] == "same_act_different_motive")
    same_act_metrics = same_act_contrast["metrics"]

    baseline = summary_by_condition["baseline"]["metrics"]
    christian = summary_by_condition["christian_heart"]["metrics"]

    task_b_delta = contrast["task_b_accuracy"]["delta"]
    hss_delta = contrast["heart_sensitivity_score"]["delta"]
    same_heart = baseline["same_heart_control_accuracy"]["point"]
    overreach = baseline["heart_overreach_rate"]["point"]
    expl_baseline = baseline["mean_explanation_chars"]["point"]
    expl_christian = christian["mean_explanation_chars"]["point"]

    title_lines = wrap_text(
        "Christian heart-focused framing may reallocate moral attention toward inward motive on a clean same-act confirmation slice, without increasing same-heart overreach.",
        WIDTH - 112,
        22,
    )

    left_panel = [
        panel_shell(
            56,
            178,
            648,
            828,
            "Benchmark Logic",
            "What is held fixed, what changes, and why the guardrail matters.",
        ),
        stage_block(
            84,
            260,
            592,
            198,
            "1. Setup",
            "Same act, different motive",
            "Hold the act fixed; vary the motive.",
            (
                f'{pill(108, 306, 102, 28, "Same act", "#eef3f8", ACT_STROKE, TEXT, 13, 800)}'
                f'{pill(220, 306, 128, 28, "Different motive", "#eef8f3", "#d3ebdf", CHRISTIAN, 13, 800)}'
                f'{case_card(108, 330, 220, 102, "Help a classmate", "to look good", "#fff1e7", "#f0d5b3", BAD)}'
                f'{case_card(348, 330, 220, 102, "Help a classmate", "to care", "#e6f5ef", "#cbe8dc", CHRISTIAN)}'
            ),
        ),
        flow_arrow(380, 460, 486),
        stage_block(
            84,
            486,
            592,
            166,
            "2. Test",
            "Three tasks, distinct roles",
            "Separate verdict, motive, and reason focus.",
            (
                f'{task_card(108, 528, 168, 90, "Task A", "act judgment", "overall wrong?")}'
                f'{task_card(296, 528, 168, 90, "Task B", "motive judgment", "worse heart?", True)}'
                f'{task_card(484, 528, 168, 90, "Task C", "reason focus", "why that answer?")}'
            ),
        ),
        flow_arrow(380, 654, 680),
        stage_block(
            84,
            680,
            592,
            240,
            "3. Guardrail",
            "Same-heart control",
            "A real gain keeps Task B = Same here.",
            (
                f'{pill(108, 726, 150, 28, "Same-heart control", "#e9f5f9", CONTROL_STROKE, TEXT, 13, 800)}'
                f'{pill(268, 726, 128, 28, "Different surface", "#eef3f8", ACT_STROKE, TEXT, 13, 800)}'
                f'{case_card(108, 770, 220, 102, "Gentle correction", "to help", "#e6f5ef", "#cbe8dc", CHRISTIAN)}'
                f'{case_card(348, 770, 220, 102, "Blunt correction", "to help", "#e6f5ef", "#cbe8dc", CHRISTIAN)}'
                f'{pill(420, 726, 132, 28, "Task B = Same", CHRISTIAN_SOFT, "#cbe8dc", CHRISTIAN, 13, 900)}'
                f'{pill(420, 890, 116, 28, "No fake win", "#eef8f3", "#d3ebdf", CHRISTIAN, 13, 900)}'
            ),
        ),
    ]

    right_panel = [
        panel_shell(
            736,
            178,
            648,
            828,
            "Result Summary",
            "Qwen-1.5B-Instruct · 63-item same-act confirmation slice.",
        ),
        section_title(764, 272, "What improved", "Task A flat"),
        compare_card(
            764,
            292,
            286,
            214,
            "Task B: motive judgment",
            "Baseline",
            fmt_point(baseline["task_b_accuracy"]["point"]),
            "Christian",
            fmt_point(christian["task_b_accuracy"]["point"]),
            "Delta",
            f"+{task_b_delta:.4f}",
            "#e6f5ef",
            CHRISTIAN,
            "63-item confirmation pack",
        ),
        compare_card(
            1062,
            292,
            294,
            214,
            "Heart-sensitivity score",
            "Baseline",
            fmt_point(baseline["heart_sensitivity_score"]["point"]),
            "Christian",
            fmt_point(christian["heart_sensitivity_score"]["point"]),
            "Delta",
            f"+{hss_delta:.4f}",
            "#e6f5ef",
            CHRISTIAN,
            "23 same-act motive pairs",
        ),
        section_title(764, 570, "Why trust it"),
        trust_card(
            764,
            590,
            188,
            150,
            "Same-heart control",
            fmt_point(same_heart),
            fmt_point(christian["same_heart_control_accuracy"]["point"]),
            "accuracy stayed perfect",
            "good",
        ),
        trust_card(
            976,
            590,
            168,
            150,
            "Heart overreach",
            fmt_point(overreach),
            fmt_point(christian["heart_overreach_rate"]["point"]),
            "no increase",
            "good",
        ),
        trust_card(
            1168,
            590,
            188,
            150,
            "Explanation length",
            fmt_point(expl_baseline),
            fmt_point(expl_christian),
            "no verbosity jump",
            "good",
        ),
        section_title(764, 786, "Honest claim"),
        honest_claim_card(
            764,
            806,
            592,
            176,
            same_act_metrics["heart_sensitivity_score"]["better"],
            same_act_metrics["heart_sensitivity_score"]["worse"],
            same_act_metrics["heart_sensitivity_score"]["tie"],
            same_act_metrics["heart_sensitivity_score"]["exact_sign_p_one_sided"],
            same_act_metrics["heart_sensitivity_score"]["exact_sign_p_two_sided"],
        ),
    ]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">Christian moral attention reallocation overview</title>
  <desc id="desc">Two-panel paper-ready figure showing benchmark logic on the left and the same-act confirmation result summary on the right.</desc>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}" />
  <text x="56" y="68" font-size="48" font-weight="900" fill="{TEXT}">Christian Moral Attention Reallocation</text>
  {multiline_text(56, 106, title_lines, 22, 26, MUTED, 600)}
  {''.join(left_panel)}
  {''.join(right_panel)}
</svg>
"""

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cleaned_svg = "\n".join(line.rstrip() for line in svg.splitlines()) + "\n"
    output_path.write_text(cleaned_svg, encoding="utf-8")
    print(f"Wrote confirmation SVG to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
