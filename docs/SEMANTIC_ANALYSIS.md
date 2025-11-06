# Semantic Analysis & Scoring

## Overview

`semantic_scorer.py` and `ai_evaluation/semantic_analysis.py` provide semantic comparison for recursive outputs.

## Purpose

- Detect whether new recursive outputs meaningfully differ.
- Assign delta and similarity scores using cosine/Levenshtein methods.
- Halt recursion if change < threshold.

## Scoring Formula


Semantic Delta = 1 - Similarity(Old_Output, New_Output)


## Example Integration
```python
from generator.semantic_scorer import SemanticScorer
score = SemanticScorer().compare(text_a, text_b)
if score < 0.15:
    stop_recursion()
