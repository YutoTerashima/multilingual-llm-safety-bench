from __future__ import annotations

"""Report metadata for the mature portfolio iteration."""

PROJECT_TITLE = 'Multilingual LLM Safety Bench'
RESEARCH_PROBLEM = 'How does safety classification performance vary across languages, scripts, and low-resource slices?'
DATASET_SUMMARY = '80,000 stratified multilingual safety examples with language/script group metadata.'
TAKEAWAYS = ['Aggregate macro-F1 hides meaningful per-language variation.', 'Character n-grams remain competitive because script-level information matters.', 'The GPU MLP result is best interpreted as a calibration warning: high unsafe recall can collapse safe recall.']
NEXT_EXPERIMENTS = ['Add compact XLM-R or mBERT fine-tuning for a stronger multilingual baseline.', 'Group languages by script and resource level in the report appendix.', 'Add over-refusal proxy analysis for benign prompts by language.']


def report_outline() -> list[str]:
    return [
        "Abstract",
        "Research question",
        "Dataset card",
        "Methods",
        "Experiment matrix",
        "Results",
        "Ablations",
        "Failure analysis",
        "Engineering notes",
        "Limitations",
        "Reproduction",
    ]


def maturity_claims() -> dict[str, object]:
    return {
        "title": PROJECT_TITLE,
        "problem": RESEARCH_PROBLEM,
        "dataset": DATASET_SUMMARY,
        "takeaways": TAKEAWAYS,
        "next_experiments": NEXT_EXPERIMENTS,
    }
