# Working Paper Draft

Formal LaTeX paper:

- PDF: [paper/main.pdf](../paper/main.pdf)
- Source: [paper/main.tex](../paper/main.tex)

## Title

Religious Text Anchors and Moral Attention Reallocation in Language Models

## Subtitle

heart-focused and cross-tradition framing as probes of motive sensitivity rather than a general claim of moral improvement

## Abstract

This project studies a mechanistic question about moral cognition in language models: when an LLM reads a moral case, what does it treat as morally diagnostic? Rather than asking whether a religious prompt makes a model "more moral" overall, the benchmark asks whether framing changes the model's attention across outward act, inward motive, consequence, and rule. The broader project includes a generic heart-focused scaffold plus four frozen study-paraphrased cross-tradition text anchors keyed to cited passages: `Proverbs 4:23` from the Biblical Jewish/Christian tradition, `Dhammapada 34` from the Buddhist tradition, `Bhagavad Gita 15.15` from the Hindu tradition, and `Qur'an 26:88-89` from the Islamic tradition. The repo therefore has two linked layers: a project-level six-condition cross-tradition readout, and a narrower frozen release artifact. On the current `Qwen-1.5B-Instruct` confirmation slice, `Heart-focused` and `Proverbs 4:23` tie for the strongest motive-sensitive result, `Bhagavad Gita 15.15` and `Qur'an 26:88-89` are smaller positive shifts, and `Dhammapada 34` is null on this slice; all six conditions preserve same-heart controls and keep heart overreach at `0.0`. The frozen release artifact remains narrower: `Baseline` vs `Heart-focused` improves `Task B` from `0.8889` to `0.9524`, raises heart-sensitivity from `0.6957` to `0.8696`, and leaves same-heart guardrails intact. Under conservative paired testing that release result is directional rather than decisive, and the later paired-order follow-up suggests the remaining limitation is power rather than same-item order instability.

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

The frozen release claim centers on `Task B` and heart-sensitivity, with `Task C` used as support and same-heart controls used as guardrails.

## Implementation Notes

- The released artifacts are prompting-only inference runs; no model training or fine-tuning is performed in this repo.
- The shared runtime is `scripts/run_transformers_multipass.py` with the `prompts/pilot_v12` prompt package.
- `Task A` and `Task C` are answered from the two full case texts.
- In the released configs, `Task B` uses `task_b_copy_mode=benchmark_summary`, so the intention-only comparison is built from the benchmark `motive_summary` strings rather than a model-generated copy pass.
- A relation gate first checks whether the two intention texts express the same or different inward orientation; only `different` items proceed to the final inward-orientation choice.
- The four religion-labeled conditions reuse the same generic heart-focused scaffold and append one frozen study-paraphrased anchor block keyed to the cited passage.

## Frozen Public Release Artifact

The current public artifact is intentionally narrow.

- Model: `Qwen-1.5B-Instruct`
- Conditions: `Baseline`, `Heart-focused`
- Slice size: `63` items
- Composition: `23` same-act motive pairs + `40` same-heart controls
- Decoding: `temperature=0`, `top_p=1.0`, `max_new_tokens=120`

## Frozen Release Results

| Metric | Baseline | Heart-focused | Delta | Interpretation |
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
- paired-order Task B gap for `Baseline`: `0.0`
- paired-order Task B gap for `Heart-focused`: `0.0`

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
- a paired-order follow-up on the same same-act slice for `Baseline` and `Heart-focused`

Not yet frozen:

- the full `160`-item main benchmark
- a fully double-annotated transformed Moral Stories main set
- a final order-robust `Task B` method across all targeted cells

## Project-Level Cross-Tradition Readout

The repo also contains a broader project-level cross-tradition readout that is **not** part of the frozen release claim. This readout keeps the same benchmark logic but expands the prompt family to six conditions:

- `Baseline`
- `Heart-focused`
- `proverbs_4_23`
- `dhammapada_34`
- `bhagavad_gita_15_15`
- `quran_26_88_89`

The goal is not to claim that one anchor "wins." It is to test whether multiple text-anchored variants move motive-sensitive metrics in a common direction while preserving same-heart guardrails.
Because this six-condition readout is a later rerun rather than the frozen release package, its point estimates differ slightly from the narrower release artifact even on the same 63-item slice.

Current status:

- Full 20-item pilot completed: `240` valid records, `0.0` parse failures.
- Pilot paired-order diagnostic completed: `288` valid records with `0.0` item-level Task B order flips on the held-out same-act pilot slice.
- A targeted 63-item `Qwen-1.5B-Instruct` cross-tradition confirmation has now been completed: `378` valid records, `0.0` parse failures.
- Same-heart control accuracy stayed `1.0` in all six confirmation conditions.
- Heart overreach stayed `0.0` in all six confirmation conditions.
- `Heart-focused` and `Proverbs 4:23` tie for the strongest confirmation result:
  - `Task B`: `0.8889 -> 0.9683`
  - `HSS`: `0.6957 -> 0.9130`
  - same-act exact sign test for HSS: one-sided `p = 0.03125`, two-sided `p = 0.0625`
- `Bhagavad Gita 15.15` and `Qur'an 26:88-89` remain directionally positive but smaller:
  - `Task B`: `0.8889 -> 0.9206`
  - `HSS`: `0.6957 -> 0.7826`
- `Dhammapada 34` is effectively null on this confirmation slice.

The key follow-up diagnostics are now in the repo:

- Confirmation readout: [`results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md`](../results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md)
- Confirmation family summary: [`results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_text_anchor_family.md`](../results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_text_anchor_family.md)
- Confirmation paired-order stability: [`results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.md`](../results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.md)
- Confirmation figure: [`assets/text-anchor-confirmation-qwen15.svg`](../assets/text-anchor-confirmation-qwen15.svg)

That confirmation paired-order pack matters because it shows `0.0` item-level Task B order flips and `0.0` paired-order Task B gaps across all six conditions on the 23 same-act confirmation items. So the large split-based swap-gap seen in some aggregate confirmation summaries should not be read as same-item order instability on that slice.

Interpretation:

- the six-condition readout is now a substantially stronger project-level family result on `Qwen-1.5B-Instruct`
- it is strongest for `Heart-focused` and `Proverbs 4:23`
- it still is not a freeze-grade cross-model result, because the pilot remained heterogeneous across models
- it should not replace the narrower public confirmation claim in the README or paper title yet

## Figures And Readouts

- Frozen release figure: [`assets/confirmation-comparison-bars.svg`](../assets/confirmation-comparison-bars.svg)
- Project overview figure: [`assets/text-anchor-confirmation-qwen15.svg`](../assets/text-anchor-confirmation-qwen15.svg)
- Readout: [`results/main_same_act_confirmation_v12_mps/confirmation_readout.md`](../results/main_same_act_confirmation_v12_mps/confirmation_readout.md)
- Public paired-order follow-up: [`results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md`](../results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md)
- Robustness report: [`results/main_same_act_confirmation_v12_mps/confirmation_robustness.md`](../results/main_same_act_confirmation_v12_mps/confirmation_robustness.md)

## Reproduction

The public entry point is:

```bash
make setup
make reproduce-confirmation
```

This target creates a portable local config and auto-selects `cuda`, `mps`, or `cpu`, so it is not tied to the original development machine.

Optional paired-order follow-up:

```bash
make reproduce-paired-order
```
