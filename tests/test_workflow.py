from pathlib import Path

from madnet_research_agent.workflow import ResearchWorkflow


def test_workflow_writes_three_artifacts(tmp_path: Path) -> None:
    workflow = ResearchWorkflow()
    result = workflow.run(
        question="What are the open issues in remote sensing VSR?",
        corpus_path=Path("data/sample_corpus.json"),
        output_dir=tmp_path,
    )
    assert result["report_path"].exists()
    assert result["trace_path"].exists()
    assert result["summary_path"].exists()
