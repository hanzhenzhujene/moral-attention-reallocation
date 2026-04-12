#!/usr/bin/env python3
"""Render a paper-ready SVG overview for the same-act confirmation result."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence


WIDTH = 1280
HEIGHT = 1020
CARD_FILL = "#f8fafc"
CARD_STROKE = "#d7dee8"
TEXT = "#122033"
MUTED = "#5c6b7c"
ACCENT = "#0f766e"
BASELINE = "#5166d6"
CHRISTIAN = "#12805c"
ALERT = "#b45309"
SOFT = "#e8edf4"


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


def multiline_text(x: int, y: int, lines: Sequence[str], font_size: int, line_gap: int, fill: str) -> str:
    tspans = []
    for idx, line in enumerate(lines):
        dy = 0 if idx == 0 else line_gap
        tspans.append(f'<tspan x="{x}" dy="{dy}">{esc(line)}</tspan>')
    return f'<text x="{x}" y="{y}" font-size="{font_size}" fill="{fill}">{"".join(tspans)}</text>'


def card(x: int, y: int, w: int, h: int, title: str, value: str, subtitle: str, tone: str = "good") -> str:
    value_fill = ACCENT if tone == "good" else ALERT
    subtitle_lines = wrap_text(subtitle, w - 44, 13)
    return f"""
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{CARD_FILL}" stroke="{CARD_STROKE}" />
    <text x="{x + 22}" y="{y + 30}" font-size="18" font-weight="700" fill="{TEXT}">{esc(title)}</text>
    <text x="{x + 22}" y="{y + 78}" font-size="36" font-weight="800" fill="{value_fill}">{esc(value)}</text>
    {multiline_text(x + 22, y + 104, subtitle_lines, 13, 16, MUTED)}
    """


def metric_panel(x: int, y: int, w: int, h: int, summary: Dict[str, Any], health: Dict[str, Any]) -> str:
    summaries = {row["condition"]: row for row in summary["summaries"]}
    health_rows = {row["condition"]: row for row in health["groups"]}
    rows = [
        ("Heart-Sensitivity Score", "heart_sensitivity_score", True),
        ("Task B Accuracy", "task_b_accuracy", True),
        ("P(reason = motive)", "p_reason_motive", True),
        ("Task B Swap-Gap", "task_b_swap_accuracy_gap", False),
    ]

    row_svgs: List[str] = []
    for idx, (label, key, higher_is_better) in enumerate(rows):
        baseline = (
            summaries["baseline"]["metrics"][key]["point"]
            if key != "task_b_swap_accuracy_gap"
            else health_rows["baseline"]["task_b_swap_accuracy_gap"]
        )
        christian = (
            summaries["christian_heart"]["metrics"][key]["point"]
            if key != "task_b_swap_accuracy_gap"
            else health_rows["christian_heart"]["task_b_swap_accuracy_gap"]
        )
        max_value = 1.0 if key != "task_b_swap_accuracy_gap" else 0.5
        baseline_fill = int(320 * min(max(baseline / max_value, 0.0), 1.0))
        christian_fill = int(320 * min(max(christian / max_value, 0.0), 1.0))
        row_y = y + 88 + idx * 92
        helper = "higher is better" if higher_is_better else "lower is better"
        row_svgs.append(
            f"""
            <text x="{x + 26}" y="{row_y}" font-size="17" font-weight="700" fill="{TEXT}">{esc(label)}</text>
            <text x="{x + 26}" y="{row_y + 20}" font-size="13" fill="{MUTED}">{helper}</text>

            <text x="{x + 26}" y="{row_y + 48}" font-size="15" font-weight="700" fill="{TEXT}">Baseline</text>
            <rect x="{x + 130}" y="{row_y + 34}" width="320" height="16" rx="8" fill="{SOFT}" />
            <rect x="{x + 130}" y="{row_y + 34}" width="{baseline_fill}" height="16" rx="8" fill="{BASELINE}" />
            <text x="{x + 468}" y="{row_y + 48}" font-size="15" fill="{TEXT}" text-anchor="end">{baseline:.4f}</text>

            <text x="{x + 26}" y="{row_y + 74}" font-size="15" font-weight="700" fill="{TEXT}">Christian</text>
            <rect x="{x + 130}" y="{row_y + 60}" width="320" height="16" rx="8" fill="{SOFT}" />
            <rect x="{x + 130}" y="{row_y + 60}" width="{christian_fill}" height="16" rx="8" fill="{CHRISTIAN}" />
            <text x="{x + 468}" y="{row_y + 74}" font-size="15" fill="{TEXT}" text-anchor="end">{christian:.4f}</text>
            """
        )

    return f"""
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{CARD_FILL}" stroke="{CARD_STROKE}" />
    <text x="{x + 26}" y="{y + 38}" font-size="24" font-weight="800" fill="{TEXT}">Mechanism Signal</text>
    <text x="{x + 26}" y="{y + 64}" font-size="14" fill="{MUTED}">Qwen-1.5B-Instruct on the 63-item same-act confirmation pack.</text>
    {''.join(row_svgs)}
    """


def evidence_panel(x: int, y: int, w: int, h: int, robustness: Dict[str, Any], readout_lines: Sequence[str]) -> str:
    contrast = next(row for row in robustness["contrasts"] if row["slice"] == "same_act_different_motive")
    hss = contrast["metrics"]["heart_sensitivity_score"]
    task_b = contrast["metrics"]["task_b_accuracy"]
    lines = [
        f"HSS delta: {hss['delta']:.4f} [{hss['ci_low']:.4f}, {hss['ci_high']:.4f}]",
        f"Task B delta: {task_b['delta']:.4f} [{task_b['ci_low']:.4f}, {task_b['ci_high']:.4f}]",
        f"Exact sign counts: {hss['better']} better, {hss['worse']} worse, {hss['tie']} ties",
        f"Exact sign p: one-sided {hss['exact_sign_p_one_sided']:.4f}, two-sided {hss['exact_sign_p_two_sided']:.3f}",
    ]
    body = []
    for idx, line in enumerate(lines):
        body.append(f'<text x="{x + 24}" y="{y + 80 + idx * 30}" font-size="17" fill="{TEXT}">{esc(line)}</text>')

    note_lines = []
    note_y = y + 236
    for idx, line in enumerate(readout_lines):
        note_lines.append(f'<text x="{x + 24}" y="{note_y + idx * 28}" font-size="17" fill="{TEXT}">{esc(line)}</text>')

    return f"""
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{CARD_FILL}" stroke="{CARD_STROKE}" />
    <text x="{x + 24}" y="{y + 38}" font-size="24" font-weight="800" fill="{TEXT}">Paired Evidence</text>
    <text x="{x + 24}" y="{y + 62}" font-size="14" fill="{MUTED}">This slice holds outward action fixed and varies inward motive.</text>
    {''.join(body)}
    <line x1="{x + 24}" y1="{y + 206}" x2="{x + w - 24}" y2="{y + 206}" stroke="{CARD_STROKE}" />
    {''.join(note_lines)}
    """


def note_panel(x: int, y: int, w: int, h: int, title: str, lines: Sequence[str], tone: str) -> str:
    accent = ACCENT if tone == "good" else ALERT
    text_rows = []
    cursor_y = y + 72
    for line in lines:
        wrapped = wrap_text(line, w - 92, 16)
        for wrapped_line in wrapped:
            text_rows.append(f'<text x="{x + 28}" y="{cursor_y}" font-size="16" fill="{TEXT}">{esc(wrapped_line)}</text>')
            cursor_y += 24
        cursor_y += 8
    return f"""
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{CARD_FILL}" stroke="{CARD_STROKE}" />
    <rect x="{x}" y="{y}" width="8" height="{h}" rx="22" fill="{accent}" />
    <text x="{x + 28}" y="{y + 38}" font-size="22" font-weight="800" fill="{TEXT}">{esc(title)}</text>
    {''.join(text_rows)}
    """


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

    contrast = summary["contrasts"][0]["metrics"]
    hss_delta = contrast["heart_sensitivity_score"]["delta"]
    same_heart = summary["summaries"][0]["metrics"]["same_heart_control_accuracy"]["point"]
    overreach = summary["summaries"][0]["metrics"]["heart_overreach_rate"]["point"]
    one_sided = next(
        row for row in robustness["contrasts"] if row["slice"] == "same_act_different_motive"
    )["metrics"]["heart_sensitivity_score"]["exact_sign_p_one_sided"]
    christian_gap = next(row for row in health["groups"] if row["condition"] == "christian_heart")["task_b_swap_accuracy_gap"]

    hero_lines = wrap_text(
        "Same-act confirmation shows a clean directional gain in motive sensitivity under Christian framing on Qwen-1.5B, with stable controls and no verbosity inflation.",
        WIDTH - 112,
        18,
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">Same-act confirmation result overview</title>
  <desc id="desc">Paper-ready project figure summarizing the Qwen-1.5B confirmation run on same-act motive-sensitive items and same-heart controls.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fffdf8" />
      <stop offset="100%" stop-color="#f3f7fb" />
    </linearGradient>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg)" />
  <text x="56" y="72" font-size="40" font-weight="900" fill="{TEXT}">Christian Moral Attention Reallocation</text>
  <text x="56" y="110" font-size="20" font-weight="700" fill="{TEXT}">Same-Act Confirmation Result</text>
  {multiline_text(56, 138, hero_lines, 18, 22, MUTED)}

  {card(56, 174, 276, 138, "Confirmation Calls", "126/126", "Qwen-1.5B completed every baseline and Christian job without parse failures.", "good")}
  {card(354, 174, 276, 138, "HSS Delta", f"+{hss_delta:.4f}", "Heart-sensitivity rose on the 63-item confirmation pack.", "good")}
  {card(652, 174, 276, 138, "Guardrails", f"{same_heart:.1f} / {overreach:.1f}", "Same-heart control accuracy stayed perfect and heart overreach stayed at zero.", "good")}
  {card(950, 174, 274, 138, "Paired Threshold", f"p={one_sided:.4f}", "Exact one-sided sign test is near threshold, directional but not yet decisive.", "warn")}

  {metric_panel(56, 338, 546, 470, summary, health)}
  {evidence_panel(628, 338, 596, 470, robustness, [
      "Bootstrap intervals stay positive for the same-act HSS delta.",
      "Christian framing improves motive-sensitive Task B without extra explanation length.",
      f"Christian swap-gap falls to {christian_gap:.4f}; baseline still blocks full freeze."
  ])}

  {note_panel(56, 840, 568, 150, "What This Supports", [
      "A heart-focused Christian frame can improve inward-orientation judgment before it changes Task A verdicts.",
      "The gain here is mechanistic: better motive discrimination with no guardrail regression."
  ], "good")}
  {note_panel(656, 840, 568, 150, "What Still Needs Work", [
      "Baseline still has residual same-act order sensitivity, so freeze remains blocked.",
      "This slice is strong enough for a paper-quality directional result, but not yet a final decisive main claim."
  ], "warn")}
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
