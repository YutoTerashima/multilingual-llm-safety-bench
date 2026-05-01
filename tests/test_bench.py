from multilingual_llm_safety_bench.bench import run_benchmark


def test_benchmark_labels_all_languages():
    judgements = run_benchmark()
    assert {item.language for item in judgements} == {"en", "ja", "zh"}
    assert any(item.status == "review" for item in judgements)
