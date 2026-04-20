#!/usr/bin/env bash
set -euo pipefail

# Run the public 6-condition cross-tradition confirmation artifact for Qwen-1.5B-Instruct.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${ROOT_DIR}/results/main_same_act_text_anchor_v1_qwen15b_mps}"
JOBS_PATH="${OUTPUT_DIR}/text_anchor_confirmation_jobs.jsonl"
STUDY_CONFIG="${ROOT_DIR}/project/configs/text_anchor_study_v1.json"
BENCHMARK_PATH="${ROOT_DIR}/data/study/paper_first_main_same_act_confirmation_v0.json"
PYTHON_BIN="${ROOT_DIR}/.venv/bin/python"
TMP_CONFIG="$(mktemp "${TMPDIR:-/tmp}/text_anchor_confirmation_config.XXXXXX.json")"

cleanup() {
  rm -f "${TMP_CONFIG}"
}
trap cleanup EXIT

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

OUTPUT_DISPLAY_DIR="$("${PYTHON_BIN}" - <<'PY' "${ROOT_DIR}" "${OUTPUT_DIR}"
import sys
from pathlib import Path

root_dir = Path(sys.argv[1]).resolve()
output_dir = Path(sys.argv[2]).resolve()
try:
    print(output_dir.relative_to(root_dir).as_posix())
except ValueError:
    print(output_dir.as_posix())
PY
)"

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

"${PYTHON_BIN}" - <<'PY' "${ROOT_DIR}" "${TMP_CONFIG}" "${OUTPUT_DIR}"
import json
import sys
from pathlib import Path

root_dir = Path(sys.argv[1]).resolve()
tmp_config = Path(sys.argv[2]).resolve()
output_dir = Path(sys.argv[3]).resolve()

config = {
    "name": "text_anchor_confirmation_v1_qwen15b",
    "study_config_path": str(root_dir / "project/configs/text_anchor_study_v1.json"),
    "benchmark_path": str(root_dir / "data/study/paper_first_main_same_act_confirmation_v0.json"),
    "jobs_path": str(output_dir / "text_anchor_confirmation_jobs.jsonl"),
    "prompt_dir": str(root_dir / "project/prompts/pilot_v12"),
    "task_b_copy_mode": "benchmark_summary",
    "task_b_order_mode": "canonical_source",
    "conditions": [
        "baseline",
        "heart_focused",
        "proverbs_4_23",
        "dhammapada_34",
        "bhagavad_gita_15_15",
        "quran_26_88_89",
    ],
    "models": [
        {
            "alias": "Qwen-1.5B-Instruct",
            "hf_model_id": "Qwen/Qwen2.5-1.5B-Instruct",
        }
    ],
    "inference": {
        "prompt_mode": "chat",
        "temperature": 0.0,
        "top_p": 1.0,
        "n": 1,
        "max_new_tokens": 120,
        "max_attempts": 2,
        "device": "auto",
        "dtype": "auto",
    },
    "outputs": {
        "run_dir": str(output_dir),
    },
}

