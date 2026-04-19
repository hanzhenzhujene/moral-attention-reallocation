# Text-Anchor Family Summary

## Qwen-1.5B-Instruct

| Condition | vs baseline Task B | vs baseline HSS | vs heart-focused HSS | Same-heart stable | Overreach non-increase |
| --- | ---: | ---: | ---: | --- | --- |
| Proverbs 4:23 | 0.0794 | 0.2173 | 0.0 | True | True |
| Dhammapada 34 | 0.0 | 0.0 | -0.2173 | True | True |
| Bhagavad Gita 15.15 | 0.0317 | 0.0869 | -0.1304 | True | True |
| Qur'an 26:88-89 | 0.0317 | 0.0869 | -0.1304 | True | True |

| Family mean delta vs baseline | Task B | HSS | P(reason=motive) | Same-heart control | Overreach |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean | 0.0357 | 0.0978 | 0.0714 | 0.0 | 0.0 |

- supportive text anchors: `3`
- non-increased overreach anchors: `4`
- stable same-heart anchors: `4`
