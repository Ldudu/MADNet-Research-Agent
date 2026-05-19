from __future__ import annotations

import json
from pathlib import Path

from madnet_research_agent.agents import PaperNote


def load_corpus(corpus_path: Path) -> list[PaperNote]:
    payload = json.loads(corpus_path.read_text(encoding="utf-8"))
    return [PaperNote(**item) for item in payload]


def load_questions(questions_path: Path) -> list[dict[str, object]]:
    return json.loads(questions_path.read_text(encoding="utf-8"))
