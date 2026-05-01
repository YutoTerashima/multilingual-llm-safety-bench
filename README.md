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
