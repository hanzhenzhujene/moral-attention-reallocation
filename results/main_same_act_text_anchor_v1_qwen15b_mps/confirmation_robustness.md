# Robustness Report

## Condition Summaries

| Model | Slice | Condition | n | Task A | Task B | HSS | P(reason=motive) | Same-Heart | Overreach | Mean chars |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-1.5B-Instruct | all_items | baseline | 63 | 0.5079 | 0.8889 | 0.6957 | 0.4127 | 1.0000 | 0.0000 | 112.9365 |
| Qwen-1.5B-Instruct | all_items | bhagavad_gita_15_15 | 63 | 0.4762 | 0.9206 | 0.7826 | 0.4603 | 1.0000 | 0.0000 | 114.7143 |
| Qwen-1.5B-Instruct | all_items | dhammapada_34 | 63 | 0.5079 | 0.8889 | 0.6957 | 0.4127 | 1.0000 | 0.0000 | 106.6190 |
| Qwen-1.5B-Instruct | all_items | heart_focused | 63 | 0.5079 | 0.9683 | 0.9130 | 0.4762 | 1.0000 | 0.0000 | 105.6508 |
| Qwen-1.5B-Instruct | all_items | proverbs_4_23 | 63 | 0.5079 | 0.9683 | 0.9130 | 0.5397 | 1.0000 | 0.0000 | 108.0000 |
| Qwen-1.5B-Instruct | all_items | quran_26_88_89 | 63 | 0.4921 | 0.9206 | 0.7826 | 0.5238 | 1.0000 | 0.0000 | 109.0000 |
| Qwen-1.5B-Instruct | heartbench | baseline | 23 | 0.6087 | 0.6957 | 0.6957 | 0.9565 | - | - | 111.4783 |
| Qwen-1.5B-Instruct | heartbench | bhagavad_gita_15_15 | 23 | 0.5217 | 0.7826 | 0.7826 | 0.9565 | - | - | 106.6522 |
| Qwen-1.5B-Instruct | heartbench | dhammapada_34 | 23 | 0.6522 | 0.6957 | 0.6957 | 0.9130 | - | - | 98.5217 |
| Qwen-1.5B-Instruct | heartbench | heart_focused | 23 | 0.6957 | 0.9130 | 0.9130 | 0.9565 | - | - | 108.6087 |
| Qwen-1.5B-Instruct | heartbench | proverbs_4_23 | 23 | 0.4783 | 0.9130 | 0.9130 | 1.0000 | - | - | 103.1739 |
| Qwen-1.5B-Instruct | heartbench | quran_26_88_89 | 23 | 0.7391 | 0.7826 | 0.7826 | 1.0000 | - | - | 104.6957 |
| Qwen-1.5B-Instruct | moralstories | baseline | 40 | 0.4500 | 1.0000 | - | 0.1000 | 1.0000 | 0.0000 | 113.7750 |
| Qwen-1.5B-Instruct | moralstories | bhagavad_gita_15_15 | 40 | 0.4500 | 1.0000 | - | 0.1750 | 1.0000 | 0.0000 | 119.3500 |
| Qwen-1.5B-Instruct | moralstories | dhammapada_34 | 40 | 0.4250 | 1.0000 | - | 0.1250 | 1.0000 | 0.0000 | 111.2750 |
| Qwen-1.5B-Instruct | moralstories | heart_focused | 40 | 0.4000 | 1.0000 | - | 0.2000 | 1.0000 | 0.0000 | 103.9500 |
| Qwen-1.5B-Instruct | moralstories | proverbs_4_23 | 40 | 0.5250 | 1.0000 | - | 0.2750 | 1.0000 | 0.0000 | 110.7750 |
| Qwen-1.5B-Instruct | moralstories | quran_26_88_89 | 40 | 0.3500 | 1.0000 | - | 0.2500 | 1.0000 | 0.0000 | 111.4750 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline | 23 | 0.6087 | 0.6957 | 0.6957 | 0.9565 | - | - | 111.4783 |
| Qwen-1.5B-Instruct | motive_sensitive | bhagavad_gita_15_15 | 23 | 0.5217 | 0.7826 | 0.7826 | 0.9565 | - | - | 106.6522 |
| Qwen-1.5B-Instruct | motive_sensitive | dhammapada_34 | 23 | 0.6522 | 0.6957 | 0.6957 | 0.9130 | - | - | 98.5217 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused | 23 | 0.6957 | 0.9130 | 0.9130 | 0.9565 | - | - | 108.6087 |
| Qwen-1.5B-Instruct | motive_sensitive | proverbs_4_23 | 23 | 0.4783 | 0.9130 | 0.9130 | 1.0000 | - | - | 103.1739 |
| Qwen-1.5B-Instruct | motive_sensitive | quran_26_88_89 | 23 | 0.7391 | 0.7826 | 0.7826 | 1.0000 | - | - | 104.6957 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline | 23 | 0.6087 | 0.6957 | 0.6957 | 0.9565 | - | - | 111.4783 |
| Qwen-1.5B-Instruct | same_act_different_motive | bhagavad_gita_15_15 | 23 | 0.5217 | 0.7826 | 0.7826 | 0.9565 | - | - | 106.6522 |
| Qwen-1.5B-Instruct | same_act_different_motive | dhammapada_34 | 23 | 0.6522 | 0.6957 | 0.6957 | 0.9130 | - | - | 98.5217 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused | 23 | 0.6957 | 0.9130 | 0.9130 | 0.9565 | - | - | 108.6087 |
| Qwen-1.5B-Instruct | same_act_different_motive | proverbs_4_23 | 23 | 0.4783 | 0.9130 | 0.9130 | 1.0000 | - | - | 103.1739 |
| Qwen-1.5B-Instruct | same_act_different_motive | quran_26_88_89 | 23 | 0.7391 | 0.7826 | 0.7826 | 1.0000 | - | - | 104.6957 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline | 40 | 0.4500 | 1.0000 | - | 0.1000 | 1.0000 | 0.0000 | 113.7750 |
| Qwen-1.5B-Instruct | same_heart_controls | bhagavad_gita_15_15 | 40 | 0.4500 | 1.0000 | - | 0.1750 | 1.0000 | 0.0000 | 119.3500 |
| Qwen-1.5B-Instruct | same_heart_controls | dhammapada_34 | 40 | 0.4250 | 1.0000 | - | 0.1250 | 1.0000 | 0.0000 | 111.2750 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused | 40 | 0.4000 | 1.0000 | - | 0.2000 | 1.0000 | 0.0000 | 103.9500 |
| Qwen-1.5B-Instruct | same_heart_controls | proverbs_4_23 | 40 | 0.5250 | 1.0000 | - | 0.2750 | 1.0000 | 0.0000 | 110.7750 |
| Qwen-1.5B-Instruct | same_heart_controls | quran_26_88_89 | 40 | 0.3500 | 1.0000 | - | 0.2500 | 1.0000 | 0.0000 | 111.4750 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline | 40 | 0.4500 | 1.0000 | - | 0.1000 | 1.0000 | 0.0000 | 113.7750 |
| Qwen-1.5B-Instruct | same_intention_controls | bhagavad_gita_15_15 | 40 | 0.4500 | 1.0000 | - | 0.1750 | 1.0000 | 0.0000 | 119.3500 |
| Qwen-1.5B-Instruct | same_intention_controls | dhammapada_34 | 40 | 0.4250 | 1.0000 | - | 0.1250 | 1.0000 | 0.0000 | 111.2750 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused | 40 | 0.4000 | 1.0000 | - | 0.2000 | 1.0000 | 0.0000 | 103.9500 |
| Qwen-1.5B-Instruct | same_intention_controls | proverbs_4_23 | 40 | 0.5250 | 1.0000 | - | 0.2750 | 1.0000 | 0.0000 | 110.7750 |
| Qwen-1.5B-Instruct | same_intention_controls | quran_26_88_89 | 40 | 0.3500 | 1.0000 | - | 0.2500 | 1.0000 | 0.0000 | 111.4750 |

