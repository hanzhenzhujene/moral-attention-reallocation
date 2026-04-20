#!/usr/bin/env bash
set -euo pipefail

# Historical pilot paired-order diagnostic for the six-condition text-anchor family.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${ROOT_DIR}/results/pilot_paired_order_text_anchor_same_act_v1_mps}"
JOBS_PATH="${ROOT_DIR}/results/text_anchor_paired_order_same_act_v1_jobs.jsonl"
PYTHON_BIN="${ROOT_DIR}/.venv/bin/python"

if [[ ! -x "${PYTHON_BIN}" ]]; then
  PYTHON_BIN="python3"
fi

CONDITIONS=(
  baseline
  heart_focused
  proverbs_4_23
  dhammapada_34
  bhagavad_gita_15_15
  quran_26_88_89
)

mkdir -p "${OUTPUT_DIR}"

if "${PYTHON_BIN}" - <<'PY' >/dev/null 2>&1
import torch
raise SystemExit(0 if torch.cuda.is_available() else 1)
PY
then
  DEVICE="cuda"
elif "${PYTHON_BIN}" - <<'PY' >/dev/null 2>&1
import torch
has_mps = hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
raise SystemExit(0 if has_mps else 1)
PY
then
  DEVICE="mps"
else
  DEVICE="cpu"
fi

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/build_paired_order_jobs.py" \
  --items "${ROOT_DIR}/data/study/paper_first_pilot_v1.json" \
  --conditions "${CONDITIONS[@]}" \
  --pair-types same_act_different_motive \
  --output "${JOBS_PATH}" \
  --prompt-dir "${ROOT_DIR}/prompts"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_transformers_multipass.py" \
  --config "${ROOT_DIR}/configs/pilot_execution_text_anchor_v1_mps.json" \
  --jobs "${JOBS_PATH}" \
  --model-alias Qwen-0.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_0_5b_paired_order_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_0_5b_paired_order_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_0_5b_paired_order_trace.jsonl"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_transformers_multipass.py" \
  --config "${ROOT_DIR}/configs/pilot_execution_text_anchor_v1_mps.json" \
  --jobs "${JOBS_PATH}" \
  --model-alias Qwen-1.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_1_5b_paired_order_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_1_5b_paired_order_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_1_5b_paired_order_trace.jsonl"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/analyze_paired_order_stability.py" \
  --input \
  "${OUTPUT_DIR}/qwen_0_5b_paired_order_runs.jsonl" \
  "${OUTPUT_DIR}/qwen_1_5b_paired_order_runs.jsonl" \
  --output-json "${OUTPUT_DIR}/paired_order_stability.json" \
  --output-md "${OUTPUT_DIR}/paired_order_stability.md"

echo "Detected device: ${DEVICE}"
echo "Wrote paired-order diagnostic to ${OUTPUT_DIR}"
