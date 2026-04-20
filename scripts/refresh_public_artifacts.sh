#!/usr/bin/env bash
set -euo pipefail

# Regenerate the checked-in public figures and tables from the canonical result JSON files.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${ROOT_DIR}/.venv/bin/python"

if [[ ! -x "${PYTHON_BIN}" ]]; then
  PYTHON_BIN="python3"
fi

CONFIRM_SUMMARY="${ROOT_DIR}/results/main_same_act_confirmation_v12_mps/confirmation_summary.json"
CONFIRM_ROBUSTNESS="${ROOT_DIR}/results/main_same_act_confirmation_v12_mps/confirmation_robustness.json"
TEXT_SUMMARY="${ROOT_DIR}/results/main_same_act_text_anchor_v1_qwen15b_mps/confirmation_summary.json"
TEXT_PAIRED="${ROOT_DIR}/results/main_same_act_text_anchor_v1_qwen15b_paired_order_mps/paired_order_stability.json"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/render_confirmation_comparison_bars.py" \
  --summary "${CONFIRM_SUMMARY}" \
  --robustness "${CONFIRM_ROBUSTNESS}" \
  --output "${ROOT_DIR}/docs/assets/confirmation-comparison-bars.svg"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/render_confirmation_comparison_bars.py" \
  --summary "${CONFIRM_SUMMARY}" \
  --robustness "${CONFIRM_ROBUSTNESS}" \
  --output "${ROOT_DIR}/docs/assets/confirmation-comparison-bars.png"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/render_confirmation_comparison_bars.py" \
  --summary "${CONFIRM_SUMMARY}" \
  --robustness "${CONFIRM_ROBUSTNESS}" \
  --output "${ROOT_DIR}/docs/assets/confirmation-comparison-bars.pdf"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/render_text_anchor_confirmation_family_chart.py" \
  --summary "${TEXT_SUMMARY}" \
  --paired-order "${TEXT_PAIRED}" \
  --model "Qwen-1.5B-Instruct" \
  --output-svg "${ROOT_DIR}/docs/assets/text-anchor-confirmation-qwen15.svg" \
  --output-png "${ROOT_DIR}/docs/assets/text-anchor-confirmation-qwen15.png" \
  --output-pdf "${ROOT_DIR}/docs/assets/text-anchor-confirmation-qwen15.pdf"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/render_text_anchor_confirmation_tables.py" \
  --summary "${TEXT_SUMMARY}" \
  --paired-order "${TEXT_PAIRED}" \
  --model "Qwen-1.5B-Instruct" \
  --output-md "${ROOT_DIR}/docs/tables/text_anchor_confirmation_tables.md" \
  --output-tex "${ROOT_DIR}/project/paper/text_anchor_confirmation_tables.tex" \
  --output-absolute-csv "${ROOT_DIR}/docs/tables/condition_metric_matrix.csv"

echo "Refreshed public figures and tables under docs/assets/, docs/tables/, and project/paper/."
