# Public Confirmation Paired-Order Follow-Up

## Setup

- Model: `Qwen-1.5B-Instruct`
- Slice: `23 same_act_different_motive items in both A/B orders`
- Conditions: `baseline, heart_focused`
- Complete paired-order records: `92`

## Main Result

- Maximum item-level Task B order-flip rate: `0.0`
- Maximum paired-order Task B accuracy gap: `0.0`

| Condition | Paired-order Task B | Order flips | Paired gap | Correct both orders | Wrong both orders |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline | 0.6957 | 0.0 | 0.0 | 16 | 7 |
| Heart-focused | 0.913 | 0.0 | 0.0 | 21 | 2 |

## Interpretation

- On this same-act follow-up, the public `baseline` and `heart_focused` conditions show no item-level Task B order flips.
- The paired-order accuracy gap is zero in both public conditions, so the earlier split-based swap-gap should not be read as same-item order instability on this slice.

## Primary File

- Source paired-order stability file: `results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.json`
