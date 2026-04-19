# Religious Text Anchors and Moral Attention Reallocation in Language Models

![Release](https://img.shields.io/github/v/release/hanzhenzhujene/moral-attention-reallocation?style=flat-square)
![Status](https://img.shields.io/badge/status-pre--freeze%20confirmation%20artifact-0f766e?style=flat-square)
![Public Scope](https://img.shields.io/badge/public%20scope-Qwen--1.5B%20confirmation%20slice-12805c?style=flat-square)
![License](https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square)
[![Paper PDF](https://img.shields.io/badge/paper-LaTeX%20PDF-b45309?style=flat-square)](paper/main.pdf)

> This repo studies whether generic heart-focused framing and cross-tradition religious text anchors change what an LLM treats as morally diagnostic. The strongest public claim remains narrow: on a clean same-act confirmation slice, heart-focused framing directionally improves inward-motive judgment without increasing same-heart overreach.

## Artifact Index

| Paper | Figures | Tables | Results | Release |
| --- | --- | --- | --- | --- |
| [PDF](paper/main.pdf) · [LaTeX](paper/main.tex) | [Project overview](assets/text-anchor-confirmation-qwen15.svg) · [Frozen release](assets/confirmation-comparison-bars.svg) | [Cross-tradition matrix](docs/tables/text_anchor_confirmation_tables.md) | [Frozen readout](results/main_same_act_confirmation_v12_mps/confirmation_readout.md) · [Paired-order](results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md) · [6-condition readout](results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md) | [v0.1-confirmation](https://github.com/hanzhenzhujene/moral-attention-reallocation/releases/tag/v0.1-confirmation) |

| Narrative | Status | Reproduce | Environment |
| --- | --- | --- | --- |
| [Working paper note](docs/WORKING_PAPER.md) | [Status and next steps](docs/STATUS_AND_NEXT_STEPS.md) | [Root Makefile](Makefile) | [requirements.txt](requirements.txt) · [environment.yml](environment.yml) |

## Overview

This project asks a mechanistic question about moral reasoning in language models:
when an LLM reads a moral case, what does it treat as morally diagnostic?

Instead of asking whether a religious framing makes a model "more moral" overall, the benchmark asks whether framing reallocates moral attention across:

- outward act
- inward motive
- consequence
- rule

The repo exposes two linked artifact layers:

- a broader **project-level cross-tradition readout** on one 63-item confirmation slice
- a narrower **frozen public release artifact** used for the strongest release-grade claim

The six-condition project-level readout uses:

- `Baseline`
- `Heart-focused`
- `Proverbs 4:23` from the Biblical Jewish/Christian tradition
- `Dhammapada 34` from the Buddhist tradition
- `Bhagavad Gita 15.15` from the Hindu tradition
- `Qur'an 26:88-89` from the Islamic tradition

All four religion-labeled conditions reuse the same generic heart-focused scaffold and add one frozen study-paraphrased text anchor keyed to the cited passage.

![Cross-tradition project overview figure for the 63-item confirmation slice](assets/text-anchor-confirmation-qwen15.svg)

This figure is the repo's canonical project overview. It shows the broader six-condition readout; it is not the same thing as the narrower frozen release claim.

## Main Result At A Glance

### Project-Level Cross-Tradition Readout

Current scope:

- model: `Qwen-1.5B-Instruct`
- slice: `63` items
- composition: `23` same-act motive pairs + `40` same-heart controls

Headline pattern:

- `Heart-focused` and `Proverbs 4:23` tie for the strongest motive-sensitive improvement
- `Bhagavad Gita 15.15` and `Qur'an 26:88-89` are smaller positive shifts
- `Dhammapada 34` is effectively null on this slice
- all six conditions preserve same-heart control accuracy at `1.0` and heart overreach at `0.0`
- the paired-order follow-up shows `0.0` item-level Task B order flips across all six conditions

| Condition | Tradition / frame | Task A | Task B | Task C = motive | HSS | Same-heart | Overreach | Read |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Baseline | No religious text | `0.5079` | `0.8889` | `0.4127` | `0.6957` | `1.0` | `0.0` | Reference condition |
| Heart-focused | Generic scaffold | `0.5079` | `0.9683` | `0.4762` | `0.9130` | `1.0` | `0.0` | Strongest tie |
| Proverbs 4:23 | Biblical (Jewish/Christian) | `0.5079` | `0.9683` | `0.5397` | `0.9130` | `1.0` | `0.0` | Strongest tie |
| Dhammapada 34 | Buddhist | `0.5079` | `0.8889` | `0.4127` | `0.6957` | `1.0` | `0.0` | Null on this slice |
| Bhagavad Gita 15.15 | Hindu | `0.4762` | `0.9206` | `0.4603` | `0.7826` | `1.0` | `0.0` | Smaller positive shift |
| Qur'an 26:88-89 | Islamic | `0.4921` | `0.9206` | `0.5238` | `0.7826` | `1.0` | `0.0` | Smaller positive shift |

Reading note:

- identical percentages here reflect identical discrete counts on a small slice, not a rendering bug

### Frozen Public Release Claim

The strongest public claim remains narrower than the six-condition readout above.
The release artifact compares `Baseline` vs `Heart-focused` only.

![Frozen public release figure for baseline vs heart-focused](assets/confirmation-comparison-bars.svg)

| Metric | Baseline | Heart-focused | Delta | Read |
| --- | ---: | ---: | ---: | --- |
| Task A accuracy | `0.5079` | `0.5079` | `+0.0000` | Top-line verdict stays flat |
| Task B accuracy | `0.8889` | `0.9524` | `+0.0635` | Inward-orientation judgment improves |
| Heart-sensitivity score | `0.6957` | `0.8696` | `+0.1739` | Stronger motive sensitivity on the frozen release slice |
| `P(reason = motive)` | `0.4127` | `0.4762` | `+0.0635` | Reason focus shifts toward motive |
| Same-heart control accuracy | `1.0` | `1.0` | `+0.0` | Guardrail remains perfect |
| Heart overreach rate | `0.0` | `0.0` | `+0.0` | No false projection increase |
| Mean explanation chars | `111.54` | `109.16` | `-2.38` | No verbosity inflation |

Boundary note:

- on the `23` same-act motive pairs, the exact sign test gives one-sided `p = 0.0625` and two-sided `p = 0.125`
- the later paired-order follow-up shows `0.0` item-level Task B order flips for both `Baseline` and `Heart-focused`
- the release artifact is therefore best described as **directional confirmation**, not a definitive final result

## Benchmark Design

The benchmark is designed to separate motive sensitivity from indiscriminate heart projection.

### Item Types

| Item type | What stays fixed | What changes | Why it matters |
| --- | --- | --- | --- |
| Same-act / different-motive pairs | outward act | inward motive | tests whether framing increases motive sensitivity |
| Same-heart controls | inward orientation | outward surface | prevents fake wins from over-imputing bad hearts |

Stylized same-act example:

| Case A | Case B |
| --- | --- |
| A student offers help mainly to look generous in public. | The same student offers the same help out of sincere concern. |

### Tasks

| Task | Plain-language question | Role |
| --- | --- | --- |
| Task A | Which case is more morally problematic overall? | top-line verdict |
| Task B | Which case reveals a worse inward orientation? | core mechanistic target |
| Task C | Is the judgment mainly driven by outward act, motive, consequence, or rule? | explanation-focus diagnostic |

Implementation note:

- the released artifacts are inference-only; no model is trained or fine-tuned in this repo
- `Task A` and `Task C` are prompted on the full case pair
- `Task B` is run through a separate multi-pass intention-only pipeline using `prompts/pilot_v12`
- the released configs use `task_b_copy_mode=benchmark_summary` and `task_b_order_mode=canonical_source`

## Claim Boundary

| Scope | What we can claim | What we cannot yet claim |
| --- | --- | --- |
| Frozen public release artifact | `Heart-focused` directionally improves inward-motive judgment on a clean confirmation slice without increasing same-heart overreach | that heart-focused framing improves moral reasoning overall |
| Project-level 6-condition readout | motive-sensitive movement is not confined to one wording; the strongest slice-level gain is reproduced by both `Heart-focused` and `Proverbs 4:23` | that one religious text anchor is decisively best across models or benchmarks |
| Overall repository status | the current public artifact is honest, reproducible, and mechanically interpretable | that the full 160-item benchmark is frozen and final |

## Complete 6-Condition Matrix

Canonical table artifact: [docs/tables/text_anchor_confirmation_tables.md](docs/tables/text_anchor_confirmation_tables.md)

CSV export: [docs/tables/condition_metric_matrix.csv](docs/tables/condition_metric_matrix.csv)

How to read the matrix:

- each column is one prompt condition
- values are proportions from `0` to `1` unless the row says `chars`
- higher is better for Task A, Task B, Task C motive-focus rate, HSS, same-heart control accuracy, and paired-order Task B accuracy
- lower is better for heart overreach, order-flip rate, and paired-order Task B gap

Metric guide:

| Metric | What it means |
| --- | --- |
| Task A accuracy | How often the model picks the more morally problematic case overall. |
| Task B accuracy | How often the model picks the case with the worse inward motive or heart posture. |
| Task C motive-focus rate | How often the model says motive is the main reason for its Task A judgment. |
| HSS | Heart-sensitivity score on the 23 same-act / different-motive pairs. This is the main motive-sensitive metric. |
| Same-heart control accuracy | How often the model correctly preserves matched inward orientation on guardrail items. |
| Heart overreach rate | How often the model falsely projects a worse inward heart onto same-heart controls. |
| Paired-order Task B accuracy | Task B accuracy when the same 23 same-act items are rerun in both A/B orders. |

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

Two quick reading notes:

- `Bhagavad Gita 15.15` and `Qur'an 26:88-89` both score `58/63` on Task B and `18/23` on HSS
- `Heart-focused` and `Proverbs 4:23` both score `61/63` on Task B and `21/23` on HSS

## Reproduce

This public repo guarantees reproduction of the current `Qwen-1.5B-Instruct` confirmation slice, not the full benchmark-construction workflow. Third-party raw benchmark mirrors are intentionally not vendored here.

Tested public runtime:

- `Python 3.11`
- `torch 2.11.0`
- `transformers 5.5.4`
- `numpy 2.4.4`
- `safetensors 0.7.0`
- `matplotlib 3.10.8`

Reproduce the frozen public release artifact:

```bash
make setup
make reproduce-confirmation
```

Expected outputs:

- `results/reproduction_confirmation/confirmation_summary.json`
- `results/reproduction_confirmation/confirmation_health.json`
- `results/reproduction_confirmation/confirmation_robustness.md`
- `results/reproduction_confirmation/confirmation_readout.md`
- `results/reproduction_confirmation/confirmation_comparison_bars.svg`
- `results/reproduction_confirmation/confirmation_overview.svg`

Optional later paired-order follow-up:

```bash
make reproduce-paired-order
```

Cross-tradition artifact reproduction:

```bash
make reproduce-text-anchor
make reproduce-text-anchor-paired-order
```

## Repository Map

- `assets/`: figures used on the project page
- `paper/`: LaTeX manuscript and compiled paper PDF
- `Makefile`: one-command public setup, reproduction, and paper rebuild targets
- `docs/WORKING_PAPER.md`: paper-style summary of the public artifact
- `docs/STATUS_AND_NEXT_STEPS.md`: current state, blockers, and recommended next experiments
- `configs/`: execution configs for the public confirmation artifact and internal study configs
- `results/main_same_act_confirmation_v12_mps/`: canonical public result files for the current strongest narrow claim
- `results/main_same_act_text_anchor_v1_qwen15b_mps/`: project-level 6-condition confirmation artifact
- `scripts/reproduce_confirmation_slice.sh`: minimal reproduction entry point
- `scripts/reproduce_confirmation_paired_order_followup.sh`: optional same-item paired-order reproduction for the later public follow-up
- `scripts/run_text_anchor_confirmation_qwen15b.sh`: cross-tradition 6-condition confirmation runner
- `scripts/run_text_anchor_confirmation_paired_order_qwen15b.sh`: paired-order stability runner for the 6-condition confirmation slice
- `docs/RUNBOOK.md`: internal full-pipeline runbook for benchmark construction and broader experiments
- `docs/ANNOTATION_PROTOCOL.md`: annotation rules for Task A, Task B, and Task C
- `docs/archive/`: archived planning and scoping notes from the earlier workspace phase

<details>
<summary>Method Details And Internal Diagnostics</summary>

- [Same-act confirmation readout](results/main_same_act_confirmation_v12_mps/confirmation_readout.md)
- [Public paired-order follow-up](results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md)
- [Robustness report](results/main_same_act_confirmation_v12_mps/confirmation_robustness.md)
- [Swap-gap breakdown](results/main_same_act_confirmation_v12_mps/confirmation_swap_gap_by_pair_type.md)
- [Cross-tradition 6-condition confirmation readout](results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md)
- [Cross-tradition confirmation paired-order stability](results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.md)
- [Annotation protocol](docs/ANNOTATION_PROTOCOL.md)
- [Internal runbook](docs/RUNBOOK.md)
- [Task B revision log](docs/TASK_B_REVISION_LOG.md)
- [Preregistration draft](docs/PREREGISTRATION_DRAFT.md)
- [Working paper note on the cross-tradition readout](docs/WORKING_PAPER.md)

</details>

## Citation

Use the GitHub release artifact for citation when referencing this repository:

- Working paper draft: [docs/WORKING_PAPER.md](docs/WORKING_PAPER.md)
- Paper PDF: [paper/main.pdf](paper/main.pdf)
- Paper source: [paper/main.tex](paper/main.tex)
- Release: [v0.1-confirmation](https://github.com/hanzhenzhujene/moral-attention-reallocation/releases/tag/v0.1-confirmation)
- Citation metadata: [CITATION.cff](CITATION.cff)
- Preprint: no public preprint is linked yet

```bibtex
@software{zhu_2026_moral_attention_reallocation,
  author = {Zhu, Hanzhen},
  title = {Religious Text Anchors and Moral Attention Reallocation in Language Models},
  year = {2026},
  version = {v0.1-confirmation},
  url = {https://github.com/hanzhenzhujene/moral-attention-reallocation},
  note = {Pre-freeze confirmation artifact}
}
```
