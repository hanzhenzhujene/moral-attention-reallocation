# Working Paper Draft

Formal LaTeX paper:

- PDF: [paper/main.pdf](../paper/main.pdf)
- Source: [paper/main.tex](../paper/main.tex)

## Title

Moral Attention Reallocation in Language Models

## Subtitle

heart-focused framing as a probe of motive sensitivity rather than a general claim of moral improvement

## Abstract

This project studies a mechanistic question about moral cognition in language models: when an LLM reads a moral case, what does it treat as morally diagnostic? Rather than asking whether a religious prompt makes a model "more moral" overall, the benchmark asks whether framing changes the model's attention across outward act, inward motive, consequence, and rule. The public artifact focuses on a clean confirmation slice built from `same_act_different_motive` items plus `same-heart` guardrail controls. On the current `Qwen-1.5B-Instruct` confirmation slice, a heart-focused condition improves `Task B` inward-orientation judgment from `0.8889` to `0.9524`, raises heart-sensitivity score from `0.6957` to `0.8696`, and increases `P(reason = motive)` from `0.4127` to `0.4762`, while same-heart control accuracy remains `1.0` and heart overreach remains `0.0`. Under conservative paired testing this is a directional confirmation result, not yet a freeze-grade decisive result. A later paired-order follow-up on the same `23` same-act items found `0.0` item-level Task B order flips for both `baseline` and `heart_focused`, so the main remaining limitation on this slice is power rather than same-item order instability.

## Research Question

The project asks:

- Does framing change what an LLM treats as morally diagnostic?
- When outward behavior is held fixed, does a heart-focused framing make the model more sensitive to inward motive?
- Can that happen without increasing false projection of "bad hearts" onto outwardly harsher but inwardly matched cases?

## Benchmark Logic

The core design uses two complementary item types.

### 1. Same-Act / Different-Motive Pairs

These hold outward behavior fixed while changing the written motive. They test whether a model notices that the same act can express different inward orientations.

Example logic:

- Case A: helps another person out of genuine care
- Case B: performs the same helpful act for vanity or self-display

### 2. Same-Heart Controls

These hold inward orientation fixed while varying outward surface. They prevent artificial gains from models that simply map harsher outward behavior onto worse heart judgments.

## Tasks

Each item is evaluated with three task layers.

- `Task A`: overall moral verdict
- `Task B`: inward-orientation judgment
- `Task C`: reason focus (`outward_act`, `motive`, `consequence`, `rule`)

The public confirmation claim centers on `Task B` and heart-sensitivity, with `Task C` used as support and same-heart controls used as guardrails.

## Public Confirmation Slice

The current public artifact is intentionally narrow.

- Model: `Qwen-1.5B-Instruct`
- Conditions: `baseline`, `heart_focused`
- Slice size: `63` items
- Composition: `23` same-act motive pairs + `40` same-heart controls
- Decoding: `temperature=0`, `top_p=1.0`, `max_new_tokens=120`

## Main Public Results

| Metric | Baseline | heart-focused | Delta | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Task A accuracy | `0.5079` | `0.5079` | `+0.0000` | Top-line verdict stayed flat |
| Task B accuracy | `0.8889` | `0.9524` | `+0.0635` | Inward-orientation judgment improved |
| Heart-sensitivity score | `0.6957` | `0.8696` | `+0.1739` | Core mechanistic target improved |
| `P(reason = motive)` | `0.4127` | `0.4762` | `+0.0635` | Explanation focus shifted toward motive |
| Same-heart control accuracy | `1.0` | `1.0` | `+0.0` | Guardrail stayed perfect |
| Heart overreach rate | `0.0` | `0.0` | `+0.0` | No false projection increase |
| Mean explanation chars | `111.54` | `109.16` | `-2.38` | No verbosity inflation |

## Significance Note

On the `23` same-act motive pairs:

- paired sign counts: `4` better, `0` worse, `19` ties
- one-sided exact sign test: `p = 0.0625`
- two-sided exact sign test: `p = 0.125`

This supports a directional confirmation claim rather than a final decisive paper claim.

Later follow-up:

- paired-order Task B order flips on the same `23` same-act items: `0.0`
- paired-order Task B gap for `baseline`: `0.0`
- paired-order Task B gap for `heart_focused`: `0.0`

## Interpretation

The strongest current interpretation is:

> heart-focused framing may reallocate moral attention toward inward motive on a clean confirmation slice, without increasing same-heart overreach.

What the public artifact does support:

- a cleaner motive-sensitive reading under the heart-focused condition
- stable same-heart guardrails
- a shift in reason focus consistent with motive sensitivity

What it does not yet support:

- a general claim that heart-focused prompting improves moral reasoning overall
- a freeze-grade final result for the full benchmark
- a uniquely heart-focused effect, as opposed to a broader semantic reorientation, without the matched secular comparison in the canonical public slice

## Artifact Boundaries

This repository is a publication-style research artifact, but it is still pre-freeze.

