# Robustness Report

## Condition Summaries

| Model | Slice | Condition | n | Task A | Task B | HSS | P(reason=motive) | Same-Heart | Overreach | Mean chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-1.5B-Instruct | all_items | baseline | 63 | 0.5079 | 0.8889 | 0.6957 | 0.4127 | 1.0000 | 0.0000 | 111.5397 |
| Qwen-1.5B-Instruct | all_items | christian_heart | 63 | 0.5079 | 0.9524 | 0.8696 | 0.4762 | 1.0000 | 0.0000 | 109.1587 |
| Qwen-1.5B-Instruct | heartbench | baseline | 23 | 0.6087 | 0.6957 | 0.6957 | 0.9565 | - | - | 109.7391 |
| Qwen-1.5B-Instruct | heartbench | christian_heart | 23 | 0.5652 | 0.8696 | 0.8696 | 0.9565 | - | - | 107.2609 |
| Qwen-1.5B-Instruct | moralstories | baseline | 40 | 0.4500 | 1.0000 | - | 0.1000 | 1.0000 | 0.0000 | 112.5750 |
| Qwen-1.5B-Instruct | moralstories | christian_heart | 40 | 0.4750 | 1.0000 | - | 0.2000 | 1.0000 | 0.0000 | 110.2500 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline | 23 | 0.6087 | 0.6957 | 0.6957 | 0.9565 | - | - | 109.7391 |
| Qwen-1.5B-Instruct | motive_sensitive | christian_heart | 23 | 0.5652 | 0.8696 | 0.8696 | 0.9565 | - | - | 107.2609 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline | 23 | 0.6087 | 0.6957 | 0.6957 | 0.9565 | - | - | 109.7391 |
| Qwen-1.5B-Instruct | same_act_different_motive | christian_heart | 23 | 0.5652 | 0.8696 | 0.8696 | 0.9565 | - | - | 107.2609 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline | 40 | 0.4500 | 1.0000 | - | 0.1000 | 1.0000 | 0.0000 | 112.5750 |
| Qwen-1.5B-Instruct | same_heart_controls | christian_heart | 40 | 0.4750 | 1.0000 | - | 0.2000 | 1.0000 | 0.0000 | 110.2500 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline | 40 | 0.4500 | 1.0000 | - | 0.1000 | 1.0000 | 0.0000 | 112.5750 |
| Qwen-1.5B-Instruct | same_intention_controls | christian_heart | 40 | 0.4750 | 1.0000 | - | 0.2000 | 1.0000 | 0.0000 | 110.2500 |

## Paired Contrasts

