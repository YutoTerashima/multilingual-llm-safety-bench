from multilingual_llm_safety_bench.analysis import behavior_distribution


def test_behavior_distribution_has_review_rate():
    data = behavior_distribution()
    assert data["review_rate"] > 0
    assert "zh" in data["by_language"]