Frozen and public now:

- the `Qwen-1.5B-Instruct` confirmation slice
- canonical run outputs in `results/main_same_act_confirmation_v12_mps/`
- the current overview figures and reproduction path
- a paired-order follow-up on the same same-act slice for `baseline` and `heart_focused`

Not yet frozen:

- the full `160`-item main benchmark
- a fully double-annotated transformed Moral Stories main set
- a final order-robust `Task B` method across all targeted cells

## Exploratory Extension: 6-Condition Text Anchors

The repo now also contains a broader exploratory extension that is **not** part of the frozen public claim. This extension keeps the same benchmark logic but expands the prompt family to six conditions:

- `baseline`
- `heart_focused`
- `proverbs_4_23`
- `dhammapada_34`
- `bhagavad_gita_15_15`
- `quran_26_88_89`

The goal is not to claim that one anchor "wins." It is to test whether multiple text-anchored variants move motive-sensitive metrics in a common direction while preserving same-heart guardrails.

Current status:

- Full 20-item pilot completed: `240` valid records, `0.0` parse failures.
- Pilot paired-order diagnostic completed: `288` valid records with `0.0` item-level Task B order flips on the held-out same-act pilot slice.
- A targeted 63-item `Qwen-1.5B-Instruct` exploratory confirmation has now been completed: `378` valid records, `0.0` parse failures.
- Same-heart control accuracy stayed `1.0` in all six confirmation conditions.
- Heart overreach stayed `0.0` in all six confirmation conditions.
- `heart_focused` and `Proverbs 4:23` tie for the strongest confirmation result:
  - `Task B`: `0.8889 -> 0.9683`
  - `HSS`: `0.6957 -> 0.9130`
  - same-act exact sign test for HSS: one-sided `p = 0.03125`, two-sided `p = 0.0625`
- `Bhagavad Gita 15.15` and `Qur'an 26:88-89` remain directionally positive but smaller:
  - `Task B`: `0.8889 -> 0.9206`
  - `HSS`: `0.6957 -> 0.7826`
- `Dhammapada 34` is effectively null on this confirmation slice.

The key follow-up diagnostics are now in the repo:

- Pilot stage report: [`results/pilot_live_text_anchor_v1_mps/text_anchor_stage_report.md`](../results/pilot_live_text_anchor_v1_mps/text_anchor_stage_report.md)
- Pilot paired-order stability: [`results/pilot_paired_order_text_anchor_same_act_v1_mps/paired_order_stability.md`](../results/pilot_paired_order_text_anchor_same_act_v1_mps/paired_order_stability.md)
- Confirmation readout: [`results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md`](../results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md)
- Confirmation family summary: [`results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_text_anchor_family.md`](../results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_text_anchor_family.md)
- Confirmation paired-order stability: [`results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.md`](../results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.md)
- Confirmation figure: [`assets/text-anchor-confirmation-qwen15.svg`](../assets/text-anchor-confirmation-qwen15.svg)

That confirmation paired-order pack matters because it shows `0.0` item-level Task B order flips and `0.0` paired-order Task B gaps across all six conditions on the 23 same-act confirmation items. So the large split-based swap-gap seen in some aggregate confirmation summaries should not be read as same-item order instability on that slice.

Interpretation:

- the extension is now a substantially stronger exploratory family result on `Qwen-1.5B-Instruct`
- it is strongest for `heart_focused` and `Proverbs 4:23`
- it still is not a freeze-grade cross-model result, because the pilot remained heterogeneous across models
- it should not replace the narrower public confirmation claim in the README or paper title yet

## Figures And Readouts

- Main comparison figure: [`assets/confirmation-comparison-bars.svg`](../assets/confirmation-comparison-bars.svg)
- Overview figure: [`assets/same-act-confirmation-overview.svg`](../assets/same-act-confirmation-overview.svg)
- Metric scoreboard: [`assets/confirmation-metric-scoreboard.svg`](../assets/confirmation-metric-scoreboard.svg)
- Exploratory text-anchor confirmation figure: [`assets/text-anchor-confirmation-qwen15.svg`](../assets/text-anchor-confirmation-qwen15.svg)
- Readout: [`results/main_same_act_confirmation_v12_mps/confirmation_readout.md`](../results/main_same_act_confirmation_v12_mps/confirmation_readout.md)
- Public paired-order follow-up: [`results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md`](../results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md)
- Robustness report: [`results/main_same_act_confirmation_v12_mps/confirmation_robustness.md`](../results/main_same_act_confirmation_v12_mps/confirmation_robustness.md)

## Reproduction

The public entry point is:

```bash
bash scripts/reproduce_confirmation_slice.sh results/reproduction_confirmation
```

This script now creates a portable local config and auto-selects `cuda`, `mps`, or `cpu`, so it is not tied to the original development machine.

Optional paired-order follow-up:

```bash
bash scripts/reproduce_confirmation_paired_order_followup.sh results/reproduction_confirmation_paired_order
```
