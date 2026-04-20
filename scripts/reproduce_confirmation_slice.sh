#!/usr/bin/env bash
set -euo pipefail

# Reproduce the frozen public Baseline-vs-Heart-focused confirmation artifact.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${ROOT_DIR}/results/reproduction_confirmation}"
TMP_CONFIG="$(mktemp "${TMPDIR:-/tmp}/confirmation_repro_config.XXXXXX.json")"

cleanup() {
  rm -f "${TMP_CONFIG}"
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

python3 - <<'PY' "${ROOT_DIR}" "${TMP_CONFIG}" "${OUTPUT_DIR}"
import json
import sys
from pathlib import Path

root_dir = Path(sys.argv[1]).resolve()
tmp_config = Path(sys.argv[2]).resolve()
output_dir = Path(sys.argv[3]).resolve()

config = {
    "name": "public_confirmation_reproduction",
    "benchmark_path": str(root_dir / "data/study/paper_first_main_same_act_confirmation_v0.json"),
    "jobs_path": str(root_dir / "results/paper_first_main_same_act_confirmation_jobs_v1.jsonl"),
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
  --model-alias Qwen-1.5B-Instruct \
  --device "${DEVICE}" \
  --output "${OUTPUT_DIR}/qwen_1_5b_confirmation_runs.jsonl" \
  --failures-output "${OUTPUT_DIR}/qwen_1_5b_confirmation_failures.jsonl" \
  --trace-output "${OUTPUT_DIR}/qwen_1_5b_confirmation_trace.jsonl"

python3 "${ROOT_DIR}/scripts/run_diagnostics.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_confirmation_runs.jsonl" \
  --output "${OUTPUT_DIR}/confirmation_run_diagnostics.json"

python3 "${ROOT_DIR}/scripts/evaluate_runs.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_confirmation_runs.jsonl" \
  --bootstrap-samples 1000 \
  --contrasts baseline:heart_focused \
  --output "${OUTPUT_DIR}/confirmation_summary.json"

if ! python3 "${ROOT_DIR}/scripts/evaluate_pilot_health.py" \
  --config "${ROOT_DIR}/configs/paper_first_study_v1.json" \
  --jobs "${ROOT_DIR}/results/paper_first_main_same_act_confirmation_jobs_v1.jsonl" \
  --runs "${OUTPUT_DIR}/qwen_1_5b_confirmation_runs.jsonl" \
  --models Qwen-1.5B-Instruct \
  --output "${OUTPUT_DIR}/confirmation_health.json"; then
  echo "Health thresholds were not fully met for this pre-freeze artifact; confirmation outputs were still written." >&2
fi

python3 "${ROOT_DIR}/scripts/evaluate_robustness_report.py" \
  --bootstrap-samples 400 \
  --contrasts baseline:heart_focused \
  --input "${OUTPUT_DIR}/qwen_1_5b_confirmation_runs.jsonl" \
  --output-json "${OUTPUT_DIR}/confirmation_robustness.json" \
  --output-md "${OUTPUT_DIR}/confirmation_robustness.md"

python3 "${ROOT_DIR}/scripts/analyze_task_b_swap_gap.py" \
  --input "${OUTPUT_DIR}/qwen_1_5b_confirmation_runs.jsonl" \
  --bucket-mode pair_type \
  --output-json "${OUTPUT_DIR}/confirmation_swap_gap_by_pair_type.json" \
  --output-md "${OUTPUT_DIR}/confirmation_swap_gap_by_pair_type.md"

python3 "${ROOT_DIR}/scripts/render_confirmation_overview.py" \
  --summary "${OUTPUT_DIR}/confirmation_summary.json" \
  --health "${OUTPUT_DIR}/confirmation_health.json" \
  --robustness "${OUTPUT_DIR}/confirmation_robustness.json" \
  --output "${OUTPUT_DIR}/confirmation_overview.svg"

python3 "${ROOT_DIR}/scripts/render_confirmation_comparison_bars.py" \
  --summary "${OUTPUT_DIR}/confirmation_summary.json" \
  --robustness "${OUTPUT_DIR}/confirmation_robustness.json" \
  --output "${OUTPUT_DIR}/confirmation_comparison_bars.svg"

python3 "${ROOT_DIR}/scripts/render_public_confirmation_report.py" \
  --summary "${OUTPUT_DIR}/confirmation_summary.json" \
  --robustness "${OUTPUT_DIR}/confirmation_robustness.json" \
  --health "${OUTPUT_DIR}/confirmation_health.json" \
  --model "Qwen-1.5B-Instruct" \
  --benchmark-name "paper_first_main_same_act_confirmation_v0" \
  --slice-composition "23 same_act_different_motive + 40 same-heart controls" \
  --summary-path "${OUTPUT_DIR}/confirmation_summary.json" \
  --robustness-path "${OUTPUT_DIR}/confirmation_robustness.json" \
  --health-path "${OUTPUT_DIR}/confirmation_health.json" \
  --output-json "${OUTPUT_DIR}/confirmation_readout.json" \
  --output-md "${OUTPUT_DIR}/confirmation_readout.md"

echo "Detected device: ${DEVICE}"
echo "Wrote confirmation artifact to ${OUTPUT_DIR}"
