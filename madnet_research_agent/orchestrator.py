from __future__ import annotations

import json
from pathlib import Path

from madnet_research_agent.exporters import export_markdown_bundle
from madnet_research_agent.workflow import ResearchWorkflow


class ProjectOrchestrator:
    def __init__(self) -> None:
        self.workflow = ResearchWorkflow()

    def run_project(
        self,
        question: str,
        corpus_path: Path,
        output_dir: Path,
    ) -> dict[str, Path]:
        outputs = self.workflow.run(
            question=question,
            corpus_path=corpus_path,
            output_dir=output_dir,
        )
        report = outputs["report_path"].read_text(encoding="utf-8")
        summary = json.loads(outputs["summary_path"].read_text(encoding="utf-8"))
        bundle_outputs = export_markdown_bundle(output_dir, report, summary)
        return {**outputs, **bundle_outputs}
