from __future__ import annotations

from pathlib import Path

from madnet_research_agent.reporting import write_json, write_text


def export_markdown_bundle(
    output_dir: Path,
    report: str,
    summary: dict[str, object],
) -> dict[str, Path]:
    bundle_dir = output_dir / "bundle"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    report_path = bundle_dir / "report.md"
    summary_path = bundle_dir / "summary.json"
    write_text(report_path, report)
    write_json(summary_path, summary)
    return {
        "bundle_report_path": report_path,
        "bundle_summary_path": summary_path,
    }
