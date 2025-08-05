from assistant.context_manager import ContextManager
from assistant.task_engine import TaskEngine
from assistant.interaction_logger import InteractionLogger
from assistant.nlp_module import NLPModule

nlp = NLPModule()
context = ContextManager()
logger = InteractionLogger()
task_engine = TaskEngine()

def main():
    print("👋 Welcome to the AI Task Assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        intent, confidence = nlp.classify_intent(user_input, ["set_reminder", "fetch_summary", "search_web", "unknown"])
        context.update_context("user1", intent, {})
        logger.log(user_input, intent, confidence)
        response = task_engine.execute(intent, {})
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
