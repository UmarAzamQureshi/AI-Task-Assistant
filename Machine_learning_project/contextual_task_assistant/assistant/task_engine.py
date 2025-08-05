import openai
from transformers import pipeline

class TaskEngine:
    def __init__(self, openai_api_key=None, deepseek_api_key=None):
        try:
            self.llm = pipeline("text-generation", model="gpt2", max_new_tokens=100)
        except Exception as e:
            print(f"Error initializing pipeline: {str(e)}")
            self.llm = None
        self.tasks = {}
        self.task_status = {}
        self.openai_api_key = openai_api_key
        self.deepseek_api_key = deepseek_api_key
        if openai_api_key:
            import openai
            openai.api_key = openai_api_key

    def register_task(self, task_name, task_function):
        self.tasks[task_name] = task_function
        self.task_status[task_name] = 'registered'

    def execute_task(self, task_name, *args, **kwargs):
        if task_name in self.tasks:
            self.task_status[task_name] = 'in_progress'
            result = self.tasks[task_name](*args, **kwargs)
            self.task_status[task_name] = 'completed'
            return result
        else:
            # Fallback to LLM if task is not registered
            user_input = kwargs.get('user_input', '')
            return self.run_fallback_llm(user_input)

    def get_task_status(self, task_name):
        return self.task_status.get(task_name, 'not_found')

    def run_fallback_llm(self, user_input):
        # Try DeepSeek chat if API key is set, else OpenAI, else local LLM
        if self.deepseek_api_key:
            import requests
            url = "https://api.deepseek.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.deepseek_api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": user_input}]
            }
            try:
                resp = requests.post(url, headers=headers, json=payload)
                resp.raise_for_status()
                data = resp.json()
                return data["choices"][0]["message"]["content"]
            except Exception as e:
                print(f"DeepSeek error: {e}")
                # Fall through to OpenAI/local LLM if DeepSeek fails
        if self.openai_api_key:
            try:
                import openai
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": user_input}]
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"OpenAI error: {e}")
                # Fall through to local LLM if OpenAI fails
        if self.llm is not None:
            try:
                result = self.llm(f"Task: {user_input}\nResponse:")
                return result[0]['generated_text'].split("Response:")[-1].strip()
            except Exception as e:
                return f"Local LLM error: {str(e)}"
        return "Error: No language model available"