| Model | Slice | Contrast | Metric | Delta | 95% CI | Better | Worse | Tie | p(two-sided) | p(one-sided) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-1.5B-Instruct | all_items | baseline -> christian_heart | task_a_accuracy | 0.0000 | [-0.1433, 0.1905] | 14 | 14 | 35 | 1.0000 | 0.5747 |
| Qwen-1.5B-Instruct | all_items | baseline -> christian_heart | task_b_accuracy | 0.0635 | [0.0159, 0.1270] | 4 | 0 | 59 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | all_items | baseline -> christian_heart | heart_sensitivity_score | 0.1739 | [0.0475, 0.3448] | 4 | 0 | 19 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | all_items | baseline -> christian_heart | p_reason_motive | 0.0635 | [-0.0159, 0.1429] | 6 | 2 | 55 | 0.2891 | 0.1445 |
| Qwen-1.5B-Instruct | all_items | baseline -> christian_heart | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> christian_heart | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> christian_heart | mean_explanation_chars | -2.3810 | [-9.5242, 4.6714] | 27 | 31 | 5 | 0.6940 | 0.7441 |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | task_a_accuracy | -0.0435 | [-0.2620, 0.2174] | 4 | 5 | 14 | 1.0000 | 0.7461 |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | task_b_accuracy | 0.1739 | [0.0435, 0.3478] | 4 | 0 | 19 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | heart_sensitivity_score | 0.1739 | [0.0435, 0.3478] | 4 | 0 | 19 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | mean_explanation_chars | -2.4783 | [-14.4391, 11.6957] | 9 | 12 | 2 | 0.6636 | 0.8083 |
| Qwen-1.5B-Instruct | moralstories | baseline -> christian_heart | task_a_accuracy | 0.0250 | [-0.2006, 0.2500] | 10 | 9 | 21 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | moralstories | baseline -> christian_heart | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> christian_heart | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> christian_heart | p_reason_motive | 0.1000 | [-0.0006, 0.2000] | 5 | 1 | 34 | 0.2188 | 0.1094 |
| Qwen-1.5B-Instruct | moralstories | baseline -> christian_heart | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> christian_heart | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> christian_heart | mean_explanation_chars | -2.3250 | [-10.9025, 4.7812] | 18 | 19 | 3 | 1.0000 | 0.6286 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | task_a_accuracy | -0.0435 | [-0.2620, 0.2174] | 4 | 5 | 14 | 1.0000 | 0.7461 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | task_b_accuracy | 0.1739 | [0.0435, 0.3478] | 4 | 0 | 19 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | heart_sensitivity_score | 0.1739 | [0.0435, 0.3478] | 4 | 0 | 19 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | mean_explanation_chars | -2.4783 | [-14.4391, 11.6957] | 9 | 12 | 2 | 0.6636 | 0.8083 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | task_a_accuracy | -0.0435 | [-0.2620, 0.2174] | 4 | 5 | 14 | 1.0000 | 0.7461 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | task_b_accuracy | 0.1739 | [0.0435, 0.3478] | 4 | 0 | 19 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | heart_sensitivity_score | 0.1739 | [0.0435, 0.3478] | 4 | 0 | 19 | 0.1250 | 0.0625 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | mean_explanation_chars | -2.4783 | [-14.4391, 11.6957] | 9 | 12 | 2 | 0.6636 | 0.8083 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | task_a_accuracy | 0.0250 | [-0.2006, 0.2500] | 10 | 9 | 21 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | p_reason_motive | 0.1000 | [-0.0006, 0.2000] | 5 | 1 | 34 | 0.2188 | 0.1094 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | mean_explanation_chars | -2.3250 | [-10.9025, 4.7812] | 18 | 19 | 3 | 1.0000 | 0.6286 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | task_a_accuracy | 0.0250 | [-0.2006, 0.2500] | 10 | 9 | 21 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | p_reason_motive | 0.1000 | [-0.0006, 0.2000] | 5 | 1 | 34 | 0.2188 | 0.1094 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | mean_explanation_chars | -2.3250 | [-10.9025, 4.7812] | 18 | 19 | 3 | 1.0000 | 0.6286 |

## Power Planning

Directional sign-test power uses alpha=0.05 and target power=0.80.

| Model | Slice | Contrast | Metric | Pairs | Better | Worse | Tie | Current power | Min N for target power |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | heart_sensitivity_score | 23 | 4 | 0 | 19 | 0.3706 | 38 |
| Qwen-1.5B-Instruct | heartbench | baseline -> christian_heart | p_reason_motive | 23 | 1 | 1 | 21 | 0.0012 | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | heart_sensitivity_score | 23 | 4 | 0 | 19 | 0.3706 | 38 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> christian_heart | p_reason_motive | 23 | 1 | 1 | 21 | 0.0012 | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | heart_sensitivity_score | 23 | 4 | 0 | 19 | 0.3706 | 38 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> christian_heart | p_reason_motive | 23 | 1 | 1 | 21 | 0.0012 | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> christian_heart | p_reason_motive | 40 | 5 | 1 | 34 | 0.3106 | 100 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> christian_heart | p_reason_motive | 40 | 5 | 1 | 34 | 0.3106 | 100 |
