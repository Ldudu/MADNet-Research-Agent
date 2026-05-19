# Project Highlights

## One-paragraph summary

MADNet Research Agent is a multi-agent research assistant prototype for remote sensing video super-resolution. It addresses a real research productivity problem: relevant papers, degradation assumptions, datasets, and metrics are scattered, so researchers often spend excessive time manually searching, comparing, extracting, and re-checking evidence. The project turns that process into a long-chain multi-agent workflow with explicit stages for planning, retrieval, analysis, critique, and report generation.

## Core pain point

- Literature and evidence are scattered.
- Experimental assumptions are inconsistent across papers.
- Manual comparison is slow and easy to miss details.
- Final conclusions are often hard to audit back to evidence.

## Agent workflow

`Planner -> Retriever -> Analyst -> Critic -> Writer`

- `Planner`: decomposes the question into research targets.
- `Retriever`: recalls candidate evidence from the corpus.
- `Analyst`: turns raw evidence into structured observations.
- `Critic`: finds evidence gaps and overclaim risk.
- `Writer`: outputs report plus reasoning trace.

## Why it matters

- It demonstrates explicit long-chain reasoning.
- It demonstrates multi-agent collaboration with state handoff.
- It produces inspectable outputs instead of only a final answer.
- It is structured for verification, not just presentation.
- It includes prompts, evaluation logic, sample questions, and tests, so the repository has visible engineering depth.

## Review entry points

- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/DESIGN_CN.md`
- `docs/MIMO_APPLICATION_TEXT.md`
- `tests/test_workflow.py`
- `outputs/example_report.md`
- `outputs/example_summary.json`
- `outputs/example_trace.json`
