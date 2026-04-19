# Task B Swap-Gap Breakdown

Bucket mode: `pair_type`

## Qwen-1.5B-Instruct / baseline

| Bucket | n | swap_false acc | swap_true acc | abs gap |
| --- | ---: | ---: | ---: | ---: |
| same_act_different_motive | 23 | 1.0 | 0.5625 | 0.4375 |
| same_intention_moral_vs_immoral_action | 40 | 1.0 | 1.0 | 0.0 |

## Qwen-1.5B-Instruct / heart_focused

| Bucket | n | swap_false acc | swap_true acc | abs gap |
| --- | ---: | ---: | ---: | ---: |
| same_act_different_motive | 23 | 1.0 | 0.8235 | 0.1765 |
| same_intention_moral_vs_immoral_action | 40 | 1.0 | 1.0 | 0.0 |
