# Same-Act Confirmation Readout

## Setup

- Benchmark: `paper_first_main_same_act_confirmation_v0`
- Slice composition: `23` `same_act_different_motive` items + `40` same-heart controls
- Conditions: `baseline`, `christian_heart`
- Model: `Qwen-1.5B-Instruct`
- Inference: `temperature=0`, `top_p=1.0`, `max_new_tokens=120`, `mps`

## What Held

- `126/126` valid records
- `parse_failure_rate = 0.0`
- `same_heart_control_accuracy = 1.0` for both conditions
- `heart_overreach_rate = 0.0` for both conditions
- mean explanation length stayed stable:
  - baseline: `111.54`
  - christian_heart: `109.16`

## Main Directional Result

On the full 63-item confirmation pack:

- `heart_sensitivity_score`: `0.6957 -> 0.8696` (`+0.1739`)
- `task_b_accuracy`: `0.8889 -> 0.9524` (`+0.0635`)
- `p(reason = motive)`: `0.4127 -> 0.4762` (`+0.0635`)

On the 23-item `same_act_different_motive` slice:

- `heart_sensitivity_score`: `0.6957 -> 0.8696` (`+0.1739`)
- paired bootstrap CI: `[0.0435, 0.3478]`
- paired sign counts: `4` better, `0` worse, `19` ties
- exact sign test:
  - two-sided `p = 0.125`
  - one-sided `p = 0.0625`

Interpretation:

- Christian heart-focused framing improved motive sensitivity directionally on the cleanest mechanistic slice.
- The gain was not accompanied by extra verbosity or same-heart overreach.
- The result is stronger than the 20-item pilot, but it is still not a full freeze-grade significance result under conservative paired testing.

## What Still Blocks Freeze

- Baseline still fails the swap-gap health threshold:
  - overall Task B swap gap: `0.1842`
- Christian passes the overall swap-gap threshold on this pack:
  - overall Task B swap gap: `0.0789`
- Same-act order sensitivity remains concentrated in the baseline condition:
  - baseline same-act swap gap: `0.4375`
  - christian_heart same-act swap gap: `0.1765`

So the confirmation pack strengthens the substantive direction of the effect, but it does not fully solve the order-robustness bar.

## Actionable Next Step

The power estimate from this pack says:

- for `same_act_different_motive` HSS under the observed effect pattern, the current `23` motive items only give:
  - directional sign-test power around `0.37`
  - two-sided sign-test power around `0.20`
- reaching roughly `0.80` power would require about:
  - `38` motive items under a directional sign test
  - `44` motive items under a two-sided sign test

Practical implication:

- add about `15` more clean `same_act_different_motive` items before treating this as a decisive confirmation slice
- keep the same-heart controls unchanged, because they are already doing their guardrail job well
