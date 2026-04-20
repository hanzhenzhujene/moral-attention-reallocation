#!/usr/bin/env bash
set -euo pipefail

# Historical live pilot runner for the six-condition text-anchor family.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${ROOT_DIR}/results/pilot_live_text_anchor_v1_mps}"
JOBS_PATH="${ROOT_DIR}/results/text_anchor_pilot_v1_jobs.jsonl"
STUDY_CONFIG="${ROOT_DIR}/configs/text_anchor_study_v1.json"
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

CONTRASTS=(
  baseline:heart_focused
  baseline:proverbs_4_23
  baseline:dhammapada_34
  baseline:bhagavad_gita_15_15
  baseline:quran_26_88_89
  heart_focused:proverbs_4_23
  heart_focused:dhammapada_34
  heart_focused:bhagavad_gita_15_15
  heart_focused:quran_26_88_89
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

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/build_prompt_jobs.py" \
  --items "${ROOT_DIR}/data/study/paper_first_pilot_v1.json" \
  --conditions "${CONDITIONS[@]}" \
  --output "${JOBS_PATH}" \
  --prompt-dir "${ROOT_DIR}/prompts"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/report_prompt_diagnostics.py" \
  --prompt-dir "${ROOT_DIR}/prompts/pilot_v12" \
  --conditions "${CONDITIONS[@]}" \
  --model-id "Qwen/Qwen2.5-1.5B-Instruct" \
  --output-json "${OUTPUT_DIR}/prompt_diagnostics.json" \
  --output-md "${OUTPUT_DIR}/prompt_diagnostics.md"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_transformers_multipass.py" \
  --config "${ROOT_DIR}/configs/pilot_execution_text_anchor_v1_mps.json" \
  --model-alias Qwen-0.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_0_5b_text_anchor_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_0_5b_text_anchor_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_0_5b_text_anchor_trace.jsonl"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_transformers_multipass.py" \
  --config "${ROOT_DIR}/configs/pilot_execution_text_anchor_v1_mps.json" \
  --model-alias Qwen-1.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_1_5b_text_anchor_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_1_5b_text_anchor_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_1_5b_text_anchor_trace.jsonl"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_diagnostics.py" \
  --input \
  "${OUTPUT_DIR}/qwen_0_5b_text_anchor_runs.jsonl" \
  "${OUTPUT_DIR}/qwen_1_5b_text_anchor_runs.jsonl" \
  --output "${OUTPUT_DIR}/pilot_run_diagnostics.json"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/evaluate_runs.py" \
  --input \
  "${OUTPUT_DIR}/qwen_0_5b_text_anchor_runs.jsonl" \
  "${OUTPUT_DIR}/qwen_1_5b_text_anchor_runs.jsonl" \
  --bootstrap-samples 1000 \
  --contrasts "${CONTRASTS[@]}" \
  --output "${OUTPUT_DIR}/pilot_summary.json"

if ! "${PYTHON_BIN}" "${ROOT_DIR}/scripts/evaluate_pilot_health.py" \
  --config "${STUDY_CONFIG}" \
  --jobs "${JOBS_PATH}" \
  --runs \
  "${OUTPUT_DIR}/qwen_0_5b_text_anchor_runs.jsonl" \
  "${OUTPUT_DIR}/qwen_1_5b_text_anchor_runs.jsonl" \
  --models Qwen-0.5B-Instruct Qwen-1.5B-Instruct \
  --output "${OUTPUT_DIR}/pilot_health.json"; then
  echo "Pilot health thresholds were not fully met; exploratory outputs were still written." >&2
fi

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/evaluate_robustness_report.py" \
  --input \
  "${OUTPUT_DIR}/qwen_0_5b_text_anchor_runs.jsonl" \
  "${OUTPUT_DIR}/qwen_1_5b_text_anchor_runs.jsonl" \
  --bootstrap-samples 400 \
  --contrasts "${CONTRASTS[@]}" \
  --output-json "${OUTPUT_DIR}/pilot_robustness.json" \
  --output-md "${OUTPUT_DIR}/pilot_robustness.md"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/analyze_task_b_swap_gap.py" \
  --input \
  "${OUTPUT_DIR}/qwen_0_5b_text_anchor_runs.jsonl" \
  "${OUTPUT_DIR}/qwen_1_5b_text_anchor_runs.jsonl" \
  --bucket-mode pair_type \
  --output-json "${OUTPUT_DIR}/pilot_swap_gap_by_pair_type.json" \
  --output-md "${OUTPUT_DIR}/pilot_swap_gap_by_pair_type.md"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/summarize_text_anchor_family.py" \
  --summary "${OUTPUT_DIR}/pilot_summary.json" \
  --output-json "${OUTPUT_DIR}/pilot_text_anchor_family.json" \
  --output-md "${OUTPUT_DIR}/pilot_text_anchor_family.md"

echo "Detected device: ${DEVICE}"
echo "Wrote text-anchor pilot artifact to ${OUTPUT_DIR}"
