import json
import os

class MemoryManager:
    def __init__(self, filepath="data/user_logs/memory.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump({}, f)

    def get_user_memory(self, user_id):
        with open(self.filepath, "r") as f:
            data = json.load(f)
        return data.get(user_id, [])

    def add_interaction(self, user_id, interaction):
        with open(self.filepath, "r") as f:
            data = json.load(f)
        if user_id not in data:
            data[user_id] = []
        data[user_id].append(interaction)
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)
