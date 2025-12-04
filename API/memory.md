# 🧠 Memory API (ai_memory/)  
### Persistence · Feedback Integration · Benchmark Tracking

---

# 📦 MemoryStore

## `save(workflow)`
Writes workflow JSON to:

```
data/workflows/<id_timestamp>.json
```

---

# 📊 BenchmarkTracker
Tracks improvements:

- clarity  
- score deltas  
- regeneration success  

---

# 🧠 FeedbackIntegrator

Core component of recursive meta-learning.

### Methods:

#### `record_cycle(diff_summary, evaluation, regenerated)`
Stores clarity, diff size, regen events.

#### `_recalculate_threshold()`
Adaptive regeneration threshold logic.

---

# 🚨 AnomalyDetector (stub)
Future:
- detect semantic drift  
- graph instability  
- recursion runaway
