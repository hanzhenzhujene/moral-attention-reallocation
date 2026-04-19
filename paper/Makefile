PAPER=main

all: $(PAPER).pdf

$(PAPER).pdf: $(PAPER).tex ../assets/confirmation-comparison-bars.pdf ../assets/text-anchor-confirmation-qwen15.pdf
	pdflatex -interaction=nonstopmode -halt-on-error $(PAPER).tex
	pdflatex -interaction=nonstopmode -halt-on-error $(PAPER).tex

clean:
	rm -f $(PAPER).aux $(PAPER).log $(PAPER).out $(PAPER).toc $(PAPER).fls $(PAPER).fdb_latexmk
