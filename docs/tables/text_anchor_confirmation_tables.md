# Complete 6-Condition Comparison Tables

Full project-level cross-tradition matrix for `Qwen-1.5B-Instruct` on the 63-item confirmation slice.
Task A, Task B, and Task C are evaluated on all 63 items; HSS and paired-order Task B are evaluated on the 23 same-act pairs.

## Table 1. Metric-by-condition matrix

| Metric | Baseline<br><sub>No religious text</sub> | Heart-focused<br><sub>Generic scaffold</sub> | Proverbs 4:23<br><sub>Biblical (Jewish/Christian)</sub> | Dhammapada 34<br><sub>Buddhist</sub> | Bhagavad Gita 15.15<br><sub>Hindu</sub> | Qur'an 26:88-89<br><sub>Islamic</sub> |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Task A overall verdict | 0.5079 | 0.5079 | 0.5079 | 0.5079 | 0.4762 | 0.4921 |
| Task B inward-orientation judgment | 0.8889 | 0.9683 | 0.9683 | 0.8889 | 0.9206 | 0.9206 |
| Task C motive as primary reason | 0.4127 | 0.4762 | 0.5397 | 0.4127 | 0.4603 | 0.5238 |
| Heart-sensitivity score | 0.6957 | 0.9130 | 0.9130 | 0.6957 | 0.7826 | 0.7826 |
| Same-heart control accuracy | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Heart overreach rate | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Mean explanation chars | 112.9 | 105.7 | 108.0 | 106.6 | 114.7 | 109.0 |
| Paired-order Task B | 0.6957 | 0.9130 | 0.9130 | 0.6957 | 0.7826 | 0.7826 |
| Order-flip rate | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Paired-order Task B gap | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

## Table 2. Condition-by-delta matrix vs baseline

| Condition | Tradition / frame | Delta Task A | Delta Task B | Delta Task C = motive | Delta HSS | Delta chars | Same-heart | Overreach | Paired-order stable |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Heart-focused | Generic scaffold | +0.0000 | +0.0794 | +0.0635 | +0.2173 | -7.3 | 1.0000 | 0.0000 | yes |
| Proverbs 4:23 | Biblical (Jewish/Christian) | +0.0000 | +0.0794 | +0.1270 | +0.2173 | -4.9 | 1.0000 | 0.0000 | yes |
| Dhammapada 34 | Buddhist | +0.0000 | +0.0000 | +0.0000 | +0.0000 | -6.3 | 1.0000 | 0.0000 | yes |
| Bhagavad Gita 15.15 | Hindu | -0.0317 | +0.0317 | +0.0476 | +0.0869 | +1.8 | 1.0000 | 0.0000 | yes |
| Qur'an 26:88-89 | Islamic | -0.0158 | +0.0317 | +0.1111 | +0.0869 | -3.9 | 1.0000 | 0.0000 | yes |

## Notes

- Identical percentages here reflect identical discrete counts on a small slice, not a rendering bug.
- Example: `Bhagavad Gita 15.15` and `Qur'an 26:88-89` both score `58/63` on Task B and `18/23` on HSS.
- `Heart-focused` and `Proverbs 4:23` tie at `61/63` on Task B and `21/23` on HSS.
- `Baseline` and `Dhammapada 34` tie at `56/63` on Task B and `16/23` on HSS.
