# Results Guide

This directory mixes two kinds of material:

- checked-in public artifacts that support the README and paper
- local historical or exploratory outputs from the development process

The checked-in public artifacts are the ones to trust first.

## Canonical public artifacts

- [main_same_act_confirmation_v12_mps/](main_same_act_confirmation_v12_mps/): frozen public `Baseline` vs `Heart-focused` confirmation artifact.
- [main_same_act_text_anchor_v1_qwen15b_mps/](main_same_act_text_anchor_v1_qwen15b_mps/): six-condition cross-tradition confirmation readout on Qwen-1.5B-Instruct.
- [main_same_act_text_anchor_v1_qwen15b_paired_order_mps/](main_same_act_text_anchor_v1_qwen15b_paired_order_mps/): paired-order stability follow-up for the six-condition confirmation slice.

## How to read the naming

- `main_same_act_confirmation_v12_mps` is the canonical narrow public release claim.
- `text_anchor` directories belong to the broader cross-tradition robustness layer.
- `_mps` in checked-in directory names is provenance from the original public run on Apple silicon. The current public reproduction scripts are device-neutral.

## Historical outputs

Files such as `pilot_v*`, `mock_*`, `main_partial_*`, and various `freeze_manifest` / `job_balance` snapshots are retained because they document the development process and release logic.

They are useful for:

- auditing revision history
- checking earlier pilot branches
- reproducing method decisions

They are not the first files a new reader should use to understand the public claim.
