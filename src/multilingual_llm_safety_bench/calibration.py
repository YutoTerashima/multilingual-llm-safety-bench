from __future__ import annotations


def balanced_accuracy(confusion: dict[str, int]) -> float:
    labels = sorted({pair.split("->")[0] for pair in confusion} | {pair.split("->")[1] for pair in confusion})
    recalls = []
    for label in labels:
        tp = confusion.get(f"{label}->{label}", 0)
        total = sum(count for pair, count in confusion.items() if pair.startswith(f"{label}->"))
        if total:
            recalls.append(tp / total)
    return round(sum(recalls) / len(recalls), 3) if recalls else 0.0


def language_gap(by_language: dict[str, dict[str, int]], behavior: str) -> int:
    values = [counts.get(behavior, 0) for counts in by_language.values()]
    return max(values) - min(values) if values else 0
