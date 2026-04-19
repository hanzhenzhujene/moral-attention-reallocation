# Public Confirmation Readout

## Setup

- Benchmark: `paper_first_main_same_act_confirmation_v0`
- Slice composition: `23 same_act_different_motive + 40 same-heart controls`
- Conditions: `baseline, heart_focused`
- Model: `Qwen-1.5B-Instruct`
- Valid records: `126`
- Parse failure rate: `0.0`

## What Held

- same-heart control accuracy stayed `1.0` in both conditions
- heart overreach stayed `0.0` in both conditions
- maximum explanation ratio vs baseline: `1.0`

| Condition | Task A | Task B | HSS | P(reason=motive) | Same-heart | Overreach | Mean chars |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 0.5079 | 0.8889 | 0.6957 | 0.4127 | 1.0 | 0.0 | 111.5397 |
| Heart-focused | 0.5079 | 0.9524 | 0.8696 | 0.4762 | 1.0 | 0.0 | 109.1587 |

## Main Directional Result

- `Task A` delta: `0.0`
- `Task B` delta: `0.0635`
- `heart_sensitivity_score` delta: `0.1739`
- `P(reason = motive)` delta: `0.0635`

## Same-Act Slice Evidence

- HSS delta on `same_act_different_motive`: `0.1739`
- paired sign counts: `4` better / `0` worse / `19` ties
- exact sign test: one-sided `0.0625`, two-sided `0.125`
- current directional sign-test power: `0.3706`
- minimum motive-sensitive items for target power: `38`

## Later Paired-Order Follow-Up

- paired-order records: `92`
- maximum item-level Task B order-flip rate: `0.0`
- maximum paired-order Task B gap: `0.0`

| Condition | Paired-order Task B | Order flips | Paired gap |
| --- | ---: | ---: | ---: |
| Baseline | 0.6957 | 0.0 | 0.0 |
| Heart-focused | 0.913 | 0.0 | 0.0 |

- On this follow-up, the public baseline and heart-focused conditions show no same-item Task B order instability.
- The remaining limitation on the public slice is power, not guardrail failure.

## Interpretation

- The public artifact supports a narrow mechanistic claim: heart-focused framing directionally improves inward-motive judgment on a clean confirmation slice.
- The strongest movement is in Task B and heart-sensitivity, not in the top-line Task A verdict.
- The gain does not come with worse same-heart controls, higher heart overreach, or longer explanations.

## Primary Files

- Summary: `results/main_same_act_confirmation_v12_mps/confirmation_summary.json`
- Robustness: `results/main_same_act_confirmation_v12_mps/confirmation_robustness.json`
- Health: `results/main_same_act_confirmation_v12_mps/confirmation_health.json`
- Paired-order follow-up: `results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.json`
