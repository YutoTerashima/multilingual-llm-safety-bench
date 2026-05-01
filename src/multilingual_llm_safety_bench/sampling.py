from __future__ import annotations

from collections import Counter


def stratification_report(cases: list[dict]) -> dict[str, object]:
    languages = Counter(case["language"] for case in cases)
    labels = Counter(case["expected"] for case in cases)
    pairs = Counter((case["language"], case["expected"]) for case in cases)
    return {
        "languages": dict(sorted(languages.items())),
        "labels": dict(sorted(labels.items())),
        "language_label_pairs": {f"{lang}:{label}": count for (lang, label), count in sorted(pairs.items())},
    }
