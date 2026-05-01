# Multilingual LLM Safety Bench

A compact English / Japanese / Chinese safety-evaluation benchmark for studying
refusal, over-refusal, unsafe compliance, and ambiguous handling across languages.

## Quick Start

```bash
pip install -e ".[dev]"
python examples/run_multilingual_bench.py
pytest
```

## Dataset Card

The included data is synthetic and intentionally mild. It is designed to test
evaluation plumbing and taxonomy mapping, not to publish harmful content.

## Output

```text
en refusal pass
ja safe_completion pass
zh over_refusal review
```

## Research Brief

See [`docs/research_brief.md`](docs/research_brief.md) for multilingual safety
framing, limitations, and next experiments.

## Portfolio Notes

This project connects the trilingual profile identity to a concrete multilingual AI-safety evaluation artifact.

## Deeper Analysis

`examples/run_analysis.py` computes per-language behavior distributions,
confusion pairs, and review rate.

## Experiment Artifacts

- Taxonomy: [`datasets/hazard_taxonomy.json`](datasets/hazard_taxonomy.json)
- Results: [`reports/multilingual_behavior_results.csv`](reports/multilingual_behavior_results.csv), [`reports/multilingual_behavior_results.json`](reports/multilingual_behavior_results.json)
- Analysis: [`reports/multilingual_behavior_analysis.md`](reports/multilingual_behavior_analysis.md)

## Calibration Metrics

The benchmark includes balanced accuracy and cross-language behavior gap helpers,
because raw pass rate hides whether one language is over-refusing more than another.

## Full Multilingual Suite

The expanded benchmark includes 36 cases in
[`datasets/full_multilingual_cases.json`](datasets/full_multilingual_cases.json)
and an analysis report in
[`reports/full_multilingual_analysis.md`](reports/full_multilingual_analysis.md).

## Stratification Check

`examples/check_stratification.py` verifies language and label distribution before
comparing model behavior across languages.
## Real Public Dataset Experiment

        The benchmark now includes `datasets/external/multilingual_safety_features.jsonl`, a
        hashed feature sample from
        [lumees/multilingual-safety-classification-dataset](https://huggingface.co/datasets/lumees/multilingual-safety-classification-dataset).
        The report studies language coverage and safety-label balance rather than relying only on
        hand-written demo prompts.

## GPU-Backed Real Experiment

This repository now includes a reproducible GPU-backed experiment using `lumees/multilingual-safety-classification-dataset`.
The smoke path runs on the local RTX 5090 Laptop GPU through the `Transformers` conda
environment and writes metrics, figures, and a markdown report.

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

Main report: `reports/multilingual_safety_gpu_benchmark.md`.

<!-- V2_RESEARCH_UPGRADE -->
## Publishable V2 Research Upgrade

This repository now includes a project-level V2 experiment suite:

- Reproducible matrix: `configs/experiment_matrix.yaml`
- Main runner: `scripts/run_matrix.py --device cuda --profile full`
- Failure analysis: `scripts/analyze_failures.py`
- Research report: `reports/multilingual_safety_v2_research_report.md`
- Experiment index: `reports/results/experiment_index.json`

The V2 artifacts include multiple experiments, ablations, figures, failure cases, and a discussion section while keeping raw caches and large checkpoints out of Git.

