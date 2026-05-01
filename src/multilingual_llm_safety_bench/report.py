from __future__ import annotations

from .bench import run_benchmark


def build_report() -> str:
    rows = [
        f"| {item.case_id} | {item.language} | {item.behavior} | {item.status} |"
        for item in run_benchmark()
    ]
    return "\n".join(
        [
            "# Multilingual Safety Mini-Benchmark",
            "",
            "| Case | Language | Behavior | Status |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "This synthetic benchmark emphasizes evaluator plumbing and multilingual taxonomy design.",
        ]
    )
