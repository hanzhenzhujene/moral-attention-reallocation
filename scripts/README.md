# Script Guide

This directory contains both public entry-point scripts and lower-level utilities used to build, score, and audit the benchmark.

## Start here

Public-facing entry points:

- [reproduce_confirmation_slice.sh](reproduce_confirmation_slice.sh): reproduce the frozen public `Baseline` vs `Heart-focused` confirmation artifact.
- [reproduce_confirmation_paired_order_followup.sh](reproduce_confirmation_paired_order_followup.sh): reproduce the public paired-order follow-up on the same-act slice.
- [run_text_anchor_confirmation_qwen15b.sh](run_text_anchor_confirmation_qwen15b.sh): run the six-condition cross-tradition confirmation artifact.
- [run_text_anchor_confirmation_paired_order_qwen15b.sh](run_text_anchor_confirmation_paired_order_qwen15b.sh): run the paired-order stability follow-up for the six-condition confirmation slice.
- [refresh_public_artifacts.sh](refresh_public_artifacts.sh): regenerate the checked-in public figures and tables from the canonical result JSON files.
- [build_paper.sh](build_paper.sh): build the paper PDF.

## Core runtime

- [run_transformers_multipass.py](run_transformers_multipass.py): main multi-pass inference runner used by the public artifacts.
- [evaluate_runs.py](evaluate_runs.py): compute metric summaries and item-level contrasts.
- [evaluate_robustness_report.py](evaluate_robustness_report.py): generate paired bootstrap and sign-test robustness summaries.
- [evaluate_pilot_health.py](evaluate_pilot_health.py): compute guardrail and method-health checks.

## Rendering and reporting

- `render_*`: figure and report writers used to create public-facing SVG/PDF/Markdown artifacts.
- [render_text_anchor_confirmation_tables.py](render_text_anchor_confirmation_tables.py): regenerate the 6-condition table for both README/docs and the paper include.

## Benchmark tooling

- `build_*`, `validate_*`, `audit_*`, `check_*`, `score_*`: utilities for benchmark construction, annotation workflows, release gates, and agreement checking.

## Historical scripts

Some scripts, especially `run_text_anchor_pilot.sh`, `run_text_anchor_paired_order_same_act.sh`, and earlier pilot utilities, are retained as development history rather than current public entry points.
