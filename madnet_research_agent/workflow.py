from __future__ import annotations

from pathlib import Path

from madnet_research_agent.agents import (
    AnalystAgent,
    CriticAgent,
    PlannerAgent,
    RetrieverAgent,
    WriterAgent,
)
from madnet_research_agent.corpus import load_corpus
from madnet_research_agent.evaluation import evaluate_coverage
from madnet_research_agent.reporting import write_json, write_text


class ResearchWorkflow:
    def __init__(self) -> None:
        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.analyst = AnalystAgent()
        self.critic = CriticAgent()
        self.writer = WriterAgent()

    def run(
        self,
        question: str,
        corpus_path: Path,
        output_dir: Path,
    ) -> dict[str, Path]:
        corpus = load_corpus(corpus_path)
        plan = self.planner.run(question)
        retrieved = self.retriever.run(question, plan, corpus)
        analysis = self.analyst.run(retrieved["evidence"])
        critique = self.critic.run(question, retrieved["evidence"], analysis)
        evaluation = evaluate_coverage(
            evidence=retrieved["evidence"],
            focus_dimensions=plan["focus_dimensions"],
        )
        written = self.writer.run(
            question=question,
            plan=plan,
            evidence=retrieved["evidence"],
            analysis=analysis,
            critique=critique,
            evaluation=evaluation,
        )

        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / "latest_report.md"
        trace_path = output_dir / "latest_trace.json"
        summary_path = output_dir / "latest_summary.json"

        write_text(report_path, written["report"])
        write_json(trace_path, written["trace"])
        write_json(summary_path, written["summary"])
        return {
            "report_path": report_path,
            "trace_path": trace_path,
            "summary_path": summary_path,
        }
