#!/usr/bin/env bash
set -euo pipefail

# Build the public paper PDF from the checked-in LaTeX source.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAPER_DIR="${ROOT_DIR}/project/paper"

if command -v tectonic >/dev/null 2>&1; then
  echo "Using tectonic to build ${PAPER_DIR}/main.tex"
  (
    cd "${PAPER_DIR}"
    tectonic main.tex
  )
else
  if ! command -v pdflatex >/dev/null 2>&1; then
    echo "Neither 'tectonic' nor 'pdflatex' is available." >&2
    echo "See ${PAPER_DIR}/README.md for paper build prerequisites." >&2
    exit 1
  fi
  echo "Using pdflatex via project/paper/Makefile"
  make -C "${PAPER_DIR}"
fi

# Keep the public repo clean by removing LaTeX auxiliary files after a successful build.
make -C "${PAPER_DIR}" clean >/dev/null
