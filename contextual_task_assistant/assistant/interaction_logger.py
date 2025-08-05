import pandas as pd
import os
from datetime import datetime

class InteractionLogger:
    def __init__(self, log_path="data/user_logs/interactions.csv"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        if not os.path.exists(log_path):
            pd.DataFrame(columns=["timestamp", "user_input", "intent", "confidence"]).to_csv(log_path, index=False)

    def log(self, user_input, intent, confidence):
        df = pd.read_csv(self.log_path)
        df = df.append({
            "timestamp": datetime.now(),
            "user_input": user_input,
            "intent": intent,
            "confidence": confidence
        }, ignore_index=True)
        df.to_csv(self.log_path, index=False)
