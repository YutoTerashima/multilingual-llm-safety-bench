import json

from multilingual_llm_safety_bench.analysis import behavior_distribution


if __name__ == "__main__":
    print(json.dumps(behavior_distribution(), indent=2, ensure_ascii=False))
