# Text-Anchor Confirmation Readout

## Setup

- Benchmark: `paper_first_main_same_act_confirmation_v0`
- Slice composition: `23 same_act_different_motive + 40 same-heart controls`
- Conditions: `Baseline, Heart-focused, 4 text anchors`
- Model: `Qwen-1.5B-Instruct`
- Valid records: `378`
- Parse failure rate: `0.0`

## What Held

- same-heart control accuracy minimum across all 6 conditions: `1.0`
- heart overreach maximum across all 6 conditions: `0.0`
- maximum explanation ratio vs baseline: `1.0157`

| Condition | Task A | Task B | HSS | P(reason=motive) | Same-heart | Overreach |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline (no religious text) | 0.5079 | 0.8889 | 0.6957 | 0.4127 | 1.0 | 0.0 |
| Heart-focused (generic scaffold) | 0.5079 | 0.9683 | 0.913 | 0.4762 | 1.0 | 0.0 |
| Proverbs 4:23 (Biblical; Jewish/Christian) | 0.5079 | 0.9683 | 0.913 | 0.5397 | 1.0 | 0.0 |
| Dhammapada 34 (Buddhist) | 0.5079 | 0.8889 | 0.6957 | 0.4127 | 1.0 | 0.0 |
| Bhagavad Gita 15.15 (Hindu) | 0.4762 | 0.9206 | 0.7826 | 0.4603 | 1.0 | 0.0 |
| Qur'an 26:88-89 (Islamic) | 0.4921 | 0.9206 | 0.7826 | 0.5238 | 1.0 | 0.0 |

## Main Project-Level Result

- `Heart-focused` vs `Baseline` Task B: `0.0794`
- `Heart-focused` vs `Baseline` HSS: `0.2173`
- supportive text anchors vs baseline: `3` / `4`
- mean text-anchor delta vs baseline on Task B: `0.0357`
- mean text-anchor delta vs baseline on HSS: `0.0978`

| Text anchor | Delta Task B vs baseline | Delta HSS vs baseline | Delta HSS vs heart-focused |
| --- | ---: | ---: | ---: |
| Proverbs 4:23 | 0.0794 | 0.2173 | 0.0 |
| Dhammapada 34 | 0.0 | 0.0 | -0.2173 |
| Bhagavad Gita 15.15 | 0.0317 | 0.0869 | -0.1304 |
| Qur'an 26:88-89 | 0.0317 | 0.0869 | -0.1304 |

## Same-Act Slice Robustness

### Heart-focused (generic scaffold) vs baseline

- HSS delta vs baseline: `0.2174`
- paired sign counts: `5` better / `0` worse / `18` ties
- exact sign test: one-sided `0.03125`, two-sided `0.0625`

### Proverbs 4:23 (Biblical; Jewish/Christian) vs baseline

- HSS delta vs baseline: `0.2174`
- paired sign counts: `5` better / `0` worse / `18` ties
- exact sign test: one-sided `0.03125`, two-sided `0.0625`

### Dhammapada 34 (Buddhist) vs baseline

- HSS delta vs baseline: `0.0`
- paired sign counts: `2` better / `2` worse / `19` ties
- exact sign test: one-sided `0.6875`, two-sided `1.0`

### Bhagavad Gita 15.15 (Hindu) vs baseline

- HSS delta vs baseline: `0.087`
- paired sign counts: `4` better / `2` worse / `17` ties
- exact sign test: one-sided `0.34375`, two-sided `0.6875`

### Qur'an 26:88-89 (Islamic) vs baseline

- HSS delta vs baseline: `0.087`
- paired sign counts: `4` better / `2` worse / `17` ties
- exact sign test: one-sided `0.34375`, two-sided `0.6875`

## Confirmation Paired-Order Diagnostic

- paired-order records: `276`
- maximum item-level Task B order-flip rate: `0.0`
- maximum paired-order Task B accuracy gap: `0.0`

| Condition | Paired-order Task B | Order flips | Paired gap |
| --- | ---: | ---: | ---: |
| Baseline (no religious text) | 0.6957 | 0.0 | 0.0 |
| Bhagavad Gita 15.15 (Hindu) | 0.7826 | 0.0 | 0.0 |
| Dhammapada 34 (Buddhist) | 0.6957 | 0.0 | 0.0 |
| Heart-focused (generic scaffold) | 0.913 | 0.0 | 0.0 |
| Proverbs 4:23 (Biblical; Jewish/Christian) | 0.913 | 0.0 | 0.0 |
| Qur'an 26:88-89 (Islamic) | 0.7826 | 0.0 | 0.0 |

## Interpretation

- This run is a targeted six-condition confirmation on the model that showed the strongest earlier support; it is broader than the frozen release artifact, but it is not a new freeze-grade cross-model main claim.
- The confirmation question is whether multiple text-anchored variants continue to move motive-sensitive metrics in the same direction as `Heart-focused` while preserving same-heart controls.
- The confirmation paired-order pack matters because it separates genuine same-item order instability from split-based swap-gap artifacts. On this run, the same-item paired-order diagnostic is clean across all six conditions.
- The current project-level result is therefore strongest for `Heart-focused` and `Proverbs 4:23`: both improve the mechanistic target on the confirmation slice, preserve same-heart guardrails, and stay stable under paired-order diagnosis.

## Primary Files

- Summary: `results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_summary.json`
- Robustness: `results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_robustness.json`
- Family summary: `results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_text_anchor_family.json`
- Health: `results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_health.json`
- Paired-order stability: `results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.json`
