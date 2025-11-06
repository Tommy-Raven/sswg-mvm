# Visualization Guide

Visual representations of recursion and dependencies.

## Tools Used
- **Graphviz** (DOT graph generation)
- **Mermaid.js** (for Markdown rendering)

## Example
```mermaid
graph TD
  A[Phase 1: Initialization] --> B[Phase 2: Generation]
  B --> C[Phase 3: Expansion]
  C --> D[Phase 4: Evaluation]
  D --> E[Phase 5: Regeneration]
  