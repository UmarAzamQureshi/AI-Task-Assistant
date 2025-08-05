
import streamlit as st
from assistant.nlp_module import NLPModule
from assistant.memory_manager import MemoryManager
from assistant.task_engine import TaskEngine

nlp = NLPModule()
memory = MemoryManager()
# Initialize TaskEngine with DeepSeek API key in backend
task_engine = TaskEngine(deepseek_api_key="sk-a6ff51ac660d4da2abc98c9436102200")
user_id = "user1"

st.title("AI Task Assistant")

# Secure input field for OpenAI API key
# Remove OpenAI API key input from UI

user_input = st.text_input("Say something:")
if user_input:
    intent, confidence = nlp.classify_intent(user_input)
    if confidence < 0.5:
        intent = "unknown"
    st.write(f"🔍 Intent Detected: `{intent}` (Confidence: {confidence:.2f})")
    metadata = {}
    if intent == "search_web":
        metadata = {"query": user_input.replace("search ", "", 1)}
    response = task_engine.execute(intent, metadata, user_input=user_input)
    st.write(f"Assistant: {response}")
    memory.add_interaction(user_id, {
        "input": user_input,
        "intent": intent,
        "response": response
    })

    st.write("Was this prediction accurate?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Yes, correct intent"):
            if intent != "unknown":
                learned = nlp.learn_from_feedback(user_input, intent)
                if learned:
                    st.success("✅ Learned from this input for future classification.")
                else:
                    st.info("Already learned.")
            else:
                st.warning("Can't learn from unknown intent.")
    with col2:
        if st.button("👎 No, wrong intent"):
            st.write("Assign a correct intent below:")
            all_intents = list(nlp.intent_examples.keys())
            selected_intent = st.selectbox("Select intent to assign:", all_intents + ["new_intent"])
            if selected_intent == "new_intent":
                new_intent_name = st.text_input("Enter new intent name:")
                if st.button("Add new intent and assign") and new_intent_name:
                    nlp.learn_from_feedback(user_input, new_intent_name)
                    st.success(f"Added '{new_intent_name}' and learned from this input.")
            else:
                if st.button("Assign to selected intent"):
                    nlp.learn_from_feedback(user_input, selected_intent)
                    st.success(f"Assigned to '{selected_intent}' and learned from this input.")
