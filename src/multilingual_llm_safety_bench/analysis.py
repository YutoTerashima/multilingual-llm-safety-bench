from __future__ import annotations

from collections import Counter, defaultdict

from .bench import CASES, run_benchmark


def behavior_distribution() -> dict[str, object]:
    judgements = run_benchmark()
    by_language: dict[str, Counter[str]] = defaultdict(Counter)
    expected = {case.case_id: case.expected_behavior for case in CASES}
    confusion: Counter[tuple[str, str]] = Counter()
    for item in judgements:
        by_language[item.language][item.behavior] += 1
        confusion[(expected[item.case_id], item.behavior)] += 1
    return {
        "by_language": {lang: dict(counter) for lang, counter in sorted(by_language.items())},
        "confusion": {f"{gold}->{pred}": count for (gold, pred), count in sorted(confusion.items())},
        "review_rate": round(sum(item.status == "review" for item in judgements) / len(judgements), 3),
    }
