# Real Dataset Analysis: Multilingual Safety Classification

Source: [lumees/multilingual-safety-classification-dataset](https://huggingface.co/datasets/lumees/multilingual-safety-classification-dataset)

This analysis uses 320 public multilingual safety prompts sampled from multiple dataset offsets. Prompts are represented as hashes, prompt lengths, language codes, and safety labels.

- Sampling strategy: stratified offsets [0, 5000, 10000, 20000, 50000, 100000, 150000, 200000]
- Distinct languages in sample: 8
- Label counts: {'2': 157, '0': 92, '1': 71}
- Language counts: {'amh_Ethi': 40, 'ben_Beng': 40, 'bos_Latn': 40, 'ces_Latn': 40, 'ind_Latn': 40, 'nso_Latn': 40, 'srp_Cyrl': 40, 'yor_Latn': 40}

Interpretation: multilingual safety evaluation should report per-language coverage rather than only aggregate pass/fail rates. This sampled slice is intentionally stratified because the source dataset is ordered by language.
