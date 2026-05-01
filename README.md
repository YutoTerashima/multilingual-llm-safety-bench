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
