from multilingual_llm_safety_bench.bench import run_benchmark


if __name__ == "__main__":
    for judgement in run_benchmark():
        print(judgement.language, judgement.behavior, judgement.status)
