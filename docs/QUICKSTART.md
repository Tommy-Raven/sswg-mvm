# Quickstart Guide

Welcome to **AI Instructions Workflow Generator v4.5**

This system creates, evaluates, and evolves instructional AI workflows — automatically and recursively.

## 🚀 Getting Started
1. **Clone the repository**
   ```bash
   git clone https://github.com/Tommy-Raven/AI_instructions_workflow.git
   cd AI_instructions_workflow

Install dependencies
bash

pip install -r REQUIREMENTS.txt

Run the main generator
bash
python generator/main.py

Trigger recursion (optional)
When prompted, type E to generate recursive workflow variants and merge best results.

Requirements
Python 3.11+
VS Code recommended for editing and testing

Outputs
Human-readable: Markdown (.md)
Machine-readable: JSON (.json)
yaml

---

### `ARCHITECTURE.md`
```markdown
# System Architecture Overview

**AI Instructions Workflow v4.5** follows a modular, recursive design divided into eight optimization phases.

## 🔧 Core Directories

| Directory | Purpose |
|------------|----------|
| `generator/` | Workflow creation, recursion management, caching, and export logic |
| `ai_core/` | Phase orchestration, dependency graph, and task coordination |
| `ai_recursive/` | Handles variant generation, merging, and version evolution |
| `ai_evaluation/` | Workflow scoring, semantic comparison, and quality metrics |
| `ai_monitoring/` | Logging, telemetry, and live CLI dashboard |
| `ai_validation/` | Schema validation, regression testing, version tracking |
| `ai_visualization/` | Workflow graph rendering (Graphviz/Mermaid) |
| `ai_memory/` | Memory persistence, benchmarks, and feedback adaptation |
| `ai_graph/` | Dependency mapping and semantic network construction |

## Workflow Phases
1. Initialization & Variable Acquisition  
2. Objective Refinement  
3. Human-Readable How-To Generation  
4. Modular Expansion & Reusability  
5. Evaluation & Quality Assurance  
6. Regeneration & Evolution  
7. Visualization & Monitoring  
8. Adaptive Optimization & Learning Memory