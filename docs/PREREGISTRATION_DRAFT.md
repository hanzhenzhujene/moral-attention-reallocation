# Preregistration Draft

Internal naming note:
This draft uses raw condition ids such as `baseline` and `heart_focused` where exact implementation names matter.
In the public-facing README and paper, these appear as `Baseline` and `Heart-focused`.

## Title

Moral Attention Reallocation under Framing Conditions in Language Models

## Main Question

Does heart-focused framing change what LLMs treat as morally diagnostic, especially under conditions where outward behavior is held constant and inward motive varies?

## Primary Hypotheses

### H1

heart-focused framing increases Heart-Sensitivity Score relative to baseline.

### H2

heart-focused framing increases `P(reason = motive)` relative to baseline.

### H3

heart-focused framing decreases Surface-Overweighting Index relative to baseline.

### H4

If heart-focused framing and secular matched framing produce similar improvements, the main mechanism is semantic reorientation rather than uniquely sacred authority.

## Primary Contrasts

- `baseline -> heart_focused`
- `baseline -> secular_matched`
- `heart_focused -> secular_matched`

All reported deltas are right-minus-left.

## Inclusion Criteria

- Items must be pairwise and textually interpretable on their own.
- For the MVP, items must be marked as included in the frozen benchmark file.
- Each model-condition pair must contain at most one run record per item.

## Exclusion Criteria

- malformed JSON outputs
- duplicated run records for the same model, condition, and item
- items discovered after freezing to violate structural invariants

## Primary Metrics

- Heart-Sensitivity Score
- Surface-Overweighting Index
- `P(reason = motive)`
- Cross-Task Consistency

## Secondary Metrics

- Task A accuracy
- Task B accuracy
- mean explanation length
- run-level position-bias diagnostics

## Uncertainty Estimation

- 95% bootstrap confidence intervals within model-condition groups
- paired bootstrap deltas on shared item sets for condition comparisons

## Interpretation Boundaries

- Improvements in response length or moralizing tone alone do not count as improvements in moral attention.
- A null heart-focused-vs-secular contrast is still theoretically informative if both differ from baseline in the same direction.
- Strong claims about general moral improvement require evidence beyond motive-sensitive subsets.
