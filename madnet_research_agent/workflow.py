from __future__ import annotations

import json
from pathlib import Path

from madnet_research_agent.agents import (
    AnalystAgent,
    CriticAgent,
    PaperNote,
    PlannerAgent,
    RetrieverAgent,
    WriterAgent,
)


class ResearchWorkflow:
    def __init__(self) -> None:
        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.analyst = AnalystAgent()
        self.critic = CriticAgent()
        self.writer = WriterAgent()

    def load_corpus(self, corpus_path: Path) -> list[PaperNote]:
        payload = json.loads(corpus_path.read_text(encoding="utf-8"))
        return [PaperNote(**item) for item in payload]

    def run(
        self,
        question: str,
        corpus_path: Path,
        output_dir: Path,
    ) -> dict[str, Path]:
        corpus = self.load_corpus(corpus_path)
        plan = self.planner.run(question)
        retrieved = self.retriever.run(question, plan, corpus)
        analysis = self.analyst.run(retrieved["evidence"])
        critique = self.critic.run(question, retrieved["evidence"], analysis)
        written = self.writer.run(
            question=question,
            plan=plan,
            evidence=retrieved["evidence"],
            analysis=analysis,
            critique=critique,
        )

        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / "latest_report.md"
        trace_path = output_dir / "latest_trace.json"

        report_path.write_text(written["report"], encoding="utf-8")
        trace_path.write_text(
            json.dumps(written["trace"], indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return {"report_path": report_path, "trace_path": trace_path}
