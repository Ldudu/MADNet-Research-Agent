from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PlanState:
    normalized_question: str
    sub_goals: list[str]
    focus_dimensions: list[str]


@dataclass
class RetrievalState:
    evidence: list[dict[str, object]]
    notes: list[str]


@dataclass
class AnalysisState:
    findings: list[str]
    datasets: list[str]
    metrics: list[str]
    limitation_signals: list[str]


@dataclass
class CritiqueState:
    review_target: str
    blind_spots: list[str]
    risks: list[str]
    limitation_signals: list[str]


@dataclass
class EvaluationState:
    coverage_score: float
    evidence_count: int
    dimension_coverage: dict[str, bool]
    summary: str


@dataclass
class RunArtifacts:
    report_markdown: str
    trace_payload: dict[str, object]
    summary_payload: dict[str, object] = field(default_factory=dict)
