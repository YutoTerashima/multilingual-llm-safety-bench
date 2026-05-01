from multilingual_llm_safety_bench.analysis import behavior_distribution
from multilingual_llm_safety_bench.calibration import balanced_accuracy, language_gap


def test_calibration_metrics():
    data = behavior_distribution()
    assert balanced_accuracy(data["confusion"]) >= 0
    assert language_gap(data["by_language"], "over_refusal") >= 0
