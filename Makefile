PYTHON ?= python3
VENV ?= .venv
VENV_PY := $(VENV)/bin/python
VENV_PIP := $(VENV)/bin/pip
SETUP_STAMP := $(VENV)/.public_runtime_installed

.PHONY: help setup reproduce-confirmation reproduce-paired-order reproduce-text-anchor reproduce-text-anchor-paired-order refresh-public-artifacts paper clean

help:
	@printf "Targets:\n"
	@printf "  make setup                           Create .venv and install the pinned public runtime\n"
	@printf "  make reproduce-confirmation          Reproduce the frozen public confirmation artifact\n"
	@printf "  make reproduce-paired-order          Reproduce the public paired-order follow-up\n"
	@printf "  make reproduce-text-anchor           Reproduce the 6-condition cross-tradition readout\n"
	@printf "  make reproduce-text-anchor-paired-order  Reproduce the 6-condition paired-order diagnostic\n"
	@printf "  make refresh-public-artifacts        Regenerate the checked-in public figures and tables\n"
	@printf "  make paper                           Rebuild the paper PDF (prefers tectonic, falls back to pdflatex)\n"
	@printf "  make clean                           Remove public reproduction outputs and LaTeX aux files\n"

$(SETUP_STAMP): project/requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r project/requirements.txt
	touch $(SETUP_STAMP)

setup: $(SETUP_STAMP)

reproduce-confirmation: $(SETUP_STAMP)
	bash scripts/reproduce_confirmation_slice.sh results/reproduction_confirmation

reproduce-paired-order: $(SETUP_STAMP)
	bash scripts/reproduce_confirmation_paired_order_followup.sh results/reproduction_confirmation_paired_order

reproduce-text-anchor: $(SETUP_STAMP)
	bash scripts/run_text_anchor_confirmation_qwen15b.sh results/reproduction_text_anchor_confirmation

reproduce-text-anchor-paired-order: $(SETUP_STAMP)
	bash scripts/run_text_anchor_confirmation_paired_order_qwen15b.sh results/reproduction_text_anchor_paired_order

refresh-public-artifacts: $(SETUP_STAMP)
	bash scripts/refresh_public_artifacts.sh

paper:
	bash scripts/build_paper.sh

clean:
	$(MAKE) -C project/paper clean
	rm -rf results/reproduction_confirmation
	rm -rf results/reproduction_confirmation_paired_order
	rm -rf results/reproduction_text_anchor_confirmation
	rm -rf results/reproduction_text_anchor_paired_order
