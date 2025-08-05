import datetime

class ContextManager:
    def __init__(self):
        self.context = {}

    def update_context(self, user_id, intent, metadata):
        timestamp = datetime.datetime.now()
        self.context[user_id] = {"intent": intent, "metadata": metadata, "timestamp": timestamp}

    def get_context(self, user_id):
        return self.context.get(user_id, {})
