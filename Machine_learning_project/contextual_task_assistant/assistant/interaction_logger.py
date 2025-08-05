class InteractionLogger:
    def __init__(self):
        self.logs = []

    def log_interaction(self, interaction):
        self.logs.append(interaction)

    def get_logs(self):
        return self.logs

    def clear_logs(self):
        self.logs = []