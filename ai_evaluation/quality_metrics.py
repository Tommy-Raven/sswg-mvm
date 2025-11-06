def evaluate_clarity(wf):
    scores = {}
    for phase in wf.get("phases", []):
        text = phase.get("ai_task_logic", "")
        scores[phase["id"]] = len(text.split()) / 10  # crude clarity metric
    return {"clarity_score": sum(scores.values()) / len(scores)}
