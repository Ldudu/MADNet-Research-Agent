from __future__ import annotations

from typing import Protocol


class Planner(Protocol):
    def run(self, question: str) -> dict[str, object]:
        ...


class Retriever(Protocol):
    def run(
        self,
        question: str,
        plan: dict[str, object],
        corpus: object,
        top_k: int = 4,
    ) -> dict[str, object]:
        ...


class Analyst(Protocol):
    def run(self, evidence: object) -> dict[str, object]:
        ...


class Critic(Protocol):
    def run(
        self,
        question: str,
        evidence: object,
        analysis: dict[str, object],
    ) -> dict[str, object]:
        ...


class Writer(Protocol):
    def run(
        self,
        question: str,
        plan: dict[str, object],
        evidence: object,
        analysis: dict[str, object],
        critique: dict[str, object],
        evaluation: dict[str, object],
    ) -> dict[str, object]:
        ...
