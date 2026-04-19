# Project Status And Next Steps

## Current Position

The repo now supports one narrow public claim and one broader exploratory supplement.

- **Public claim**: on the 63-item `Qwen-1.5B-Instruct` confirmation slice, the `heart_focused` condition directionally improves inward-motive judgment without increasing same-heart overreach.
- **Exploratory supplement**: on the same 63-item slice, `heart_focused` and `Proverbs 4:23` tie for the strongest motive-sensitive gain in a 6-condition family, while all 6 conditions preserve same-heart controls and show clean paired-order stability.

## What Is Solid Now

- The benchmark logic is coherent:
  - same-act / different-motive pairs test motive sensitivity
  - same-heart controls prevent fake wins from over-imputing bad hearts
- The public confirmation slice is reproducible and honest about scope:
  - `Task A` stays flat
  - `Task B` and `heart_sensitivity_score` improve
  - same-heart control accuracy stays `1.0`
  - heart overreach stays `0.0`
  - explanation length does not inflate
- The later paired-order follow-up materially improved interpretation:
  - on the same `23` same-act items, `baseline` and `heart_focused` both show `0.0` item-level Task B order flips
  - the remaining limitation on this slice is now best understood as **power**, not same-item order instability
- The exploratory 6-condition extension is now methodologically much cleaner than a one-off prompt tweak:
  - pilot completed
  - pilot paired-order completed
  - targeted 63-item `Qwen-1.5B-Instruct` confirmation completed
  - confirmation paired-order completed

## What Is Not Finished Yet

- The public result is still directional rather than decisive under conservative paired testing.
- The full 160-item main benchmark is not yet frozen.
- The transformed Moral Stories main set is not yet fully double-annotated and adjudicated.
- The 6-condition extension is not yet a cross-model claim.
- The repo is a strong pre-freeze artifact, not yet a final paper submission package with a frozen main benchmark and preprint.

## Recommended Next Steps

### 1. Power up the canonical same-act slice first

This is the highest-value next move.

- Add roughly `15` to `21` more clean `same_act_different_motive` items.
- Keep the existing `40` same-heart controls fixed.
- Re-run the canonical `baseline` vs `heart_focused` confirmation before broadening the story further.

Why this comes first:

- the current public slice already has clean guardrails
- paired-order on the same items now looks clean
- the remaining bottleneck is statistical power on the motive-sensitive target items

### 2. Freeze the transformed benchmark properly

- Finish the `candidate -> ready for second annotator -> adjudicated main` workflow
- add a second annotator pass
- promote only stable transformed items into the main benchmark

Why this comes second:

- it upgrades the project from a strong confirmation artifact to a real frozen benchmark contribution

### 3. Re-run the main public comparison on both Qwen models after the stronger slice is ready

- use the expanded motive-sensitive slice
- keep the current guardrail controls unchanged
- keep prompt wording and decoding frozen during this phase

Goal:

- learn whether the main effect survives a cleaner, better-powered slice across the two already-scaffolded models

### 4. Use the 6-condition family as a secondary robustness layer, not the primary headline

After the stronger public slice is ready:

- rerun the 6-condition family on the strengthened confirmation slice
- compare each anchor to `baseline`
- summarize whether multiple anchored variants move in the same direction without hurting controls

Why this should stay secondary:

- it is a compelling robustness story
- but the project still needs a stronger primary mechanistic result before broadening the headline

### 5. Only then launch the full 160-item main benchmark

Launch criteria:

- transformed main items are double-annotated and adjudicated
- public slice is better powered
- prompts, decoding, schema, and metrics are frozen
- release gates are green

## Recommended Public Framing Right Now

Use this sentence as the safest current summary:

> On a clean same-act confirmation slice, heart-focused framing directionally improves inward-motive judgment without increasing same-heart overreach; the current limitation is power, not guardrail failure.

Use this sentence for the exploratory supplement:

> In a broader six-condition extension on the same slice, the strongest motive-sensitive gain is reproduced by both the heart-focused prompt and a Proverbs 4:23 anchor, while all six conditions preserve same-heart controls and show clean paired-order stability.

## Canonical Files

- Public readout: [`results/main_same_act_confirmation_v12_mps/confirmation_readout.md`](../results/main_same_act_confirmation_v12_mps/confirmation_readout.md)
- Public paired-order follow-up: [`results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md`](../results/main_same_act_confirmation_v12_mps/confirmation_paired_order_followup.md)
- Exploratory readout: [`results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md`](../results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_readout.md)
- Public figure: [`assets/confirmation-comparison-bars.svg`](../assets/confirmation-comparison-bars.svg)
- Exploratory figure: [`assets/text-anchor-confirmation-qwen15.svg`](../assets/text-anchor-confirmation-qwen15.svg)
- Paper draft: [`paper/main.tex`](../paper/main.tex)
