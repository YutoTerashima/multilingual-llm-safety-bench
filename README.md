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
## Publishable V2 Research Results

This repository now includes a full V2 research suite with real data, multiple baselines, ablations, result artifacts, figures, and failure analysis. The README summarizes the measured run so the project can be judged from results, not just project intent.

### Dataset And Scale

80,000 stratified examples from `lumees/multilingual-safety-classification-dataset`, with language/script group metadata retained.

- Full-profile result rows: `4`
- Experiment profile: `full`
- Experiment index: [`reports/results/experiment_index.json`](reports/results/experiment_index.json)
- Full report: [`reports/multilingual_safety_v2_research_report.md`](reports/multilingual_safety_v2_research_report.md)

### Main Results

| experiment_id | accuracy | macro_f1 | unsafe_recall | safe_recall | auroc | runtime_seconds |
| --- | --- | --- | --- | --- | --- | --- |
| char_ngram_tfidf | 0.7049 | 0.6930 | 0.6695 | 0.7779 | 0.8027 | 14.4710 |
| word_tfidf_lr | 0.7216 | 0.7104 | 0.6817 | 0.8039 | 0.8286 | 3.4470 |
| gpu_char_mlp | 0.6754 | 0.4104 | 0.9992 | 0.0077 | 0.6789 | 4.8220 |
| english_transfer_proxy | 0.7049 | 0.6930 | 0.6695 | 0.7779 | 0.8027 | 14.2900 |

Language/group slice preview:

| group | macro_f1 | rows | unsafe_recall |
| --- | --- | --- | --- |
| amh_Ethi | 0.7341 | 892.0 | 0.7664 |
| ben_Beng | 0.7744 | 1,505 | 0.7855 |
| bos_Latn | 0.7885 | 1,805 | 0.8079 |
| bul_Cyrl | 0.8118 | 1,792 | 0.8369 |
| ceb_Latn | 0.7595 | 1,067 | 0.7510 |
| ces_Latn | 0.7029 | 891.0 | 0.6766 |
| deu_Latn | 0.7534 | 906.0 | 0.7585 |
| eng_Latn | 0.7850 | 868.0 | 0.7986 |
| fra_Latn | 0.6712 | 356.0 | 0.6936 |
| ind_Latn | 0.7890 | 827.0 | 0.7982 |

### Analysis

- Word TF-IDF is the strongest measured baseline in this run, with macro-F1 around 0.710 and AUROC around 0.829 across the multilingual sample.
- Character n-grams are competitive, confirming that script-level cues matter for multilingual safety classification.
- The GPU MLP run behaves like a high-unsafe-recall operating point and nearly collapses safe recall, which is useful as a calibration warning rather than a final model.
- Per-language group breakdown is included because aggregate macro-F1 hides low-resource and script-family behavior differences.

### Failure Analysis

- `false_negative`: 52 records
- `false_positive`: 28 records

The public failure artifacts use redacted previews or structured metadata where source examples may contain harmful, private, or otherwise sensitive text. This keeps the analysis reproducible without turning the README into a prompt-injection or unsafe-content corpus.

### Key Artifacts

- [`reports/results/v2_main_results.csv`](reports/results/v2_main_results.csv)
- [`reports/results/v2_ablation_results.csv`](reports/results/v2_ablation_results.csv)
- [`reports/results/v2_failure_cases.json`](reports/results/v2_failure_cases.json)
- [`reports/figures/v2_accuracy_by_experiment.png`](reports/figures/v2_accuracy_by_experiment.png)
- [`reports/figures/v2_confusion_matrix.png`](reports/figures/v2_confusion_matrix.png)
- [`reports/figures/v2_group_unsafe_recall.png`](reports/figures/v2_group_unsafe_recall.png)
- [`reports/figures/v2_model_macro_f1.png`](reports/figures/v2_model_macro_f1.png)

Figures:

- [`reports/figures/v2_accuracy_by_experiment.png`](reports/figures/v2_accuracy_by_experiment.png)
- [`reports/figures/v2_confusion_matrix.png`](reports/figures/v2_confusion_matrix.png)
- [`reports/figures/v2_group_unsafe_recall.png`](reports/figures/v2_group_unsafe_recall.png)
- [`reports/figures/v2_model_macro_f1.png`](reports/figures/v2_model_macro_f1.png)

### Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
