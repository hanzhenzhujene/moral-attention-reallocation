# Complete 6-Condition Comparison Tables

Full project-level cross-tradition matrix for `Qwen-1.5B-Instruct` on the 63-item confirmation slice.
Task A, Task B, and Task C are evaluated on all 63 items; HSS and paired-order Task B are evaluated on the 23 same-act pairs.

## How To Read These Tables

- Each column is one prompt condition: `Baseline`, `Heart-focused`, or one tradition-labeled text anchor.
- All values are proportions from `0` to `1` unless the row says `chars`.
- Higher is better for Task A, Task B, Task C motive-focus rate, HSS, same-heart control accuracy, and paired-order Task B accuracy.
- Lower is better for heart overreach, order-flip rate, and paired-order Task B gap.
- The table below is the main reader-facing comparison: scan across columns to compare each condition with `Baseline`.

## Metric Glossary

| Metric | Plain-English meaning |
| --- | --- |
| Task A accuracy | How often the model picks the more morally problematic case overall. |
| Task B accuracy | How often the model picks the case with the worse inward motive or heart posture. |
| Task C motive-focus rate | How often the model says motive, rather than act / consequence / rule, is the main reason for its Task A judgment. |
| HSS | Heart-sensitivity score on the 23 same-act / different-motive pairs. This is the main motive-sensitive metric. |
| Same-heart control accuracy | How often the model correctly keeps inward orientation matched on guardrail items. |
| Heart overreach rate | How often the model falsely projects a worse inward heart onto same-heart controls. Lower is better. |
| Paired-order Task B accuracy | Task B accuracy when the same 23 same-act items are rerun in both A/B orders. |
| Order-flip rate | How often the model changes which case it thinks has the worse inward orientation when the same item is shown in reverse order. |
| Paired-order Task B gap | Accuracy difference between the two presentation orders on the same items. Lower is better. |

## Table 1. Metric-by-condition matrix

| Metric | Baseline<br><sub>No religious text</sub> | Heart-focused<br><sub>Generic scaffold</sub> | Proverbs 4:23<br><sub>Biblical (Jewish/Christian)</sub> | Dhammapada 34<br><sub>Buddhist</sub> | Bhagavad Gita 15.15<br><sub>Hindu</sub> | Qur'an 26:88-89<br><sub>Islamic</sub> |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Task A accuracy (overall verdict) | 0.5079 | 0.5079 | 0.5079 | 0.5079 | 0.4762 | 0.4921 |
| Task B accuracy (inward orientation) | 0.8889 | 0.9683 | 0.9683 | 0.8889 | 0.9206 | 0.9206 |
| Task C motive-focus rate | 0.4127 | 0.4762 | 0.5397 | 0.4127 | 0.4603 | 0.5238 |
| Heart-sensitivity score (same-act) | 0.6957 | 0.9130 | 0.9130 | 0.6957 | 0.7826 | 0.7826 |
| Same-heart control accuracy | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Heart overreach rate | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Mean explanation length (chars) | 112.9 | 105.7 | 108.0 | 106.6 | 114.7 | 109.0 |
| Paired-order Task B accuracy | 0.6957 | 0.9130 | 0.9130 | 0.6957 | 0.7826 | 0.7826 |
| Order-flip rate | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Paired-order Task B gap | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

## Notes

- Identical percentages here reflect identical discrete counts on a small slice, not a rendering bug.
- Example: `Bhagavad Gita 15.15` and `Qur'an 26:88-89` both score `58/63` on Task B and `18/23` on HSS.
- `Heart-focused` and `Proverbs 4:23` tie at `61/63` on Task B and `21/23` on HSS.
- `Baseline` and `Dhammapada 34` tie at `56/63` on Task B and `16/23` on HSS.
