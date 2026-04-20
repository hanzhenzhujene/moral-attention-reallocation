#!/usr/bin/env bash
set -euo pipefail

# Reproduce the public paired-order follow-up on the same-act confirmation slice.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${ROOT_DIR}/results/reproduction_confirmation_paired_order}"
TMP_CONFIG="$(mktemp "${TMPDIR:-/tmp}/confirmation_paired_order_config.XXXXXX.json")"
TMP_JOBS="$(mktemp "${TMPDIR:-/tmp}/confirmation_paired_order_jobs.XXXXXX.jsonl")"

cleanup() {
  rm -f "${TMP_CONFIG}" "${TMP_JOBS}"
}
trap cleanup EXIT

mkdir -p "${OUTPUT_DIR}"

if python3 - <<'PY' >/dev/null 2>&1; then
import torch
raise SystemExit(0 if torch.cuda.is_available() else 1)
PY
  DEVICE="cuda"
elif python3 - <<'PY' >/dev/null 2>&1; then
import torch
has_mps = hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
raise SystemExit(0 if has_mps else 1)
PY
  DEVICE="mps"
else
  DEVICE="cpu"
fi

python3 "${ROOT_DIR}/scripts/build_paired_order_jobs.py" \
  --items "${ROOT_DIR}/data/study/paper_first_main_same_act_confirmation_v0.json" \
  --conditions baseline heart_focused \
  --pair-types same_act_different_motive \
  --prompt-dir "${ROOT_DIR}/prompts/pilot_v12" \
  --output "${TMP_JOBS}"

python3 - <<'PY' "${ROOT_DIR}" "${TMP_CONFIG}" "${OUTPUT_DIR}" "${TMP_JOBS}"
import json
import sys
from pathlib import Path

root_dir = Path(sys.argv[1]).resolve()
tmp_config = Path(sys.argv[2]).resolve()
output_dir = Path(sys.argv[3]).resolve()
jobs_path = Path(sys.argv[4]).resolve()

config = {
    "name": "public_confirmation_paired_order_reproduction",
    "benchmark_path": str(root_dir / "data/study/paper_first_main_same_act_confirmation_v0.json"),
    "jobs_path": str(jobs_path),
    "prompt_dir": str(root_dir / "prompts/pilot_v12"),
    "task_b_copy_mode": "benchmark_summary",
    "task_b_order_mode": "canonical_source",
    "conditions": ["baseline", "heart_focused"],
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

python3 "${ROOT_DIR}/scripts/run_transformers_multipass.py" \
  --config "${TMP_CONFIG}" \
  --jobs "${TMP_JOBS}" \
  --model-alias Qwen-1.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_1_5b_paired_order_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_1_5b_paired_order_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_1_5b_paired_order_trace.jsonl"

python3 "${ROOT_DIR}/scripts/analyze_paired_order_stability.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_paired_order_runs.jsonl" \
  --output-json "${OUTPUT_DIR}/paired_order_stability.json" \
  --output-md "${OUTPUT_DIR}/paired_order_stability.md"

python3 "${ROOT_DIR}/scripts/render_public_paired_order_followup.py" \
  --paired-order "${OUTPUT_DIR}/paired_order_stability.json" \
  --model "Qwen-1.5B-Instruct" \
  --source-path "${OUTPUT_DIR}/paired_order_stability.json" \
  --output-json "${OUTPUT_DIR}/confirmation_paired_order_followup.json" \
  --output-md "${OUTPUT_DIR}/confirmation_paired_order_followup.md"

echo "Detected device: ${DEVICE}"
echo "Wrote confirmation paired-order follow-up to ${OUTPUT_DIR}"