tmp_config.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
PY

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/validate_benchmark.py" \
  "${BENCHMARK_PATH}"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/audit_benchmark.py" \
  "${BENCHMARK_PATH}" \
  --output "${OUTPUT_DIR}/confirmation_benchmark_audit.json"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/build_prompt_jobs.py" \
  --items "${BENCHMARK_PATH}" \
  --conditions "${CONDITIONS[@]}" \
  --output "${JOBS_PATH}" \
  --prompt-dir "${ROOT_DIR}/project/prompts"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/check_job_balance.py" \
  --input "${JOBS_PATH}" \
  --output "${OUTPUT_DIR}/confirmation_job_balance.json"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/write_pilot_freeze_manifest.py" \
  --execution-config "${TMP_CONFIG}" \
  --study-config "${STUDY_CONFIG}" \
  --benchmark "${BENCHMARK_PATH}" \
  --jobs "${JOBS_PATH}" \
  --run-schema "${ROOT_DIR}/project/schemas/run_record.schema.json" \
  --response-schema "${ROOT_DIR}/project/schemas/model_response.schema.json" \
  --output "${OUTPUT_DIR}/confirmation_freeze_manifest.json"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/report_prompt_diagnostics.py" \
  --prompt-dir "${ROOT_DIR}/project/prompts/pilot_v12" \
  --conditions "${CONDITIONS[@]}" \
  --model-id "Qwen/Qwen2.5-1.5B-Instruct" \
  --output-json "${OUTPUT_DIR}/prompt_diagnostics.json" \
  --output-md "${OUTPUT_DIR}/prompt_diagnostics.md"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_transformers_multipass.py" \
  --config "${TMP_CONFIG}" \
  --model-alias Qwen-1.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_trace.jsonl"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_diagnostics.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_runs.jsonl" \
  --output "${OUTPUT_DIR}/confirmation_run_diagnostics.json"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/evaluate_runs.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_runs.jsonl" \
  --bootstrap-samples 1000 \
  --contrasts "${CONTRASTS[@]}" \
  --output "${OUTPUT_DIR}/confirmation_summary.json"

if ! "${PYTHON_BIN}" "${ROOT_DIR}/scripts/evaluate_pilot_health.py" \
  --config "${STUDY_CONFIG}" \
  --jobs "${JOBS_PATH}" \
  --runs "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_runs.jsonl" \
  --models Qwen-1.5B-Instruct \
  --output "${OUTPUT_DIR}/confirmation_health.json"; then
  echo "Confirmation health thresholds were not fully met; exploratory outputs were still written." >&2
fi

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/evaluate_robustness_report.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_runs.jsonl" \
  --bootstrap-samples 400 \
  --contrasts "${CONTRASTS[@]}" \
  --output-json "${OUTPUT_DIR}/confirmation_robustness.json" \
  --output-md "${OUTPUT_DIR}/confirmation_robustness.md"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/analyze_task_b_swap_gap.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_text_anchor_confirmation_runs.jsonl" \
  --bucket-mode pair_type \
  --output-json "${OUTPUT_DIR}/confirmation_swap_gap_by_pair_type.json" \
  --output-md "${OUTPUT_DIR}/confirmation_swap_gap_by_pair_type.md"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/summarize_text_anchor_family.py" \
  --summary "${OUTPUT_DIR}/confirmation_summary.json" \
  --output-json "${OUTPUT_DIR}/confirmation_text_anchor_family.json" \
  --output-md "${OUTPUT_DIR}/confirmation_text_anchor_family.md"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/render_text_anchor_confirmation_report.py" \
  --summary "${OUTPUT_DIR}/confirmation_summary.json" \
  --robustness "${OUTPUT_DIR}/confirmation_robustness.json" \
  --health "${OUTPUT_DIR}/confirmation_health.json" \
  --family-summary "${OUTPUT_DIR}/confirmation_text_anchor_family.json" \
  --model "Qwen-1.5B-Instruct" \
  --benchmark-name "paper_first_main_same_act_confirmation_v0" \
  --slice-composition "23 same_act_different_motive + 40 same-heart controls" \
  --summary-path "${OUTPUT_DISPLAY_DIR}/confirmation_summary.json" \
  --robustness-path "${OUTPUT_DISPLAY_DIR}/confirmation_robustness.json" \
  --family-path "${OUTPUT_DISPLAY_DIR}/confirmation_text_anchor_family.json" \
  --health-path "${OUTPUT_DISPLAY_DIR}/confirmation_health.json" \
  --output-json "${OUTPUT_DIR}/confirmation_readout.json" \
  --output-md "${OUTPUT_DIR}/confirmation_readout.md"

echo "Detected device: ${DEVICE}"
echo "Wrote exploratory text-anchor confirmation artifact to ${OUTPUT_DIR}"
