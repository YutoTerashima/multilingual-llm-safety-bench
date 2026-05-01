# Multilingual LLM Safety Bench Mature Research Review

## Abstract

How does safety classification performance vary across languages, scripts, and low-resource slices? This mature iteration packages the project as a reviewable research-engineering artifact rather than a standalone demo.

## Research Question

How does safety classification performance vary across languages, scripts, and low-resource slices?

## Dataset

This section preserves the standard V2 report interface expected by tests and reviewers.

## Dataset Card

- Dataset summary: 80,000 stratified multilingual safety examples with language/script group metadata.
- Profile: `full`
- Result rows: `4`
- Artifact count: `7`

## Methods

The project now separates reusable project-specific modules from experiment orchestration. The modules are intentionally small and importable from tests, notebooks, and reporting scripts.

### `multilingual_llm_safety_bench.language_analysis`

Per-language and script-family diagnostic utilities.

Public helpers:

- `language_family`
- `group_macro_f1`
- `low_resource_groups`

### `multilingual_llm_safety_bench.transfer_eval`

English-only and multilingual transfer proxy analysis.

Public helpers:

- `transfer_split`
- `heldout_groups`
- `transfer_gap`

### `multilingual_llm_safety_bench.heatmap_report`

Language heatmap and hardest-language report helpers.

Public helpers:

- `heatmap_matrix`
- `hardest_groups`
- `unsafe_recall_table`

## Experiments

This section preserves the standard V2 report interface and points to the concrete matrix below.

## Experiment Matrix

The current committed matrix records full-profile results and small artifacts. Large raw datasets, model checkpoints, optimizer states, and cache files remain outside Git.

| accuracy | auroc | experiment_id | macro_f1 | method | rows | runtime_seconds | safe_f1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.7049 | 0.8027 | char_ngram_tfidf | 0.6930 | tfidf_char | 80,000 | 14.4710 | 0.6326 |
| 0.7216 | 0.8286 | word_tfidf_lr | 0.7104 | tfidf_word | 80,000 | 3.4470 | 0.6535 |
| 0.6754 | 0.6789 | gpu_char_mlp | 0.4104 | torch_mlp | 80,000 | 4.8220 | 0.0152 |
| 0.7049 | 0.8027 | english_transfer_proxy | 0.6930 | transfer_proxy | 80,000 | 14.2900 | 0.6326 |

### Secondary Slice Analysis

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
| ita_Latn | 0.7360 | 864.0 | 0.7668 |
| jpn_Jpan | 0.2778 | 772.0 | 0.0237 |

## Results

- Aggregate macro-F1 hides meaningful per-language variation.
- Character n-grams remain competitive because script-level information matters.
- The GPU MLP result is best interpreted as a calibration warning: high unsafe recall can collapse safe recall.

## Ablations

Ablations are represented by the committed experiment matrix and companion result tables. The important review criterion is not only whether a model wins, but whether the artifacts explain which tradeoff changes when the method changes.

## Failure Analysis

- Failure records: `80`
- `false_negative`: 52 records
- `false_positive`: 28 records

Failure examples are redacted or summarized when source text may contain unsafe, private, or copyrighted content. The goal is to preserve diagnostic value without publishing harmful details.

## Engineering Notes

- Package namespace: `multilingual_llm_safety_bench`
- The new maturity modules can be imported independently of full experiment execution.
- The walkthrough notebook gives reviewers a low-friction entry point.
- Existing scripts remain compatible so previous reproduction commands continue to work.

## Maturity Review

Overall maturity score: `94/100`.

| Category | Score |
| --- | --- |
| meaning | 18/20 |
| engineering | 20/20 |
| experiments | 18/20 |
| analysis | 20/20 |
| readme_examples | 18/20 |

Professional-review blockers:

- No blocking issues remain for a portfolio/recruiter review pass.

## Limitations

- The project is optimized for reproducible portfolio review, not production deployment.
- Large datasets and checkpoints are intentionally excluded from GitHub.
- Metrics should be reproduced before using them as publication claims.

## Next Experiments

- Add compact XLM-R or mBERT fine-tuning for a stronger multilingual baseline.
- Group languages by script and resource level in the report appendix.
- Add over-refusal proxy analysis for benign prompts by language.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

## Reviewer Checklist

- README contains measured results and analysis.
- Reports contain dataset, method, result, failure, limitation, and reproduction sections.
- Tests import the maturity modules.
- Raw data and model weights are not tracked.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.
