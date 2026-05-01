import json
from pathlib import Path

from multilingual_llm_safety_bench.sampling import stratification_report


if __name__ == "__main__":
    cases = json.loads(Path("datasets/full_multilingual_cases.json").read_text(encoding="utf-8"))
    report = stratification_report(cases)
    Path("reports/stratification_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
