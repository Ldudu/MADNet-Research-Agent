from madnet_research_agent.agents import AnalystAgent, PaperNote, PlannerAgent, RetrieverAgent


def build_paper(title: str, tags: list[str]) -> PaperNote:
    return PaperNote(
        title=title,
        focus="focus",
        method="method",
        datasets=["DatasetA"],
        metrics=["PSNR"],
        limitations="limit",
        tags=tags,
    )


def test_planner_returns_focus_dimensions() -> None:
    result = PlannerAgent().run("What are the open issues?")
    assert "focus_dimensions" in result
    assert "dataset" in result["focus_dimensions"]


def test_retriever_returns_ranked_evidence() -> None:
    plan = PlannerAgent().run("real-world degradation")
    corpus = [
        build_paper("Paper A", ["real-world", "degradation"]),
        build_paper("Paper B", ["benchmark"]),
    ]
    result = RetrieverAgent().run("real-world degradation", plan, corpus, top_k=1)
    assert len(result["evidence"]) == 1
    assert result["evidence"][0].title == "Paper A"


def test_analyst_collects_datasets() -> None:
    evidence = [build_paper("Paper A", ["real-world"])]
    result = AnalystAgent().run(evidence)
    assert result["datasets"] == ["DatasetA"]
