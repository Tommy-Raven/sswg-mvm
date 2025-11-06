import json, os, datetime

class MemoryStore:
    def __init__(self, path="./data/workflows"):
        self.path = path
        os.makedirs(path, exist_ok=True)

    def save(self, wf):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file = os.path.join(self.path, f"{wf['workflow_id']}_{timestamp}.json")
        with open(file, "w", encoding="utf-8") as f:
            json.dump(wf, f, indent=2)
        return file
