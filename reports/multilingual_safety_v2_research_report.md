# Multilingual LLM Safety Bench V2 Research Report

## Abstract

This V2 upgrade turns the repository into a reproducible project-level experiment suite. The run records the dataset, device, experiment matrix, metrics, figures, failure analysis, and reproduction commands in committed small artifacts.

## Dataset

- Source path: `data/processed/classification_examples.jsonl`
- Profile: `full`
- Runtime: `37.91` seconds
- Device: `cuda` / `NVIDIA GeForce RTX 5090 Laptop GPU`

## Methods

Experiments declared in `configs/experiment_matrix.yaml`:

- `char_ngram_tfidf`: `tfidf_char`
- `word_tfidf_lr`: `tfidf_word`
- `gpu_char_mlp`: `torch_mlp`
- `english_transfer_proxy`: `transfer_proxy`

## Experiments

The matrix produced `4` result rows. Best observed `macro_f1`: `0.7104` from `word_tfidf_lr`.

## Results

Key artifacts:

- `reports\results\v2_main_results.csv`
- `reports\results\v2_ablation_results.csv`
- `reports\results\v2_failure_cases.json`
- `reports\figures\v2_accuracy_by_experiment.png`
- `reports\figures\v2_confusion_matrix.png`
- `reports\figures\v2_group_unsafe_recall.png`
- `reports\figures\v2_model_macro_f1.png`

## Ablations

Configured ablations: language_family, unsafe_threshold, class_weight, samples_per_language. The generated ablation files quantify threshold, perturbation, architecture, retrieval, or metric sensitivity depending on the project.

## Failure Analysis

Failure records: `80`.

Top clusters:

- `false_negative`: 52
- `false_positive`: 28

## Discussion

Multilingual moderation is dominated by language imbalance and script effects. V2 reports aggregate metrics only alongside per-language recall and hardest-language error slices.

## Limitations

- Full raw caches, model weights, and optimizer states are intentionally excluded from GitHub.
- Results are designed for reproducible portfolio research; they are not production safety, medical, or compliance guarantees.
- Some V2 experiments use compact local artifacts to keep the repository lightweight.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
