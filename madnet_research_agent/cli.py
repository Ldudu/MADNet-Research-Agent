from __future__ import annotations

import argparse
from pathlib import Path

from madnet_research_agent.workflow import ResearchWorkflow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the MADNet Research Agent demo workflow."
    )
    parser.add_argument(
        "--question",
        default="What are the open issues in remote sensing VSR?",
        help="Research question to analyze.",
    )
    parser.add_argument(
        "--corpus",
        default="data/sample_corpus.json",
        help="Path to the local corpus JSON file.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory for generated report and trace artifacts.",
    )
    parser.add_argument(
        "--list-questions",
        action="store_true",
        help="Print bundled example research questions and exit.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.list_questions:
        print("Bundled example questions are available in data/research_questions.json")
        return 0
    workflow = ResearchWorkflow()
    outputs = workflow.run(
        question=args.question,
        corpus_path=Path(args.corpus),
        output_dir=Path(args.output_dir),
    )
    print(f"Report: {outputs['report_path']}")
    print(f"Trace: {outputs['trace_path']}")
    print(f"Summary: {outputs['summary_path']}")
    return 0
