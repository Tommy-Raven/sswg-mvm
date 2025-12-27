# Running SSWG-MVM

**Canonical runbook (how to run + expected outputs):** This document is the canonical reference. Other docs are secondary/overview and should defer to the instructions here to avoid drift.

## Generate a Workflow (default template)

```bash
python3 -m generator.main --preview
```

## Specify a Template

```bash
python3 -m generator.main --template technical
```

## Export Artifacts

Artifacts appear under:

```
data/outputs/
```

Includes:

- JSON  
- Markdown  
- Mermaid DAG  

---

# Run Without Refinement

```bash
python3 -m generator.main --no-refine
```

---

# Enable/Disable History Tracking

```bash
python3 -m generator.main --no-history
```

---

# Full Options

```bash
python3 -m generator.main --help
```
