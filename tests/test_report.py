from multilingual_llm_safety_bench.report import build_report


def test_report_mentions_all_languages():
    report = build_report()
    for language in ["en", "ja", "zh"]:
        assert f"| {language} |" in report
