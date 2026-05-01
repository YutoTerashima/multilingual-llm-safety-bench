# Research Brief

## Problem

LLM safety behavior is not language invariant. Refusal, over-refusal, ambiguity handling,
and safe redirection can shift across English, Japanese, and Chinese.

## Method

The benchmark defines a small behavior taxonomy and maps synthetic multilingual prompts
to expected safe behavior.

## What the Mock Demo Proves

The evaluator can identify over-refusal in one language while passing safe completions in
others. The important signal is not a single score, but a behavior distribution.

## Limitations

- The dataset is synthetic and mild.
- It is a plumbing benchmark, not a production safety dataset.
- Human review would be needed for real benchmark claims.

## Next Experiments

- Add bilingual human annotations.
- Add translation consistency checks.
- Add refusal-with-alternative quality scoring.
