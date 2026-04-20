#!/usr/bin/env bash
set -euo pipefail

# Run the public paired-order diagnostic for the 6-condition cross-tradition confirmation slice.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${ROOT_DIR}/results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps}"
JOBS_PATH="${OUTPUT_DIR}/text_anchor_confirmation_paired_order_jobs.jsonl"
PYTHON_BIN="${ROOT_DIR}/.venv/bin/python"
TMP_CONFIG="$(mktemp "${TMPDIR:-/tmp}/text_anchor_confirmation_paired_order_config.XXXXXX.json")"

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

"${PYTHON_BIN}" - <<'PY' "${ROOT_DIR}" "${TMP_CONFIG}" "${OUTPUT_DIR}"
import json
import sys
from pathlib import Path

root_dir = Path(sys.argv[1]).resolve()
tmp_config = Path(sys.argv[2]).resolve()
output_dir = Path(sys.argv[3]).resolve()

config = {
    "name": "text_anchor_confirmation_paired_order_v1_qwen15b",
    "benchmark_path": str(root_dir / "data/study/paper_first_main_same_act_confirmation_v0.json"),
    "jobs_path": str(output_dir / "text_anchor_confirmation_paired_order_jobs.jsonl"),
    "prompt_dir": str(root_dir / "prompts/pilot_v12"),
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

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/build_paired_order_jobs.py" \
  --items "${ROOT_DIR}/data/study/paper_first_main_same_act_confirmation_v0.json" \
  --conditions "${CONDITIONS[@]}" \
  --pair-types same_act_different_motive \
  --output "${JOBS_PATH}" \
  --prompt-dir "${ROOT_DIR}/prompts"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run_transformers_multipass.py" \
  --config "${TMP_CONFIG}" \
  --jobs "${JOBS_PATH}" \
  --model-alias Qwen-1.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_1_5b_paired_order_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_1_5b_paired_order_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_1_5b_paired_order_trace.jsonl"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/analyze_paired_order_stability.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_paired_order_runs.jsonl" \
  --output-json "${OUTPUT_DIR}/paired_order_stability.json" \
  --output-md "${OUTPUT_DIR}/paired_order_stability.md"

echo "Detected device: ${DEVICE}"
echo "Wrote confirmation paired-order diagnostic to ${OUTPUT_DIR}"
