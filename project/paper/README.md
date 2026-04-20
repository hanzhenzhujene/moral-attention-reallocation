# Paper Build Notes

This directory contains the public LaTeX manuscript for the repository.

## Files

- [main.tex](main.tex): paper source
- [main.pdf](main.pdf): compiled paper PDF
- [text_anchor_confirmation_tables.tex](text_anchor_confirmation_tables.tex): generated table include used by the manuscript

## Build

From the repository root:

```bash
make paper
```

Build behavior:

- the public root target uses [scripts/build_paper.sh](../../scripts/build_paper.sh)
- if `tectonic` is installed, it is used first
- otherwise the build falls back to `pdflatex` through [Makefile](Makefile)

## Prerequisites

One of the following must be available on your machine:

- `tectonic`
- `pdflatex`

The paper depends on checked-in figure assets in [docs/assets/](../../docs/assets/) and on the generated table include [text_anchor_confirmation_tables.tex](text_anchor_confirmation_tables.tex), which is already committed in the public repo.

## Notes

- The shared Python experiment environment in [project/requirements.txt](../requirements.txt) is sufficient for reproducing the public result files and figures.
- LaTeX itself is a separate toolchain requirement and is therefore documented here explicitly rather than silently assumed.
