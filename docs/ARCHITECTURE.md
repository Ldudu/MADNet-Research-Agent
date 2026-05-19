# Architecture

## Overview

MADNet Research Agent is a multi-agent research workflow prototype aimed at remote sensing VSR. The design goal is not only to answer a question, but to preserve a reviewable reasoning chain from question intake to final report generation.

## Core pain point

Remote sensing VSR research often breaks down because:

- evidence is scattered across papers, notes, and benchmarks;
- degradation assumptions differ from paper to paper;
- datasets and metrics are not directly comparable;
- the final written conclusion may skip unsupported assumptions.

The system addresses this by turning the workflow into a sequence of explicit agent roles instead of one opaque answer step.

## Agent roles

### 1. Planner Agent

Input: raw research question

Output:

- normalized question
- sub-goals
- focus dimensions such as method, degradation, dataset, evaluation, and limitations

Role:

- expands the question into a reasoning plan;
- ensures the later steps do not retrieve evidence blindly.

### 2. Retriever Agent

Input:

- planner objectives
- local paper corpus

Output:

- ranked candidate evidence
- retrieval notes

Role:

- performs targeted recall against the current question;
- keeps the evidence shortlist small enough for review.

### 3. Analyst Agent

Input:

- retrieved evidence

Output:

- structured findings
- repeated patterns across methods
- extracted dataset and metric signals

Role:

- converts loose evidence into comparable observations;
- prepares the materials for synthesis.

### 4. Critic Agent

Input:

- analyst findings
- retrieved evidence
- original question

Output:

- blind spots
- evidence gaps
- likely sources of bias

Role:

- acts as a guardrail against overclaiming;
- checks whether the current evidence can support the draft conclusion.

### 5. Writer Agent

Input:

- all intermediate state

Output:

- markdown report
- JSON trace

Role:

- writes the final answer in a form that a reviewer can inspect;
- preserves the path, not just the conclusion.

## Long-chain reasoning

This project explicitly models long-chain reasoning instead of a single prompt-response exchange:

1. Decompose the question.
2. Retrieve targeted evidence.
3. Extract structured signals.
4. Stress-test the evidence.
5. Synthesize a final report.

That design is important for research use cases because the user often cares as much about the path of reasoning as the answer itself.

## Multi-agent collaboration pattern

The multi-agent pattern here is sequential and stateful rather than parallel by default. Each agent receives the previous agent's state and adds one narrowly scoped transformation. This makes the logic easy to audit and reduces prompt entanglement.

Possible future upgrades:

- replace the sample corpus with live paper retrieval;
- swap rule-based analysis for LLM-backed extraction;
- add a Reviewer Agent for self-consistency checks;
- add a Tool Agent for benchmark or experiment table parsing.

## Why this is verification-friendly

The repo is designed so a reviewer can inspect:

- the written project claim in `README.md`;
- the architecture description in this document;
- the concrete workflow in `madnet_research_agent/`;
- the output artifacts in `outputs/` after running the demo;
- the CI workflow in `.github/workflows/demo.yml`.
