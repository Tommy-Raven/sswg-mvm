# Frequently Asked Questions

### Q1. How do I stop recursion from running indefinitely?
Edit `config/recursion.yml` and set `max_depth`.

### Q2. How do I enable semantic scoring?
Ensure `semantic_scorer.py` and `semantic_analysis.py` are enabled under `config/settings.yml`.

### Q3. Can this run offline?
Yes — works entirely in VS Code with no external dependencies.