## Paired Contrasts

| Model | Slice | Contrast | Metric | Delta | 95% CI | Better | Worse | Tie | p(two-sided) | p(one-sided) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-1.5B-Instruct | all_items | baseline -> bhagavad_gita_15_15 | task_a_accuracy | -0.0317 | [-0.2063, 0.1746] | 16 | 18 | 29 | 0.8642 | 0.6962 |
| Qwen-1.5B-Instruct | all_items | baseline -> bhagavad_gita_15_15 | task_b_accuracy | 0.0317 | [-0.0321, 0.1115] | 4 | 2 | 57 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | all_items | baseline -> bhagavad_gita_15_15 | heart_sensitivity_score | 0.0870 | [-0.1176, 0.3158] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | all_items | baseline -> bhagavad_gita_15_15 | p_reason_motive | 0.0476 | [-0.0476, 0.1429] | 6 | 3 | 54 | 0.5078 | 0.2539 |
| Qwen-1.5B-Instruct | all_items | baseline -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> bhagavad_gita_15_15 | mean_explanation_chars | 1.7778 | [-7.4631, 10.6841] | 31 | 31 | 1 | 1.0000 | 0.5505 |
| Qwen-1.5B-Instruct | all_items | baseline -> dhammapada_34 | task_a_accuracy | 0.0000 | [-0.1587, 0.1746] | 13 | 13 | 37 | 1.0000 | 0.5775 |
| Qwen-1.5B-Instruct | all_items | baseline -> dhammapada_34 | task_b_accuracy | 0.0000 | [-0.0635, 0.0476] | 2 | 2 | 59 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | all_items | baseline -> dhammapada_34 | heart_sensitivity_score | 0.0000 | [-0.1819, 0.1482] | 2 | 2 | 19 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | all_items | baseline -> dhammapada_34 | p_reason_motive | 0.0000 | [-0.0794, 0.0635] | 3 | 3 | 57 | 1.0000 | 0.6562 |
| Qwen-1.5B-Instruct | all_items | baseline -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> dhammapada_34 | mean_explanation_chars | -6.3175 | [-15.5952, 1.9341] | 23 | 36 | 4 | 0.1175 | 0.9663 |
| Qwen-1.5B-Instruct | all_items | baseline -> heart_focused | task_a_accuracy | 0.0000 | [-0.1746, 0.2063] | 18 | 18 | 27 | 1.0000 | 0.5660 |
| Qwen-1.5B-Instruct | all_items | baseline -> heart_focused | task_b_accuracy | 0.0794 | [0.0159, 0.1587] | 5 | 0 | 58 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | all_items | baseline -> heart_focused | heart_sensitivity_score | 0.2174 | [0.0713, 0.4091] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | all_items | baseline -> heart_focused | p_reason_motive | 0.0635 | [-0.0317, 0.1587] | 6 | 2 | 55 | 0.2891 | 0.1445 |
| Qwen-1.5B-Instruct | all_items | baseline -> heart_focused | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> heart_focused | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> heart_focused | mean_explanation_chars | -7.2857 | [-14.0036, 0.1290] | 27 | 33 | 3 | 0.5190 | 0.8169 |
| Qwen-1.5B-Instruct | all_items | baseline -> proverbs_4_23 | task_a_accuracy | 0.0000 | [-0.1591, 0.1746] | 16 | 16 | 31 | 1.0000 | 0.5700 |
| Qwen-1.5B-Instruct | all_items | baseline -> proverbs_4_23 | task_b_accuracy | 0.0794 | [0.0159, 0.1587] | 5 | 0 | 58 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | all_items | baseline -> proverbs_4_23 | heart_sensitivity_score | 0.2174 | [0.0713, 0.4091] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | all_items | baseline -> proverbs_4_23 | p_reason_motive | 0.1270 | [0.0635, 0.2222] | 8 | 0 | 55 | 0.0078 | 0.0039 |
| Qwen-1.5B-Instruct | all_items | baseline -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> proverbs_4_23 | mean_explanation_chars | -4.9365 | [-12.2730, 2.9052] | 24 | 36 | 3 | 0.1550 | 0.9538 |
| Qwen-1.5B-Instruct | all_items | baseline -> quran_26_88_89 | task_a_accuracy | -0.0159 | [-0.1587, 0.1429] | 12 | 13 | 38 | 1.0000 | 0.6550 |
| Qwen-1.5B-Instruct | all_items | baseline -> quran_26_88_89 | task_b_accuracy | 0.0317 | [-0.0321, 0.1115] | 4 | 2 | 57 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | all_items | baseline -> quran_26_88_89 | heart_sensitivity_score | 0.0870 | [-0.1176, 0.3158] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | all_items | baseline -> quran_26_88_89 | p_reason_motive | 0.1111 | [0.0317, 0.2063] | 8 | 1 | 54 | 0.0391 | 0.0195 |
| Qwen-1.5B-Instruct | all_items | baseline -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | baseline -> quran_26_88_89 | mean_explanation_chars | -3.9365 | [-13.2099, 5.2226] | 26 | 36 | 1 | 0.2529 | 0.9191 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> bhagavad_gita_15_15 | task_a_accuracy | -0.0317 | [-0.1905, 0.1270] | 14 | 16 | 33 | 0.8555 | 0.7077 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> bhagavad_gita_15_15 | task_b_accuracy | -0.0476 | [-0.1111, 0.0000] | 0 | 3 | 60 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> bhagavad_gita_15_15 | heart_sensitivity_score | -0.1304 | [-0.2966, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> bhagavad_gita_15_15 | p_reason_motive | -0.0159 | [-0.0635, 0.0317] | 1 | 2 | 60 | 1.0000 | 0.8750 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> bhagavad_gita_15_15 | mean_explanation_chars | 9.0635 | [-1.1754, 19.1925] | 36 | 27 | 0 | 0.3135 | 0.1568 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> dhammapada_34 | task_a_accuracy | 0.0000 | [-0.1750, 0.1429] | 13 | 13 | 37 | 1.0000 | 0.5775 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> dhammapada_34 | task_b_accuracy | -0.0794 | [-0.1587, -0.0317] | 0 | 5 | 58 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> dhammapada_34 | heart_sensitivity_score | -0.2174 | [-0.4002, -0.0741] | 0 | 5 | 18 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> dhammapada_34 | p_reason_motive | -0.0635 | [-0.1270, -0.0159] | 0 | 4 | 59 | 0.1250 | 1.0000 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> dhammapada_34 | mean_explanation_chars | 0.9683 | [-6.9421, 8.3258] | 33 | 23 | 7 | 0.2288 | 0.1144 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> proverbs_4_23 | task_a_accuracy | 0.0000 | [-0.1591, 0.1591] | 14 | 14 | 35 | 1.0000 | 0.5747 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 63 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> proverbs_4_23 | heart_sensitivity_score | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> proverbs_4_23 | p_reason_motive | 0.0635 | [-0.0159, 0.1429] | 5 | 1 | 57 | 0.2188 | 0.1094 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> proverbs_4_23 | mean_explanation_chars | 2.3492 | [-5.0012, 10.0028] | 28 | 25 | 10 | 0.7838 | 0.3919 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> quran_26_88_89 | task_a_accuracy | -0.0159 | [-0.1750, 0.1429] | 15 | 16 | 32 | 1.0000 | 0.6400 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> quran_26_88_89 | task_b_accuracy | -0.0476 | [-0.1111, 0.0000] | 0 | 3 | 60 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> quran_26_88_89 | heart_sensitivity_score | -0.1304 | [-0.2966, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> quran_26_88_89 | p_reason_motive | 0.0476 | [-0.0476, 0.1429] | 6 | 3 | 54 | 0.5078 | 0.2539 |
| Qwen-1.5B-Instruct | all_items | heart_focused -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | all_items | heart_focused -> quran_26_88_89 | mean_explanation_chars | 3.3492 | [-6.2571, 10.7472] | 32 | 27 | 4 | 0.6029 | 0.3015 |
| Qwen-1.5B-Instruct | heartbench | baseline -> bhagavad_gita_15_15 | task_a_accuracy | -0.0870 | [-0.3913, 0.1750] | 5 | 7 | 11 | 0.7744 | 0.8062 |
| Qwen-1.5B-Instruct | heartbench | baseline -> bhagavad_gita_15_15 | task_b_accuracy | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | heartbench | baseline -> bhagavad_gita_15_15 | heart_sensitivity_score | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | heartbench | baseline -> bhagavad_gita_15_15 | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | heartbench | baseline -> bhagavad_gita_15_15 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> bhagavad_gita_15_15 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> bhagavad_gita_15_15 | mean_explanation_chars | -4.8261 | [-16.0467, 5.6163] | 11 | 12 | 0 | 1.0000 | 0.6612 |
| Qwen-1.5B-Instruct | heartbench | baseline -> dhammapada_34 | task_a_accuracy | 0.0435 | [-0.1739, 0.2609] | 4 | 3 | 16 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | heartbench | baseline -> dhammapada_34 | task_b_accuracy | 0.0000 | [-0.1739, 0.1739] | 2 | 2 | 19 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | heartbench | baseline -> dhammapada_34 | heart_sensitivity_score | 0.0000 | [-0.1739, 0.1739] | 2 | 2 | 19 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | heartbench | baseline -> dhammapada_34 | p_reason_motive | -0.0435 | [-0.1304, 0.0000] | 0 | 1 | 22 | 1.0000 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | baseline -> dhammapada_34 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> dhammapada_34 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> dhammapada_34 | mean_explanation_chars | -12.9565 | [-25.6565, 0.1380] | 6 | 15 | 2 | 0.0784 | 0.9867 |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | task_a_accuracy | 0.0870 | [-0.2174, 0.3913] | 7 | 5 | 11 | 0.7744 | 0.3872 |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | task_b_accuracy | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | heart_sensitivity_score | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | mean_explanation_chars | -2.8696 | [-17.0065, 10.0641] | 12 | 9 | 2 | 0.6636 | 0.3318 |
| Qwen-1.5B-Instruct | heartbench | baseline -> proverbs_4_23 | task_a_accuracy | -0.1304 | [-0.3913, 0.1304] | 3 | 6 | 14 | 0.5078 | 0.9102 |
| Qwen-1.5B-Instruct | heartbench | baseline -> proverbs_4_23 | task_b_accuracy | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | heartbench | baseline -> proverbs_4_23 | heart_sensitivity_score | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | heartbench | baseline -> proverbs_4_23 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | heartbench | baseline -> proverbs_4_23 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> proverbs_4_23 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> proverbs_4_23 | mean_explanation_chars | -8.3043 | [-18.7587, 3.4076] | 5 | 16 | 2 | 0.0266 | 0.9964 |
| Qwen-1.5B-Instruct | heartbench | baseline -> quran_26_88_89 | task_a_accuracy | 0.1304 | [-0.0870, 0.3478] | 5 | 2 | 16 | 0.4531 | 0.2266 |
| Qwen-1.5B-Instruct | heartbench | baseline -> quran_26_88_89 | task_b_accuracy | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | heartbench | baseline -> quran_26_88_89 | heart_sensitivity_score | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | heartbench | baseline -> quran_26_88_89 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | heartbench | baseline -> quran_26_88_89 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> quran_26_88_89 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | baseline -> quran_26_88_89 | mean_explanation_chars | -6.7826 | [-17.7435, 4.6663] | 7 | 15 | 1 | 0.1338 | 0.9738 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> bhagavad_gita_15_15 | task_a_accuracy | -0.1739 | [-0.4793, 0.0880] | 5 | 9 | 9 | 0.4239 | 0.9102 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> bhagavad_gita_15_15 | task_b_accuracy | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> bhagavad_gita_15_15 | heart_sensitivity_score | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> bhagavad_gita_15_15 | p_reason_motive | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> bhagavad_gita_15_15 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> bhagavad_gita_15_15 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> bhagavad_gita_15_15 | mean_explanation_chars | -1.9565 | [-11.6130, 8.2620] | 11 | 12 | 0 | 1.0000 | 0.6612 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> dhammapada_34 | task_a_accuracy | -0.0435 | [-0.3054, 0.2174] | 5 | 6 | 12 | 1.0000 | 0.7256 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> dhammapada_34 | task_b_accuracy | -0.2174 | [-0.3913, -0.0859] | 0 | 5 | 18 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> dhammapada_34 | heart_sensitivity_score | -0.2174 | [-0.3913, -0.0859] | 0 | 5 | 18 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> dhammapada_34 | p_reason_motive | -0.0435 | [-0.1304, 0.0000] | 0 | 1 | 22 | 1.0000 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> dhammapada_34 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> dhammapada_34 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> dhammapada_34 | mean_explanation_chars | -10.0870 | [-20.2196, 0.2337] | 10 | 11 | 2 | 1.0000 | 0.6682 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> proverbs_4_23 | task_a_accuracy | -0.2174 | [-0.4783, 0.0435] | 2 | 7 | 14 | 0.1797 | 0.9805 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> proverbs_4_23 | heart_sensitivity_score | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> proverbs_4_23 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> proverbs_4_23 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> proverbs_4_23 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> proverbs_4_23 | mean_explanation_chars | -5.4348 | [-16.3924, 5.3043] | 9 | 11 | 3 | 0.8238 | 0.7483 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> quran_26_88_89 | task_a_accuracy | 0.0435 | [-0.2174, 0.3043] | 5 | 4 | 14 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> quran_26_88_89 | task_b_accuracy | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> quran_26_88_89 | heart_sensitivity_score | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> quran_26_88_89 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> quran_26_88_89 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> quran_26_88_89 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | heartbench | heart_focused -> quran_26_88_89 | mean_explanation_chars | -3.9130 | [-15.2261, 6.8304] | 10 | 12 | 1 | 0.8318 | 0.7383 |
| Qwen-1.5B-Instruct | moralstories | baseline -> bhagavad_gita_15_15 | task_a_accuracy | 0.0000 | [-0.2250, 0.2500] | 11 | 11 | 18 | 1.0000 | 0.5841 |
| Qwen-1.5B-Instruct | moralstories | baseline -> bhagavad_gita_15_15 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> bhagavad_gita_15_15 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> bhagavad_gita_15_15 | p_reason_motive | 0.0750 | [-0.0500, 0.1750] | 5 | 2 | 33 | 0.4531 | 0.2266 |
| Qwen-1.5B-Instruct | moralstories | baseline -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> bhagavad_gita_15_15 | mean_explanation_chars | 5.5750 | [-6.7525, 17.9013] | 20 | 19 | 1 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | moralstories | baseline -> dhammapada_34 | task_a_accuracy | -0.0250 | [-0.2256, 0.2000] | 9 | 10 | 21 | 1.0000 | 0.6762 |
| Qwen-1.5B-Instruct | moralstories | baseline -> dhammapada_34 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> dhammapada_34 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> dhammapada_34 | p_reason_motive | 0.0250 | [-0.0750, 0.1250] | 3 | 2 | 35 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | moralstories | baseline -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> dhammapada_34 | mean_explanation_chars | -2.5000 | [-13.4081, 7.9550] | 17 | 21 | 2 | 0.6271 | 0.7912 |
| Qwen-1.5B-Instruct | moralstories | baseline -> heart_focused | task_a_accuracy | -0.0500 | [-0.2756, 0.2000] | 11 | 13 | 16 | 0.8388 | 0.7294 |
| Qwen-1.5B-Instruct | moralstories | baseline -> heart_focused | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> heart_focused | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> heart_focused | p_reason_motive | 0.1000 | [0.0000, 0.2000] | 5 | 1 | 34 | 0.2188 | 0.1094 |
| Qwen-1.5B-Instruct | moralstories | baseline -> heart_focused | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> heart_focused | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> heart_focused | mean_explanation_chars | -9.8250 | [-19.3519, -0.2244] | 15 | 24 | 1 | 0.1996 | 0.9459 |
| Qwen-1.5B-Instruct | moralstories | baseline -> proverbs_4_23 | task_a_accuracy | 0.0750 | [-0.1500, 0.3000] | 13 | 10 | 17 | 0.6776 | 0.3388 |
| Qwen-1.5B-Instruct | moralstories | baseline -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> proverbs_4_23 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> proverbs_4_23 | p_reason_motive | 0.1750 | [0.0500, 0.3000] | 7 | 0 | 33 | 0.0156 | 0.0078 |
| Qwen-1.5B-Instruct | moralstories | baseline -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> proverbs_4_23 | mean_explanation_chars | -3.0000 | [-14.9581, 6.5069] | 19 | 20 | 1 | 1.0000 | 0.6254 |
| Qwen-1.5B-Instruct | moralstories | baseline -> quran_26_88_89 | task_a_accuracy | -0.1000 | [-0.3000, 0.1000] | 7 | 11 | 22 | 0.4807 | 0.8811 |
| Qwen-1.5B-Instruct | moralstories | baseline -> quran_26_88_89 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> quran_26_88_89 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> quran_26_88_89 | p_reason_motive | 0.1500 | [0.0250, 0.2750] | 7 | 1 | 32 | 0.0703 | 0.0352 |
| Qwen-1.5B-Instruct | moralstories | baseline -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | baseline -> quran_26_88_89 | mean_explanation_chars | -2.3000 | [-15.9569, 8.9525] | 19 | 21 | 0 | 0.8746 | 0.6821 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> bhagavad_gita_15_15 | task_a_accuracy | 0.0500 | [-0.1250, 0.2250] | 9 | 7 | 24 | 0.8036 | 0.4018 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> bhagavad_gita_15_15 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> bhagavad_gita_15_15 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> bhagavad_gita_15_15 | p_reason_motive | -0.0250 | [-0.1250, 0.0500] | 1 | 2 | 37 | 1.0000 | 0.8750 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> bhagavad_gita_15_15 | mean_explanation_chars | 15.4000 | [2.1156, 28.5275] | 25 | 15 | 0 | 0.1539 | 0.0769 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> dhammapada_34 | task_a_accuracy | 0.0250 | [-0.1506, 0.2250] | 8 | 7 | 25 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> dhammapada_34 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> dhammapada_34 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> dhammapada_34 | p_reason_motive | -0.0750 | [-0.1506, 0.0000] | 0 | 3 | 37 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> dhammapada_34 | mean_explanation_chars | 7.3250 | [-2.0012, 16.3256] | 23 | 12 | 5 | 0.0895 | 0.0448 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> proverbs_4_23 | task_a_accuracy | 0.1250 | [-0.0750, 0.3250] | 12 | 7 | 21 | 0.3593 | 0.1796 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> proverbs_4_23 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> proverbs_4_23 | p_reason_motive | 0.0750 | [-0.0250, 0.2000] | 4 | 1 | 35 | 0.3750 | 0.1875 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> proverbs_4_23 | mean_explanation_chars | 6.8250 | [-2.5762, 15.9300] | 19 | 14 | 7 | 0.4869 | 0.2434 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> quran_26_88_89 | task_a_accuracy | -0.0500 | [-0.2500, 0.2000] | 10 | 12 | 18 | 0.8318 | 0.7383 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> quran_26_88_89 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> quran_26_88_89 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> quran_26_88_89 | p_reason_motive | 0.0500 | [-0.0750, 0.2000] | 5 | 3 | 32 | 0.7266 | 0.3633 |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | moralstories | heart_focused -> quran_26_88_89 | mean_explanation_chars | 7.5250 | [-4.5644, 17.4756] | 22 | 15 | 3 | 0.3240 | 0.1620 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> bhagavad_gita_15_15 | task_a_accuracy | -0.0870 | [-0.3913, 0.1750] | 5 | 7 | 11 | 0.7744 | 0.8062 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> bhagavad_gita_15_15 | task_b_accuracy | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> bhagavad_gita_15_15 | heart_sensitivity_score | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> bhagavad_gita_15_15 | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> bhagavad_gita_15_15 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> bhagavad_gita_15_15 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> bhagavad_gita_15_15 | mean_explanation_chars | -4.8261 | [-16.0467, 5.6163] | 11 | 12 | 0 | 1.0000 | 0.6612 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> dhammapada_34 | task_a_accuracy | 0.0435 | [-0.1739, 0.2609] | 4 | 3 | 16 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> dhammapada_34 | task_b_accuracy | 0.0000 | [-0.1739, 0.1739] | 2 | 2 | 19 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> dhammapada_34 | heart_sensitivity_score | 0.0000 | [-0.1739, 0.1739] | 2 | 2 | 19 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> dhammapada_34 | p_reason_motive | -0.0435 | [-0.1304, 0.0000] | 0 | 1 | 22 | 1.0000 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> dhammapada_34 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> dhammapada_34 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> dhammapada_34 | mean_explanation_chars | -12.9565 | [-25.6565, 0.1380] | 6 | 15 | 2 | 0.0784 | 0.9867 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | task_a_accuracy | 0.0870 | [-0.2174, 0.3913] | 7 | 5 | 11 | 0.7744 | 0.3872 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | task_b_accuracy | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | heart_sensitivity_score | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | mean_explanation_chars | -2.8696 | [-17.0065, 10.0641] | 12 | 9 | 2 | 0.6636 | 0.3318 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> proverbs_4_23 | task_a_accuracy | -0.1304 | [-0.3913, 0.1304] | 3 | 6 | 14 | 0.5078 | 0.9102 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> proverbs_4_23 | task_b_accuracy | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> proverbs_4_23 | heart_sensitivity_score | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> proverbs_4_23 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> proverbs_4_23 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> proverbs_4_23 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> proverbs_4_23 | mean_explanation_chars | -8.3043 | [-18.7587, 3.4076] | 5 | 16 | 2 | 0.0266 | 0.9964 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> quran_26_88_89 | task_a_accuracy | 0.1304 | [-0.0870, 0.3478] | 5 | 2 | 16 | 0.4531 | 0.2266 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> quran_26_88_89 | task_b_accuracy | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> quran_26_88_89 | heart_sensitivity_score | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> quran_26_88_89 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> quran_26_88_89 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> quran_26_88_89 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> quran_26_88_89 | mean_explanation_chars | -6.7826 | [-17.7435, 4.6663] | 7 | 15 | 1 | 0.1338 | 0.9738 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> bhagavad_gita_15_15 | task_a_accuracy | -0.1739 | [-0.4793, 0.0880] | 5 | 9 | 9 | 0.4239 | 0.9102 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> bhagavad_gita_15_15 | task_b_accuracy | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> bhagavad_gita_15_15 | heart_sensitivity_score | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> bhagavad_gita_15_15 | p_reason_motive | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> bhagavad_gita_15_15 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> bhagavad_gita_15_15 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> bhagavad_gita_15_15 | mean_explanation_chars | -1.9565 | [-11.6130, 8.2620] | 11 | 12 | 0 | 1.0000 | 0.6612 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> dhammapada_34 | task_a_accuracy | -0.0435 | [-0.3054, 0.2174] | 5 | 6 | 12 | 1.0000 | 0.7256 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> dhammapada_34 | task_b_accuracy | -0.2174 | [-0.3913, -0.0859] | 0 | 5 | 18 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> dhammapada_34 | heart_sensitivity_score | -0.2174 | [-0.3913, -0.0859] | 0 | 5 | 18 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> dhammapada_34 | p_reason_motive | -0.0435 | [-0.1304, 0.0000] | 0 | 1 | 22 | 1.0000 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> dhammapada_34 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> dhammapada_34 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> dhammapada_34 | mean_explanation_chars | -10.0870 | [-20.2196, 0.2337] | 10 | 11 | 2 | 1.0000 | 0.6682 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> proverbs_4_23 | task_a_accuracy | -0.2174 | [-0.4783, 0.0435] | 2 | 7 | 14 | 0.1797 | 0.9805 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> proverbs_4_23 | heart_sensitivity_score | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> proverbs_4_23 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> proverbs_4_23 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> proverbs_4_23 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> proverbs_4_23 | mean_explanation_chars | -5.4348 | [-16.3924, 5.3043] | 9 | 11 | 3 | 0.8238 | 0.7483 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> quran_26_88_89 | task_a_accuracy | 0.0435 | [-0.2174, 0.3043] | 5 | 4 | 14 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> quran_26_88_89 | task_b_accuracy | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> quran_26_88_89 | heart_sensitivity_score | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> quran_26_88_89 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> quran_26_88_89 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> quran_26_88_89 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | motive_sensitive | heart_focused -> quran_26_88_89 | mean_explanation_chars | -3.9130 | [-15.2261, 6.8304] | 10 | 12 | 1 | 0.8318 | 0.7383 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> bhagavad_gita_15_15 | task_a_accuracy | -0.0870 | [-0.3913, 0.1750] | 5 | 7 | 11 | 0.7744 | 0.8062 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> bhagavad_gita_15_15 | task_b_accuracy | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> bhagavad_gita_15_15 | heart_sensitivity_score | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> bhagavad_gita_15_15 | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> bhagavad_gita_15_15 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> bhagavad_gita_15_15 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> bhagavad_gita_15_15 | mean_explanation_chars | -4.8261 | [-16.0467, 5.6163] | 11 | 12 | 0 | 1.0000 | 0.6612 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> dhammapada_34 | task_a_accuracy | 0.0435 | [-0.1739, 0.2609] | 4 | 3 | 16 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> dhammapada_34 | task_b_accuracy | 0.0000 | [-0.1739, 0.1739] | 2 | 2 | 19 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> dhammapada_34 | heart_sensitivity_score | 0.0000 | [-0.1739, 0.1739] | 2 | 2 | 19 | 1.0000 | 0.6875 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> dhammapada_34 | p_reason_motive | -0.0435 | [-0.1304, 0.0000] | 0 | 1 | 22 | 1.0000 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> dhammapada_34 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> dhammapada_34 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> dhammapada_34 | mean_explanation_chars | -12.9565 | [-25.6565, 0.1380] | 6 | 15 | 2 | 0.0784 | 0.9867 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | task_a_accuracy | 0.0870 | [-0.2174, 0.3913] | 7 | 5 | 11 | 0.7744 | 0.3872 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | task_b_accuracy | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | heart_sensitivity_score | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | p_reason_motive | 0.0000 | [-0.0880, 0.1304] | 1 | 1 | 21 | 1.0000 | 0.7500 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | mean_explanation_chars | -2.8696 | [-17.0065, 10.0641] | 12 | 9 | 2 | 0.6636 | 0.3318 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> proverbs_4_23 | task_a_accuracy | -0.1304 | [-0.3913, 0.1304] | 3 | 6 | 14 | 0.5078 | 0.9102 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> proverbs_4_23 | task_b_accuracy | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> proverbs_4_23 | heart_sensitivity_score | 0.2174 | [0.0435, 0.3913] | 5 | 0 | 18 | 0.0625 | 0.0312 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> proverbs_4_23 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> proverbs_4_23 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> proverbs_4_23 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> proverbs_4_23 | mean_explanation_chars | -8.3043 | [-18.7587, 3.4076] | 5 | 16 | 2 | 0.0266 | 0.9964 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> quran_26_88_89 | task_a_accuracy | 0.1304 | [-0.0870, 0.3478] | 5 | 2 | 16 | 0.4531 | 0.2266 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> quran_26_88_89 | task_b_accuracy | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> quran_26_88_89 | heart_sensitivity_score | 0.0870 | [-0.1304, 0.2609] | 4 | 2 | 17 | 0.6875 | 0.3438 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> quran_26_88_89 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> quran_26_88_89 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> quran_26_88_89 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> quran_26_88_89 | mean_explanation_chars | -6.7826 | [-17.7435, 4.6663] | 7 | 15 | 1 | 0.1338 | 0.9738 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> bhagavad_gita_15_15 | task_a_accuracy | -0.1739 | [-0.4793, 0.0880] | 5 | 9 | 9 | 0.4239 | 0.9102 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> bhagavad_gita_15_15 | task_b_accuracy | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> bhagavad_gita_15_15 | heart_sensitivity_score | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> bhagavad_gita_15_15 | p_reason_motive | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> bhagavad_gita_15_15 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> bhagavad_gita_15_15 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> bhagavad_gita_15_15 | mean_explanation_chars | -1.9565 | [-11.6130, 8.2620] | 11 | 12 | 0 | 1.0000 | 0.6612 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> dhammapada_34 | task_a_accuracy | -0.0435 | [-0.3054, 0.2174] | 5 | 6 | 12 | 1.0000 | 0.7256 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> dhammapada_34 | task_b_accuracy | -0.2174 | [-0.3913, -0.0859] | 0 | 5 | 18 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> dhammapada_34 | heart_sensitivity_score | -0.2174 | [-0.3913, -0.0859] | 0 | 5 | 18 | 0.0625 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> dhammapada_34 | p_reason_motive | -0.0435 | [-0.1304, 0.0000] | 0 | 1 | 22 | 1.0000 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> dhammapada_34 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> dhammapada_34 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> dhammapada_34 | mean_explanation_chars | -10.0870 | [-20.2196, 0.2337] | 10 | 11 | 2 | 1.0000 | 0.6682 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> proverbs_4_23 | task_a_accuracy | -0.2174 | [-0.4783, 0.0435] | 2 | 7 | 14 | 0.1797 | 0.9805 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> proverbs_4_23 | heart_sensitivity_score | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 23 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> proverbs_4_23 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> proverbs_4_23 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> proverbs_4_23 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> proverbs_4_23 | mean_explanation_chars | -5.4348 | [-16.3924, 5.3043] | 9 | 11 | 3 | 0.8238 | 0.7483 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> quran_26_88_89 | task_a_accuracy | 0.0435 | [-0.2174, 0.3043] | 5 | 4 | 14 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> quran_26_88_89 | task_b_accuracy | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> quran_26_88_89 | heart_sensitivity_score | -0.1304 | [-0.3043, 0.0000] | 0 | 3 | 20 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> quran_26_88_89 | p_reason_motive | 0.0435 | [0.0000, 0.1304] | 1 | 0 | 22 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> quran_26_88_89 | same_heart_control_accuracy | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> quran_26_88_89 | heart_overreach_rate | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_act_different_motive | heart_focused -> quran_26_88_89 | mean_explanation_chars | -3.9130 | [-15.2261, 6.8304] | 10 | 12 | 1 | 0.8318 | 0.7383 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> bhagavad_gita_15_15 | task_a_accuracy | 0.0000 | [-0.2250, 0.2500] | 11 | 11 | 18 | 1.0000 | 0.5841 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> bhagavad_gita_15_15 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> bhagavad_gita_15_15 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> bhagavad_gita_15_15 | p_reason_motive | 0.0750 | [-0.0500, 0.1750] | 5 | 2 | 33 | 0.4531 | 0.2266 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> bhagavad_gita_15_15 | mean_explanation_chars | 5.5750 | [-6.7525, 17.9013] | 20 | 19 | 1 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> dhammapada_34 | task_a_accuracy | -0.0250 | [-0.2256, 0.2000] | 9 | 10 | 21 | 1.0000 | 0.6762 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> dhammapada_34 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> dhammapada_34 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> dhammapada_34 | p_reason_motive | 0.0250 | [-0.0750, 0.1250] | 3 | 2 | 35 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> dhammapada_34 | mean_explanation_chars | -2.5000 | [-13.4081, 7.9550] | 17 | 21 | 2 | 0.6271 | 0.7912 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | task_a_accuracy | -0.0500 | [-0.2756, 0.2000] | 11 | 13 | 16 | 0.8388 | 0.7294 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | p_reason_motive | 0.1000 | [0.0000, 0.2000] | 5 | 1 | 34 | 0.2188 | 0.1094 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | mean_explanation_chars | -9.8250 | [-19.3519, -0.2244] | 15 | 24 | 1 | 0.1996 | 0.9459 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> proverbs_4_23 | task_a_accuracy | 0.0750 | [-0.1500, 0.3000] | 13 | 10 | 17 | 0.6776 | 0.3388 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> proverbs_4_23 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> proverbs_4_23 | p_reason_motive | 0.1750 | [0.0500, 0.3000] | 7 | 0 | 33 | 0.0156 | 0.0078 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> proverbs_4_23 | mean_explanation_chars | -3.0000 | [-14.9581, 6.5069] | 19 | 20 | 1 | 1.0000 | 0.6254 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> quran_26_88_89 | task_a_accuracy | -0.1000 | [-0.3000, 0.1000] | 7 | 11 | 22 | 0.4807 | 0.8811 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> quran_26_88_89 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> quran_26_88_89 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> quran_26_88_89 | p_reason_motive | 0.1500 | [0.0250, 0.2750] | 7 | 1 | 32 | 0.0703 | 0.0352 |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> quran_26_88_89 | mean_explanation_chars | -2.3000 | [-15.9569, 8.9525] | 19 | 21 | 0 | 0.8746 | 0.6821 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> bhagavad_gita_15_15 | task_a_accuracy | 0.0500 | [-0.1250, 0.2250] | 9 | 7 | 24 | 0.8036 | 0.4018 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> bhagavad_gita_15_15 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> bhagavad_gita_15_15 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> bhagavad_gita_15_15 | p_reason_motive | -0.0250 | [-0.1250, 0.0500] | 1 | 2 | 37 | 1.0000 | 0.8750 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> bhagavad_gita_15_15 | mean_explanation_chars | 15.4000 | [2.1156, 28.5275] | 25 | 15 | 0 | 0.1539 | 0.0769 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> dhammapada_34 | task_a_accuracy | 0.0250 | [-0.1506, 0.2250] | 8 | 7 | 25 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> dhammapada_34 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> dhammapada_34 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> dhammapada_34 | p_reason_motive | -0.0750 | [-0.1506, 0.0000] | 0 | 3 | 37 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> dhammapada_34 | mean_explanation_chars | 7.3250 | [-2.0012, 16.3256] | 23 | 12 | 5 | 0.0895 | 0.0448 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> proverbs_4_23 | task_a_accuracy | 0.1250 | [-0.0750, 0.3250] | 12 | 7 | 21 | 0.3593 | 0.1796 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> proverbs_4_23 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> proverbs_4_23 | p_reason_motive | 0.0750 | [-0.0250, 0.2000] | 4 | 1 | 35 | 0.3750 | 0.1875 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> proverbs_4_23 | mean_explanation_chars | 6.8250 | [-2.5762, 15.9300] | 19 | 14 | 7 | 0.4869 | 0.2434 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> quran_26_88_89 | task_a_accuracy | -0.0500 | [-0.2500, 0.2000] | 10 | 12 | 18 | 0.8318 | 0.7383 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> quran_26_88_89 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> quran_26_88_89 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> quran_26_88_89 | p_reason_motive | 0.0500 | [-0.0750, 0.2000] | 5 | 3 | 32 | 0.7266 | 0.3633 |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_heart_controls | heart_focused -> quran_26_88_89 | mean_explanation_chars | 7.5250 | [-4.5644, 17.4756] | 22 | 15 | 3 | 0.3240 | 0.1620 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> bhagavad_gita_15_15 | task_a_accuracy | 0.0000 | [-0.2250, 0.2500] | 11 | 11 | 18 | 1.0000 | 0.5841 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> bhagavad_gita_15_15 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> bhagavad_gita_15_15 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> bhagavad_gita_15_15 | p_reason_motive | 0.0750 | [-0.0500, 0.1750] | 5 | 2 | 33 | 0.4531 | 0.2266 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> bhagavad_gita_15_15 | mean_explanation_chars | 5.5750 | [-6.7525, 17.9013] | 20 | 19 | 1 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> dhammapada_34 | task_a_accuracy | -0.0250 | [-0.2256, 0.2000] | 9 | 10 | 21 | 1.0000 | 0.6762 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> dhammapada_34 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> dhammapada_34 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> dhammapada_34 | p_reason_motive | 0.0250 | [-0.0750, 0.1250] | 3 | 2 | 35 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> dhammapada_34 | mean_explanation_chars | -2.5000 | [-13.4081, 7.9550] | 17 | 21 | 2 | 0.6271 | 0.7912 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | task_a_accuracy | -0.0500 | [-0.2756, 0.2000] | 11 | 13 | 16 | 0.8388 | 0.7294 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | p_reason_motive | 0.1000 | [0.0000, 0.2000] | 5 | 1 | 34 | 0.2188 | 0.1094 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | mean_explanation_chars | -9.8250 | [-19.3519, -0.2244] | 15 | 24 | 1 | 0.1996 | 0.9459 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> proverbs_4_23 | task_a_accuracy | 0.0750 | [-0.1500, 0.3000] | 13 | 10 | 17 | 0.6776 | 0.3388 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> proverbs_4_23 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> proverbs_4_23 | p_reason_motive | 0.1750 | [0.0500, 0.3000] | 7 | 0 | 33 | 0.0156 | 0.0078 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> proverbs_4_23 | mean_explanation_chars | -3.0000 | [-14.9581, 6.5069] | 19 | 20 | 1 | 1.0000 | 0.6254 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> quran_26_88_89 | task_a_accuracy | -0.1000 | [-0.3000, 0.1000] | 7 | 11 | 22 | 0.4807 | 0.8811 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> quran_26_88_89 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> quran_26_88_89 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> quran_26_88_89 | p_reason_motive | 0.1500 | [0.0250, 0.2750] | 7 | 1 | 32 | 0.0703 | 0.0352 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> quran_26_88_89 | mean_explanation_chars | -2.3000 | [-15.9569, 8.9525] | 19 | 21 | 0 | 0.8746 | 0.6821 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> bhagavad_gita_15_15 | task_a_accuracy | 0.0500 | [-0.1250, 0.2250] | 9 | 7 | 24 | 0.8036 | 0.4018 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> bhagavad_gita_15_15 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> bhagavad_gita_15_15 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> bhagavad_gita_15_15 | p_reason_motive | -0.0250 | [-0.1250, 0.0500] | 1 | 2 | 37 | 1.0000 | 0.8750 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> bhagavad_gita_15_15 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> bhagavad_gita_15_15 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> bhagavad_gita_15_15 | mean_explanation_chars | 15.4000 | [2.1156, 28.5275] | 25 | 15 | 0 | 0.1539 | 0.0769 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> dhammapada_34 | task_a_accuracy | 0.0250 | [-0.1506, 0.2250] | 8 | 7 | 25 | 1.0000 | 0.5000 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> dhammapada_34 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> dhammapada_34 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> dhammapada_34 | p_reason_motive | -0.0750 | [-0.1506, 0.0000] | 0 | 3 | 37 | 0.2500 | 1.0000 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> dhammapada_34 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> dhammapada_34 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> dhammapada_34 | mean_explanation_chars | 7.3250 | [-2.0012, 16.3256] | 23 | 12 | 5 | 0.0895 | 0.0448 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> proverbs_4_23 | task_a_accuracy | 0.1250 | [-0.0750, 0.3250] | 12 | 7 | 21 | 0.3593 | 0.1796 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> proverbs_4_23 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> proverbs_4_23 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> proverbs_4_23 | p_reason_motive | 0.0750 | [-0.0250, 0.2000] | 4 | 1 | 35 | 0.3750 | 0.1875 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> proverbs_4_23 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> proverbs_4_23 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> proverbs_4_23 | mean_explanation_chars | 6.8250 | [-2.5762, 15.9300] | 19 | 14 | 7 | 0.4869 | 0.2434 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> quran_26_88_89 | task_a_accuracy | -0.0500 | [-0.2500, 0.2000] | 10 | 12 | 18 | 0.8318 | 0.7383 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> quran_26_88_89 | task_b_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> quran_26_88_89 | heart_sensitivity_score | - | [-, -] | 0 | 0 | 0 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> quran_26_88_89 | p_reason_motive | 0.0500 | [-0.0750, 0.2000] | 5 | 3 | 32 | 0.7266 | 0.3633 |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> quran_26_88_89 | same_heart_control_accuracy | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> quran_26_88_89 | heart_overreach_rate | 0.0000 | [0.0000, 0.0000] | 0 | 0 | 40 | - | - |
| Qwen-1.5B-Instruct | same_intention_controls | heart_focused -> quran_26_88_89 | mean_explanation_chars | 7.5250 | [-4.5644, 17.4756] | 22 | 15 | 3 | 0.3240 | 0.1620 |

## Power Planning

Directional sign-test power uses alpha=0.05 and target power=0.80.

| Model | Slice | Contrast | Metric | Pairs | Better | Worse | Tie | Current power | Min N for target power |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | heart_sensitivity_score | 23 | 5 | 0 | 18 | 0.5813 | 30 |
| Qwen-1.5B-Instruct | heartbench | baseline -> heart_focused | p_reason_motive | 23 | 1 | 1 | 21 | 0.0012 | - |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | heart_sensitivity_score | 23 | 5 | 0 | 18 | 0.5813 | 30 |
| Qwen-1.5B-Instruct | motive_sensitive | baseline -> heart_focused | p_reason_motive | 23 | 1 | 1 | 21 | 0.0012 | - |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | heart_sensitivity_score | 23 | 5 | 0 | 18 | 0.5813 | 30 |
| Qwen-1.5B-Instruct | same_act_different_motive | baseline -> heart_focused | p_reason_motive | 23 | 1 | 1 | 21 | 0.0012 | - |
| Qwen-1.5B-Instruct | same_heart_controls | baseline -> heart_focused | p_reason_motive | 40 | 5 | 1 | 34 | 0.3106 | 100 |
| Qwen-1.5B-Instruct | same_intention_controls | baseline -> heart_focused | p_reason_motive | 40 | 5 | 1 | 34 | 0.3106 | 100 |
