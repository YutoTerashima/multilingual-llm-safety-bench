import json
from pathlib import Path

from multilingual_llm_safety_bench.sampling import stratification_report


def test_stratification_report_counts_languages():
    cases = json.loads(Path("datasets/full_multilingual_cases.json").read_text(encoding="utf-8"))
    report = stratification_report(cases)
    assert set(report["languages"]) == {"en", "ja", "zh"}
