import openai
import json
import os
from sentence_transformers import SentenceTransformer, util

class NLPModule:
    def __init__(self, config_path=None):
        # Use absolute path for intent_config.json
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'intent_config.json')
            config_path = os.path.abspath(config_path)
        self.config_path = config_path
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.intent_examples = self.load_intent_config()
        self.openai_api_key = None

    def set_openai_api_key(self, api_key):
        self.openai_api_key = api_key
        openai.api_key = api_key

    def gpt_classify_intent(self, user_input):
        if not self.openai_api_key:
            return None, 0.0
        prompt = f"Classify the user's intent from these options: {list(self.intent_examples.keys())}.\nUser input: {user_input}\nIntent:"
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=10,
                temperature=0
            )
            intent = response.choices[0].message.content.strip()
            # Confidence is not provided by GPT, so we use 1.0 if it matches known intents
            if intent in self.intent_examples:
                return intent, 1.0
            else:
                return "unknown", 0.0
        except Exception as e:
            print("OpenAI error:", e)
            return None, 0.0

    def load_intent_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                return json.load(f)
        return {}

    def save_intent_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.intent_examples, f, indent=2)

    def classify_intent(self, user_input):
        print("Intent examples loaded:", self.intent_examples)
        print("User input:", user_input)
        input_emb = self.model.encode(user_input, convert_to_tensor=True)
        best_intent = "unknown"
        best_score = 0.0

        for intent, examples in self.intent_examples.items():
            example_embs = self.model.encode(examples, convert_to_tensor=True)
            similarities = util.cos_sim(input_emb, example_embs)
            score = similarities.max().item()
            print(f"Intent: {intent}, Score: {score}")
            if score > best_score:
                best_intent = intent
                best_score = score

        print(f"Best intent: {best_intent}, Best score: {best_score}")
        return best_intent, best_score

    def learn_from_feedback(self, user_input, intent):
        if intent not in self.intent_examples:
            self.intent_examples[intent] = []
        if user_input not in self.intent_examples[intent]:
            self.intent_examples[intent].append(user_input)
            self.save_intent_config()
            return True
        return False
