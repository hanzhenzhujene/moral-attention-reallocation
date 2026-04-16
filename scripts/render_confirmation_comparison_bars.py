#!/usr/bin/env python3
"""Render a paper-ready comparison chart for the public confirmation slice."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


BG = "#f7f9fc"
BASELINE = "#7c8ea5"
FOCUSED = "#117a72"
GRID = "#d7dfeb"
TEXT = "#18263d"
MUTED = "#5f7086"
HILITE = "#edf7f4"
BOX = "#fffaf3"
BOX_EDGE = "#efd8b7"
BOX_TEXT = "#9a4b10"


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def metric_triplet(metrics: Dict[str, Any], key: str) -> Tuple[float, float, float]:
    row = metrics[key]
    point = row["point"]
    low = row["ci_low"] if row["ci_low"] is not None else point
    high = row["ci_high"] if row["ci_high"] is not None else point
    return point, low, high


def fmt(value: float) -> str:
    if value in (0.0, 1.0):
        return f"{value:.1f}"
    if abs(value) >= 100:
        return f"{value:.1f}"
    return f"{value:.4f}"


def make_err(values: Iterable[Tuple[float, float, float]]) -> np.ndarray:
    lower = []
    upper = []
    for point, low, high in values:
        lower.append(max(0.0, point - low))
        upper.append(max(0.0, high - point))
    return np.array([lower, upper])


def label_bars(ax: plt.Axes, bars, values: Iterable[float], color: str) -> None:
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 0.03,
            fmt(value),
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
            color=color,
        )


def add_box(ax: plt.Axes, x: float, y: float, w: float, h: float, title: str, lines: Iterable[str]) -> None:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        linewidth=1.2,
        edgecolor=BOX_EDGE,
        facecolor=BOX,
        transform=ax.transAxes,
    )
    ax.add_patch(patch)
    ax.text(
        x + 0.03,
        y + h - 0.16,
        title,
        transform=ax.transAxes,
        fontsize=11,
        fontweight="bold",
        color=BOX_TEXT,
        va="top",
    )
    for idx, line in enumerate(lines):
        ax.text(
            x + 0.03,
            y + h - 0.33 - idx * 0.18,
            line,
            transform=ax.transAxes,
            fontsize=10.5,
            color=TEXT,
            va="top",
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True, help="Path to confirmation_summary.json")
    parser.add_argument("--robustness", required=True, help="Path to confirmation_robustness.json")
    parser.add_argument("--output", required=True, help="Output path (.png, .svg, or .pdf)")
    args = parser.parse_args()

    summary = load_json(Path(args.summary))
    robustness = load_json(Path(args.robustness))

    by_condition = {row["condition"]: row["metrics"] for row in summary["summaries"]}
    baseline = by_condition["baseline"]
    focused = by_condition["christian_heart"]

    all_contrast = summary["contrasts"][0]["metrics"]
    same_act_contrast = next(
        row for row in robustness["contrasts"] if row["slice"] == "same_act_different_motive"
    )["metrics"]

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titleweight": "bold",
            "axes.edgecolor": GRID,
            "axes.labelcolor": TEXT,
            "xtick.color": TEXT,
            "ytick.color": MUTED,
        }
    )

    fig = plt.figure(figsize=(13.6, 8.2), facecolor=BG)
    gs = fig.add_gridspec(2, 2, height_ratios=[4.4, 1.8], width_ratios=[2.45, 1.55], hspace=0.28, wspace=0.16)
    ax_main = fig.add_subplot(gs[0, 0], facecolor="white")
    ax_guard = fig.add_subplot(gs[0, 1], facecolor="white")
    ax_note = fig.add_subplot(gs[1, :], facecolor=BG)

    for ax in (ax_main, ax_guard):
        ax.set_ylim(0.0, 1.08)
        ax.set_yticks(np.linspace(0.0, 1.0, 6))
        ax.grid(axis="y", color=GRID, linewidth=1, alpha=0.9)
        ax.set_axisbelow(True)
        ax.spines["left"].set_color(GRID)
        ax.spines["bottom"].set_color(GRID)

    main_specs = [
        ("Task A\noverall verdict", "task_a_accuracy"),
        ("Task B\nmotive judgment", "task_b_accuracy"),
        ("Heart-\nsensitivity", "heart_sensitivity_score"),
        ("Task C\nreason = motive", "p_reason_motive"),
    ]
    guard_specs = [
        ("Same-heart\ncontrol", "same_heart_control_accuracy"),
        ("Heart overreach\n(lower better)", "heart_overreach_rate"),
    ]

    x_main = np.arange(len(main_specs))
    x_guard = np.arange(len(guard_specs))
    width = 0.34

    ax_main.axvspan(0.55, 2.45, color=HILITE, zorder=0)
    ax_main.text(
        1.5,
        1.045,
        "main signal",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        color=FOCUSED,
        bbox=dict(boxstyle="round,pad=0.3,rounding_size=0.6", facecolor="#dff3ee", edgecolor="#c3e4db"),
    )

    baseline_main = [metric_triplet(baseline, key) for _, key in main_specs]
    focused_main = [metric_triplet(focused, key) for _, key in main_specs]
    baseline_guard = [metric_triplet(baseline, key) for _, key in guard_specs]
    focused_guard = [metric_triplet(focused, key) for _, key in guard_specs]

    bars_base_main = ax_main.bar(
        x_main - width / 2,
        [point for point, _, _ in baseline_main],
        width,
        color=BASELINE,
        label="Baseline",
        yerr=make_err(baseline_main),
        capsize=3,
        ecolor="#65778c",
        linewidth=0,
    )
    bars_focus_main = ax_main.bar(
        x_main + width / 2,
        [point for point, _, _ in focused_main],
        width,
        color=FOCUSED,
        label="Christian heart-focused",
        yerr=make_err(focused_main),
        capsize=3,
        ecolor="#0a5d57",
        linewidth=0,
    )
    ax_main.set_xticks(x_main)
    ax_main.set_xticklabels([label for label, _ in main_specs], fontsize=11)
    ax_main.set_title("Primary outcomes", fontsize=16, loc="left", pad=12, color=TEXT)
    ax_main.set_ylabel("Score", fontsize=11)

    bars_base_guard = ax_guard.bar(
        x_guard - width / 2,
        [point for point, _, _ in baseline_guard],
        width,
        color=BASELINE,
        yerr=make_err(baseline_guard),
        capsize=3,
        ecolor="#65778c",
        linewidth=0,
    )
    bars_focus_guard = ax_guard.bar(
        x_guard + width / 2,
        [point for point, _, _ in focused_guard],
        width,
        color=FOCUSED,
        yerr=make_err(focused_guard),
        capsize=3,
        ecolor="#0a5d57",
        linewidth=0,
    )
    ax_guard.set_xticks(x_guard)
    ax_guard.set_xticklabels([label for label, _ in guard_specs], fontsize=11)
    ax_guard.set_title("Guardrails", fontsize=16, loc="left", pad=12, color=TEXT)

    label_bars(ax_main, bars_base_main, [point for point, _, _ in baseline_main], TEXT)
    label_bars(ax_main, bars_focus_main, [point for point, _, _ in focused_main], FOCUSED)
    label_bars(ax_guard, bars_base_guard, [point for point, _, _ in baseline_guard], TEXT)
    label_bars(ax_guard, bars_focus_guard, [point for point, _, _ in focused_guard], FOCUSED)

    for xpos, delta_key in zip(x_main, [key for _, key in main_specs]):
        delta = all_contrast[delta_key]["delta"]
        ax_main.text(
            xpos,
            -0.15,
            f"Delta {delta:+.4f}",
            ha="center",
            va="top",
            fontsize=10,
            color=MUTED,
            transform=ax_main.get_xaxis_transform(),
        )
    for xpos, delta_key in zip(x_guard, [key for _, key in guard_specs]):
        delta = all_contrast[delta_key]["delta"]
        ax_guard.text(
            xpos,
            -0.15,
            f"Delta {delta:+.1f}",
            ha="center",
            va="top",
            fontsize=10,
            color=MUTED,
            transform=ax_guard.get_xaxis_transform(),
        )

    fig.suptitle(
        "Public confirmation slice",
        fontsize=21,
        fontweight="bold",
        x=0.055,
        y=0.975,
        ha="left",
        color=TEXT,
    )
    fig.text(
        0.055,
        0.935,
        "Baseline vs Christian heart-focused framing | Qwen-1.5B-Instruct | 63 items total (23 same-act motive pairs + 40 same-heart controls) | error bars show bootstrap 95% CIs",
        fontsize=11.5,
        color=MUTED,
    )
    fig.legend(
        handles=[bars_base_main, bars_focus_main],
        labels=["Baseline", "Christian heart-focused"],
        loc="upper right",
        bbox_to_anchor=(0.975, 0.985),
        ncol=2,
        frameon=False,
        fontsize=10.5,
        handlelength=1.8,
        columnspacing=1.4,
    )

    ax_note.axis("off")
    add_box(
        ax_note,
        0.02,
        0.10,
        0.44,
        0.78,
        "What changed",
        [
            f"Task B accuracy: {fmt(baseline['task_b_accuracy']['point'])} -> {fmt(focused['task_b_accuracy']['point'])}",
            f"Heart-sensitivity: {fmt(baseline['heart_sensitivity_score']['point'])} -> {fmt(focused['heart_sensitivity_score']['point'])}",
            f"Task A stays flat: {fmt(baseline['task_a_accuracy']['point'])} -> {fmt(focused['task_a_accuracy']['point'])}",
            f"Task C reason=motive: {fmt(baseline['p_reason_motive']['point'])} -> {fmt(focused['p_reason_motive']['point'])}",
        ],
    )
    add_box(
        ax_note,
        0.52,
        0.10,
        0.46,
        0.78,
        "Why trust it",
        [
            f"Same-heart control: {fmt(baseline['same_heart_control_accuracy']['point'])} -> {fmt(focused['same_heart_control_accuracy']['point'])}",
            f"Heart overreach: {fmt(baseline['heart_overreach_rate']['point'])} -> {fmt(focused['heart_overreach_rate']['point'])}",
            f"Explanation length: {fmt(baseline['mean_explanation_chars']['point'])} -> {fmt(focused['mean_explanation_chars']['point'])}",
            "Same-act sign test: 4 better, 0 worse, 19 ties; p(one-sided) = "
            f"{same_act_contrast['heart_sensitivity_score']['exact_sign_p_one_sided']:.4f}",
        ],
    )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"bbox_inches": "tight", "facecolor": BG}
    if output.suffix.lower() == ".png":
        save_kwargs["dpi"] = 220
    fig.savefig(output, **save_kwargs)
    plt.close(fig)
    print(f"Wrote comparison chart to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
