import json
from pathlib import Path


def test_real_multilingual_sample_has_language_slices():
    rows = [json.loads(line) for line in Path("datasets/external/multilingual_safety_features.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(rows) >= 300
    assert len({row["lang"] for row in rows}) >= 5
    assert len({row["safety_label"] for row in rows}) >= 2
