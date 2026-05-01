from pathlib import Path

from multilingual_llm_safety_bench.report import build_report


if __name__ == "__main__":
    out = Path("reports/multilingual_safety_report.md")
    out.write_text(build_report(), encoding="utf-8")
    print(out)
