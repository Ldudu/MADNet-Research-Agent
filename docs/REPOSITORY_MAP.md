# Repository Map

## Core code

- `madnet_research_agent/agents.py`
  Agent roles and the core reasoning stages.
- `madnet_research_agent/workflow.py`
  End-to-end workflow orchestration.
- `madnet_research_agent/models.py`
  State models for plan, retrieval, analysis, critique, evaluation, and outputs.
- `madnet_research_agent/evaluation.py`
  Coverage evaluation logic.
- `madnet_research_agent/prompts.py`
  Prompt templates for each agent role.
- `madnet_research_agent/reporting.py`
  Output writing helpers.
- `madnet_research_agent/corpus.py`
  Corpus and question loading helpers.

## Project assets

- `data/sample_corpus.json`
  Local evidence corpus used by the prototype.
- `data/research_questions.json`
  Bundled sample research questions.
- `configs/default_config.json`
  Default project configuration for future expansion.
- `examples/sample_request.md`
  Example reviewer-facing request.

## Reviewer-facing docs

- `README.md`
- `docs/PROJECT_HIGHLIGHTS.md`
- `docs/DESIGN_CN.md`
- `docs/ARCHITECTURE.md`
- `docs/CASE_STUDY.md`
- `docs/MIMO_APPLICATION_TEXT.md`
- `docs/VERIFICATION.md`
- `docs/ROADMAP.md`
