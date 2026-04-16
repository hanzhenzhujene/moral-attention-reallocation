#!/usr/bin/env python3
"""Render a compact publication-style metric scoreboard for the public confirmation slice."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence


WIDTH = 1400
HEIGHT = 940

BG = "#f4f7fb"
PANEL = "#ffffff"
PANEL_STROKE = "#d6deea"
TEXT = "#16253d"
MUTED = "#617287"
LINE = "#d8e0ea"

SLATE_FILL = "#e9eef6"
SLATE_STROKE = "#c5d0e0"
TEAL = "#0f766e"
TEAL_FILL = "#dff3ee"
TEAL_STROKE = "#bee4da"
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


def fmt(value: float) -> str:
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
    return f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}"{weight_attr}>{"".join(tspans)}</text>'


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


def metric_card(
    x: int,
    y: int,
    w: int,
    h: int,
    title: str,
    baseline_value: str,
    focused_value: str,
    delta: str,
    footer: str,
    tone: str = "default",
) -> str:
    delta_fill = TEAL_FILL if tone != "flat" else SLATE_FILL
    delta_stroke = TEAL_STROKE if tone != "flat" else SLATE_STROKE
    delta_text = TEAL if tone != "flat" else TEXT
    return (
        f'{rounded_rect(x, y, w, h, 22, PANEL, PANEL_STROKE)}'
        f'{multiline_text(x + 18, y + 30, wrap_text(title, w - 36, 18), 18, 20, TEXT, 800)}'
        f'<text x="{x + 18}" y="{y + 82}" font-size="12" font-weight="800" fill="{MUTED}">Baseline</text>'
        f'<text x="{x + 18}" y="{y + 126}" font-size="34" font-weight="900" fill="{TEXT}">{esc(baseline_value)}</text>'
        f'<text x="{x + w - 18}" y="{y + 82}" font-size="12" font-weight="800" fill="{MUTED}" text-anchor="end">Heart-focused</text>'
        f'<text x="{x + w - 18}" y="{y + 126}" font-size="34" font-weight="900" fill="{TEAL}" text-anchor="end">{esc(focused_value)}</text>'
        f'<line x1="{x + 98}" y1="{y + 112}" x2="{x + w - 98}" y2="{y + 112}" stroke="{LINE}" stroke-width="3" />'
        f'<polygon points="{x + w / 2 + 18},{y + 112} {x + w / 2 - 4},{y + 100} {x + w / 2 - 4},{y + 124}" fill="{LINE}" />'
        f'{pill(x + 18, y + 142, 86, 30, "Delta", SLATE_FILL, SLATE_STROKE, TEXT)}'
        f'{pill(x + 112, y + 142, 104, 30, delta, delta_fill, delta_stroke, delta_text, 14, 900)}'
        f'{multiline_text(x + 18, y + 188, wrap_text(footer, w - 36, 13), 13, 16, MUTED)}'
    )


def footer_box(x: int, y: int, w: int, h: int, title: str, lines: Sequence[str]) -> str:
    text_chunks = []
    for idx, line in enumerate(lines):
        text_chunks.append(
            f'<text x="{x + 22}" y="{y + 74 + idx * 28}" font-size="18" fill="{TEXT}">{esc(line)}</text>'
        )
    return (
        f'{rounded_rect(x, y, w, h, 22, "#fffaf3", AMBER_STROKE)}'
        f'{pill(x + 20, y + 18, 210, 32, title, AMBER_FILL, AMBER_STROKE, AMBER, 14, 900)}'
        f'{"".join(text_chunks)}'
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    summary = load_json(Path(args.summary))
    by_condition = {row["condition"]: row["metrics"] for row in summary["summaries"]}
    contrast = summary["contrasts"][0]["metrics"]
    baseline = by_condition["baseline"]
    focused = by_condition["christian_heart"]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">Confirmation metric scoreboard</title>
  <desc id="desc">Publication-style metric scoreboard comparing baseline and Christian heart-focused framing on the Qwen-1.5B confirmation slice.</desc>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}" />
  <text x="54" y="70" font-size="46" font-weight="900" fill="{TEXT}">Confirmation Metrics At A Glance</text>
  <text x="54" y="108" font-size="22" fill="{MUTED}" font-weight="600">Qwen-1.5B-Instruct · 63-item same-act confirmation slice · baseline vs Christian heart-focused</text>
  {pill(1048, 78, 278, 30, "Public artifact: directional, not definitive", AMBER_FILL, AMBER_STROKE, AMBER, 13, 900)}

  {metric_card(54, 160, 412, 238, "Task A accuracy", fmt(baseline["task_a_accuracy"]["point"]), fmt(focused["task_a_accuracy"]["point"]), f"{contrast['task_a_accuracy']['delta']:+.4f}", "Top-line verdict stayed flat.", "flat")}
  {metric_card(494, 160, 412, 238, "Task B accuracy", fmt(baseline["task_b_accuracy"]["point"]), fmt(focused["task_b_accuracy"]["point"]), f"{contrast['task_b_accuracy']['delta']:+.4f}", "Inward-orientation judgment improved.")} 
  {metric_card(934, 160, 412, 238, "Heart-sensitivity score", fmt(baseline["heart_sensitivity_score"]["point"]), fmt(focused["heart_sensitivity_score"]["point"]), f"{contrast['heart_sensitivity_score']['delta']:+.4f}", "Core motive-sensitive signal moved in the expected direction.")}

  {metric_card(54, 430, 412, 238, "P(reason = motive)", fmt(baseline["p_reason_motive"]["point"]), fmt(focused["p_reason_motive"]["point"]), f"{contrast['p_reason_motive']['delta']:+.4f}", "Reason focus shifted toward motive.")} 
  {metric_card(494, 430, 412, 238, "Same-heart control accuracy", fmt(baseline["same_heart_control_accuracy"]["point"]), fmt(focused["same_heart_control_accuracy"]["point"]), f"{contrast['same_heart_control_accuracy']['delta']:+.1f}", "Guardrail stayed perfect.", "flat")}
  {metric_card(934, 430, 412, 238, "Heart overreach rate", fmt(baseline["heart_overreach_rate"]["point"]), fmt(focused["heart_overreach_rate"]["point"]), f"{contrast['heart_overreach_rate']['delta']:+.1f}", "No false projection of worse hearts.", "flat")}

  {footer_box(54, 716, 600, 168, "What this supports", ["Motive-sensitive judgment improved on the public slice.", "The gain was not accompanied by same-heart degradation.", "Explanation length also stayed stable."])}
  {footer_box(692, 716, 654, 168, "What this does not yet prove", ["This is still a pre-freeze confirmation artifact.", "The paired sign test is directional rather than fully decisive.", "The full 160-item main benchmark is not frozen yet."])}
</svg>
"""

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(line.rstrip() for line in svg.splitlines()) + "\n", encoding="utf-8")
    print(f"Wrote confirmation scoreboard to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
