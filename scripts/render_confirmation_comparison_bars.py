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
BG = "#f7f9fc"
BASELINE = "#7c8ea5"
FOCUSED = "#117a72"
GRID = "#d7dfeb"
TEXT = "#18263d"
MUTED = "#5f7086"
HILITE = "#edf7f4"


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
            fontsize=12,
            fontweight="bold",
            color=color,
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True, help="Path to confirmation_summary.json")
    parser.add_argument("--robustness", required=True, help="Path to confirmation_robustness.json")
    parser.add_argument("--output", required=True, help="Output path (.png, .svg, or .pdf)")
    args = parser.parse_args()

    summary = load_json(Path(args.summary))
    by_condition = {row["condition"]: row["metrics"] for row in summary["summaries"]}
    baseline = by_condition["baseline"]
    focused = by_condition["heart_focused"]

    all_contrast = summary["contrasts"][0]["metrics"]

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

    fig = plt.figure(figsize=(13.8, 6.8), facecolor=BG)
    ax_main = fig.add_subplot(111, facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.985, bottom=0.16, top=0.84)

    ax_main.set_ylim(0.0, 1.08)
    ax_main.set_yticks(np.linspace(0.0, 1.0, 6))
    ax_main.grid(axis="y", color=GRID, linewidth=1, alpha=0.9)
    ax_main.set_axisbelow(True)
    ax_main.spines["left"].set_color(GRID)
    ax_main.spines["bottom"].set_color(GRID)

    main_specs = [
        ("Task A\noverall verdict", "task_a_accuracy"),
        ("Task B\nmotive judgment", "task_b_accuracy"),
        ("Heart-\nsensitivity", "heart_sensitivity_score"),
        ("Task C\nreason = motive", "p_reason_motive"),
    ]
    x_main = np.arange(len(main_specs))
    width = 0.34

    ax_main.axvspan(0.55, 2.45, color=HILITE, zorder=0)
    ax_main.text(
        1.5,
        1.045,
        "main signal",
        ha="center",
        va="center",
        fontsize=11.5,
        fontweight="bold",
        color=FOCUSED,
        bbox=dict(boxstyle="round,pad=0.3,rounding_size=0.6", facecolor="#dff3ee", edgecolor="#c3e4db"),
    )

    baseline_main = [metric_triplet(baseline, key) for _, key in main_specs]
    focused_main = [metric_triplet(focused, key) for _, key in main_specs]

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
        label="heart-focused",
        yerr=make_err(focused_main),
        capsize=3,
        ecolor="#0a5d57",
        linewidth=0,
    )
    ax_main.set_xticks(x_main)
    ax_main.set_xticklabels([label for label, _ in main_specs], fontsize=13)
    ax_main.set_title("Primary outcomes", fontsize=18, loc="left", pad=12, color=TEXT)
    ax_main.set_ylabel("Score", fontsize=12)

    label_bars(ax_main, bars_base_main, [point for point, _, _ in baseline_main], TEXT)
    label_bars(ax_main, bars_focus_main, [point for point, _, _ in focused_main], FOCUSED)

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

    fig.suptitle(
        "Public confirmation slice",
        fontsize=22,
        fontweight="bold",
        x=0.055,
        y=0.955,
        ha="left",
        color=TEXT,
    )
    ax_main.legend(
        handles=[bars_base_main, bars_focus_main],
        labels=["Baseline prompt", "Heart-focused prompt"],
        loc="upper right",
        bbox_to_anchor=(0.99, 0.93),
        ncol=1,
        frameon=True,
        facecolor="white",
        edgecolor=GRID,
        fontsize=11.5,
        handlelength=1.5,
        borderpad=0.6,
        labelspacing=0.5,
    )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"facecolor": BG}
    if output.suffix.lower() == ".png":
        save_kwargs["dpi"] = 220
    fig.savefig(output, **save_kwargs)
    plt.close(fig)
    if output.suffix.lower() == ".svg":
        output.write_text(
            "\n".join(line.rstrip() for line in output.read_text(encoding="utf-8").splitlines()) + "\n",
            encoding="utf-8",
        )
    print(f"Wrote comparison chart to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
