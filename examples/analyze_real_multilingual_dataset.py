import json
from collections import Counter
from pathlib import Path

rows = [json.loads(line) for line in Path("datasets/external/multilingual_safety_features.jsonl").read_text(encoding="utf-8").splitlines()]
print({"rows": len(rows), "languages": len(set(r["lang"] for r in rows)), "labels": Counter(r["safety_label"] for r in rows)})
