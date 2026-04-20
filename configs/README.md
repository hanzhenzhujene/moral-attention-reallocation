# Config Guide

This directory contains both canonical public-study configs and historical revision snapshots from benchmark/prompt development.

## Public / reader-facing configs

- [paper_first_study_v1.json](paper_first_study_v1.json): study-level config for the frozen public `Baseline` vs `Heart-focused` artifact.
- [text_anchor_study_v1.json](text_anchor_study_v1.json): study-level config for the six-condition cross-tradition confirmation readout.
- [confirmation_execution_text_anchor_v1_qwen15b_mps.json](confirmation_execution_text_anchor_v1_qwen15b_mps.json): checked-in provenance snapshot for the public 6-condition Qwen-1.5B run.

## Historical development configs

Files named `pilot_execution_v*.json`, `pilot_execution_v*_mps.json`, `preview_execution_*.json`, and related smoke/fullpilot variants are retained as revision history from prompt and pipeline development.

They are useful for:

- reconstructing method evolution
- checking how `Task B` changed across revisions
- re-running specific earlier pilot branches

They are not the main entry point for new readers.

## Reproduction note

The public shell runners in [scripts/](../scripts/) now synthesize portable local runtime configs at execution time, so reproduction does not depend on matching the original development backend.

That means:

- checked-in `_mps` execution configs remain as provenance artifacts
- public reproduction scripts still auto-select `cuda`, `mps`, or `cpu`
