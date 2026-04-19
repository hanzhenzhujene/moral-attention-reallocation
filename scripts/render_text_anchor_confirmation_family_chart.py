#!/usr/bin/env python3
"""Render a compact figure for the Qwen-1.5B text-anchor confirmation run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

import condition_registry


ORDER = [
    "baseline",
    "heart_focused",
    "proverbs_4_23",
    "bhagavad_gita_15_15",
    "quran_26_88_89",
    "dhammapada_34",
]

COLORS = {
    "baseline": "#64748b",
    "heart_focused": "#0f766e",
    "proverbs_4_23": "#1d4ed8",
    "bhagavad_gita_15_15": "#b45309",
    "quran_26_88_89": "#047857",
    "dhammapada_34": "#7c3aed",
}


def load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def point(row: Dict[str, Any], metric_name: str) -> float:
    return float(row["metrics"][metric_name]["point"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--paired-order")
    parser.add_argument("--model", required=True)
    parser.add_argument("--output-svg", required=True)
    parser.add_argument("--output-png")
    parser.add_argument("--output-pdf")
    args = parser.parse_args()

    summary = load_json(args.summary)
    paired_order = load_json(args.paired_order) if args.paired_order else None

    rows = {
        row["condition"]: row
        for row in summary["summaries"]
        if row["model"] == args.model
    }

    labels = [condition_registry.display_name(condition) for condition in ORDER]
    task_b = [point(rows[condition], "task_b_accuracy") for condition in ORDER]
    hss = [point(rows[condition], "heart_sensitivity_score") for condition in ORDER]
    reason = [point(rows[condition], "p_reason_motive") for condition in ORDER]
    same_heart = [point(rows[condition], "same_heart_control_accuracy") for condition in ORDER]
    overreach = [point(rows[condition], "heart_overreach_rate") for condition in ORDER]
    paired_lookup = {}
    if paired_order:
        paired_lookup = {
            row["condition"]: row
            for row in paired_order["groups"]
            if row["model"] == args.model
        }
    paired_flip = [paired_lookup.get(condition, {}).get("task_b_order_flip_rate") for condition in ORDER]
    paired_gap = [paired_lookup.get(condition, {}).get("task_b_accuracy_gap") for condition in ORDER]

    fig = plt.figure(figsize=(11.2, 7.1), dpi=180)
    gs = fig.add_gridspec(
        4,
        1,
        height_ratios=[0.58, 1.42, 1.42, 0.92],
        hspace=0.38,
        top=0.94,
        bottom=0.07,
        left=0.17,
        right=0.97,
    )

    title_ax = fig.add_subplot(gs[0, 0])
    title_ax.axis("off")
    title_ax.text(
        0.0,
        0.82,
        "Exploratory 6-Condition Confirmation",
        fontsize=19.5,
        fontweight="bold",
        color="#0f172a",
        ha="left",
        va="center",
    )
    title_ax.text(
        0.0,
        0.44,
        "Qwen-1.5B-Instruct on the 63-item same-act confirmation slice",
        fontsize=11.5,
        color="#334155",
        ha="left",
        va="center",
    )
    title_ax.text(
        0.0,
        0.12,
        "Heart-focused and Proverbs 4:23 tie for the strongest gain; all six conditions keep controls clean.",
        fontsize=10.2,
        color="#475569",
        ha="left",
        va="center",
    )

    def draw_metric(ax, values: List[float], title: str, baseline_value: float, xlim: tuple[float, float]) -> None:
        ax.set_title(title, loc="left", fontsize=13.2, fontweight="bold", color="#0f172a", pad=10)
        y_positions = list(range(len(ORDER)))
        ax.barh(
            y_positions,
            values,
            color=[COLORS[condition] for condition in ORDER],
            edgecolor="none",
            height=0.62,
        )
        ax.axvline(baseline_value, color="#94a3b8", linestyle="--", linewidth=1.2)
        ax.set_yticks(y_positions)
        ax.set_yticklabels(labels, fontsize=10.5, color="#0f172a")
        ax.set_xlim(*xlim)
        ax.invert_yaxis()
        ax.grid(axis="x", color="#e2e8f0", linewidth=0.8)
        ax.set_axisbelow(True)
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.tick_params(axis="x", labelsize=10, colors="#334155")
        ax.tick_params(axis="y", length=0)
        for y, value in zip(y_positions, values):
            ax.text(
                min(value + 0.01, xlim[1] - 0.004),
                y,
                f"{value:.3f}",
                va="center",
                ha="left",
                fontsize=10.2,
                color="#0f172a",
            )

    ax1 = fig.add_subplot(gs[1, 0])
    draw_metric(ax1, task_b, "Task B: inward-orientation judgment", task_b[0], (0.84, 1.0))

    ax2 = fig.add_subplot(gs[2, 0])
    draw_metric(ax2, hss, "Heart-sensitivity score on same-act motive pairs", hss[0], (0.64, 0.96))

    footer_ax = fig.add_subplot(gs[3, 0])
    footer_ax.axis("off")
    card_specs = [
        (0.00, 0.02, 0.31, 0.90, "#f8fafc"),
        (0.345, 0.02, 0.31, 0.90, "#f0fdf4"),
        (0.69, 0.02, 0.31, 0.90, "#eff6ff"),
    ]
    for x, y, w, h, face in card_specs:
        footer_ax.add_patch(
            FancyBboxPatch(
                (x, y),
                w,
                h,
                boxstyle="round,pad=0.012,rounding_size=0.02",
                linewidth=1.0,
                edgecolor="#cbd5e1",
                facecolor=face,
                transform=footer_ax.transAxes,
                clip_on=False,
            )
        )

    footer_ax.text(
        0.03,
        0.72,
        "Task C: reason focus",
        fontsize=12.0,
        fontweight="bold",
        color="#0f172a",
        transform=footer_ax.transAxes,
    )
    footer_ax.text(
        0.03,
        0.46,
        f"Baseline {reason[0]:.3f} | Heart-focused {reason[1]:.3f}",
        fontsize=10.5,
        color="#334155",
        transform=footer_ax.transAxes,
    )
    footer_ax.text(
        0.03,
        0.20,
        f"Best anchor: Proverbs 4:23 = {reason[2]:.3f}",
        fontsize=10.5,
        color="#334155",
        transform=footer_ax.transAxes,
    )

    footer_ax.text(
        0.375,
        0.72,
        "Guardrails",
        fontsize=12.0,
        fontweight="bold",
        color="#0f172a",
        transform=footer_ax.transAxes,
    )
    footer_ax.text(
        0.375,
        0.46,
        f"Same-heart control = {min(same_heart):.1f} in all 6",
        fontsize=10.5,
        color="#334155",
        transform=footer_ax.transAxes,
    )
    footer_ax.text(
        0.375,
        0.20,
        f"Heart overreach = {max(overreach):.1f} in all 6",
        fontsize=10.5,
        color="#334155",
        transform=footer_ax.transAxes,
    )

    max_flip = max(paired_flip) if paired_flip and all(value is not None for value in paired_flip) else None
    max_gap = max(paired_gap) if paired_gap and all(value is not None for value in paired_gap) else None
    footer_ax.text(
        0.72,
        0.72,
        "Paired-order check",
        fontsize=12.0,
        fontweight="bold",
        color="#0f172a",
        transform=footer_ax.transAxes,
    )
    footer_ax.text(
        0.72,
        0.46,
        "Same-act Task B flipped on 0 items" if max_flip == 0 else "Order flips pending",
        fontsize=10.5,
        color="#334155",
        transform=footer_ax.transAxes,
    )
    footer_ax.text(
        0.72,
        0.20,
        f"Maximum paired-order gap = {max_gap:.1f}" if max_gap is not None else "Paired-order gap unavailable",
        fontsize=10.5,
        color="#334155",
        transform=footer_ax.transAxes,
    )

    output_svg = Path(args.output_svg)
    output_svg.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_svg, format="svg", bbox_inches="tight")
    if args.output_png:
        output_png = Path(args.output_png)
        output_png.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_png, format="png", bbox_inches="tight")
    if args.output_pdf:
        output_pdf = Path(args.output_pdf)
        output_pdf.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_pdf, format="pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote figure to {output_svg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
