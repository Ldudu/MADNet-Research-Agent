from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from typing import Iterable


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "for",
    "in",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "what",
}


@dataclass
class PaperNote:
    title: str
    focus: str
    method: str
    datasets: list[str]
    metrics: list[str]
    limitations: str
    tags: list[str]


def tokenize(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-zA-Z0-9-]+", text.lower())
        if token not in STOPWORDS
    }


class PlannerAgent:
    def run(self, question: str) -> dict[str, object]:
        goals = [
            "identify dominant modeling themes",
            "compare evaluation and dataset assumptions",
            "surface unresolved limitations and open issues",
        ]
        dimensions = ["method", "degradation", "dataset", "metric", "limitation"]
        return {
            "normalized_question": question.strip(),
            "sub_goals": goals,
            "focus_dimensions": dimensions,
        }


class RetrieverAgent:
    def run(
        self,
        question: str,
        plan: dict[str, object],
        corpus: Iterable[PaperNote],
        top_k: int = 4,
    ) -> dict[str, object]:
        query = " ".join([question, *plan["sub_goals"], *plan["focus_dimensions"]])
        query_tokens = tokenize(query)
        ranked: list[tuple[int, PaperNote]] = []
        for paper in corpus:
            source = " ".join(
                [
                    paper.title,
                    paper.focus,
                    paper.method,
                    paper.limitations,
                    " ".join(paper.tags),
                    " ".join(paper.datasets),
                    " ".join(paper.metrics),
                ]
            )
            overlap = len(query_tokens & tokenize(source))
            ranked.append((overlap, paper))
        ranked.sort(key=lambda item: item[0], reverse=True)
        evidence = [paper for score, paper in ranked if score > 0][:top_k]
        notes = [f"retrieved {len(evidence)} evidence items from local corpus"]
        return {"evidence": evidence, "notes": notes}


class AnalystAgent:
    def run(self, evidence: Iterable[PaperNote]) -> dict[str, object]:
        findings: list[str] = []
        datasets: set[str] = set()
        metrics: set[str] = set()
        limitation_signals: list[str] = []
        for paper in evidence:
            findings.append(f"{paper.title}: {paper.focus}")
            datasets.update(paper.datasets)
            metrics.update(paper.metrics)
            limitation_signals.append(paper.limitations)
        findings.append(
            "Most evidence emphasizes degradation realism, temporal alignment, "
            "and benchmark comparability as central research bottlenecks."
        )
        return {
            "findings": findings,
            "datasets": sorted(datasets),
            "metrics": sorted(metrics),
            "limitation_signals": limitation_signals,
        }


class CriticAgent:
    def run(
        self,
        question: str,
        evidence: Iterable[PaperNote],
        analysis: dict[str, object],
    ) -> dict[str, object]:
        blind_spots: list[str] = []
        tags = {tag for paper in evidence for tag in paper.tags}
        if "real-world" not in tags and "real-world gap" not in tags:
            blind_spots.append("Real-world degradation coverage is weak.")
        if "benchmark" not in tags and "evaluation" not in tags:
            blind_spots.append("Benchmark comparability is underexplored.")
        if not blind_spots:
            blind_spots.append(
                "Evidence covers the major themes, but unified evaluation "
                "protocols and real-world validation remain incomplete."
            )
        risks = [
            "The sample corpus is illustrative and should be replaced with real paper notes for production use.",
            "A high-level synthesis can still overfit to the retrieved shortlist if recall is poor.",
        ]
        return {
            "review_target": question,
            "blind_spots": blind_spots,
            "risks": risks,
            "limitation_signals": analysis["limitation_signals"],
        }


class WriterAgent:
    def run(
        self,
        question: str,
        plan: dict[str, object],
        evidence: Iterable[PaperNote],
        analysis: dict[str, object],
        critique: dict[str, object],
    ) -> dict[str, object]:
        evidence_rows = []
        for paper in evidence:
            evidence_rows.append(
                "| {title} | {datasets} | {metrics} | {limitations} |".format(
                    title=paper.title,
                    datasets=", ".join(paper.datasets),
                    metrics=", ".join(paper.metrics),
                    limitations=paper.limitations,
                )
            )
        report = "\n".join(
            [
                "# MADNet Research Agent Report",
                "",
                f"## Question",
                question,
                "",
                "## Planner Output",
                f"- Sub-goals: {', '.join(plan['sub_goals'])}",
                f"- Focus dimensions: {', '.join(plan['focus_dimensions'])}",
                "",
                "## Analyst Findings",
                *[f"- {finding}" for finding in analysis["findings"]],
                "",
                "## Evidence Table",
                "| Evidence | Datasets | Metrics | Noted Limitation |",
                "| --- | --- | --- | --- |",
                *evidence_rows,
                "",
                "## Critic Review",
                *[f"- {item}" for item in critique["blind_spots"]],
                "",
                "## Risks",
                *[f"- {item}" for item in critique["risks"]],
                "",
                "## Conclusion",
                "The current evidence suggests that remote sensing VSR still faces three recurring barriers: realistic degradation modeling, robust temporal alignment under viewpoint drift, and fair benchmark design. A useful next step is to connect this workflow to a larger literature corpus and a real LLM-backed extractor.",
            ]
        )
        trace = {
            "question": question,
            "plan": plan,
            "evidence": [asdict(paper) for paper in evidence],
            "analysis": analysis,
            "critique": critique,
        }
        return {"report": report, "trace": trace}
