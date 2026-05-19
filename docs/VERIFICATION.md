# Verification Guide

## What to check

This repository is intended to be easy for a reviewer to inspect.

Recommended order:

1. Read `README.md` for the project positioning and pain point.
2. Read `docs/ARCHITECTURE.md` for the multi-agent workflow.
3. Run the local demo to generate a report and trace.
4. Inspect `.github/workflows/demo.yml` to confirm the demo is CI-friendly.

## Local run

```bash
python main.py --question "What are the open issues in remote sensing VSR?"
```

Expected outputs:

- `outputs/latest_report.md`
- `outputs/latest_trace.json`

If a reviewer does not want to run the demo locally, they can inspect:

- `outputs/example_report.md`
- `outputs/example_trace.json`

## What the demo proves

The demo proves that the repository is not only a concept write-up:

- there is an explicit multi-agent workflow;
- each stage writes inspectable intermediate state;
- the final answer is backed by a traceable reasoning chain.

## Current scope

The included corpus is a small illustrative sample so the repo remains self-contained. In a production version, the same workflow can be connected to real paper retrieval, LLM inference, and benchmark parsing tools.
