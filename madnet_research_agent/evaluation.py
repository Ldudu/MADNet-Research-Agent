from __future__ import annotations

from madnet_research_agent.agents import PaperNote


def evaluate_coverage(
    evidence: list[PaperNote],
    focus_dimensions: list[str],
) -> dict[str, object]:
    tags = {tag for paper in evidence for tag in paper.tags}
    dimension_coverage = {
        "method": any(paper.method for paper in evidence),
        "degradation": "degradation" in tags or "real-world gap" in tags,
        "dataset": any(paper.datasets for paper in evidence),
        "metric": any(paper.metrics for paper in evidence),
        "limitation": any(paper.limitations for paper in evidence),
    }
    covered = sum(1 for value in dimension_coverage.values() if value)
    score = round(covered / max(len(focus_dimensions), 1), 2)
    summary = (
        "Coverage is broad enough for a first-pass synthesis."
        if score >= 0.8
        else "Coverage is partial and should be expanded before strong claims."
    )
    return {
        "coverage_score": score,
        "evidence_count": len(evidence),
        "dimension_coverage": dimension_coverage,
        "summary": summary,
    }
