# AI Task Assistant

## Overview
AI Task Assistant is an enterprise-ready, modular, and extensible assistant designed to execute tasks across multiple domains with precision. It leverages advanced language models (DeepSeek, OpenAI GPT-4, local LLMs) and integrates with external APIs to provide real-time, actionable solutions for productivity, travel, research, and more.

## Features
- **Domain-Agnostic Task Execution:** Handles tasks in productivity, travel, research, and other domains.
- **Modular Architecture:** Easily extendable for new domains and APIs.
- **LLM Integration:** Uses DeepSeek, OpenAI GPT-4, and local models for reasoning and fallback.
- **Enterprise-Grade Logging:** Tracks user interactions and task execution for audit and improvement.
- **Feedback Learning:** Learns from user corrections to improve intent classification and responses.
- **Secure API Key Management:** Backend-only key usage for enterprise security.

## Directory Structure
```
contextual_task_assistant/
├── assistant/
│   ├── __init__.py
│   ├── context_manager.py
│   ├── task_engine.py
│   ├── interaction_logger.py
│   ├── learning_model.py
│   └── nlp_module.py
├── data/
│   ├── user_logs/
│   ├── models/
│   └── embeddings/
├── main.py
├── config.py
├── requirements.txt
├── streamlit_app.py
└── README.md
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/UmarAzamQureshi/AI-Task-Assistant.git
   cd AI-Task-Assistant/contextual_task_assistant
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- **Streamlit App:**
  ```bash
  streamlit run streamlit_app.py
  ```
- **Command Line:**
  ```bash
  python main.py
  ```

## Configuration
- API keys for DeepSeek or OpenAI are set in the backend code for security.
- Modify `config.py` for custom paths and parameters.

## Extending the Assistant
- Add new domain modules in `assistant/` and register them in `TaskEngine`.
- Integrate external APIs by adding functions and updating `TaskEngine.execute`.
- Use feedback learning in `nlp_module.py` to improve intent classification.

## Example Domains
- **Travel:** Search flights, check status, book tickets.
- **Productivity:** Set reminders, manage calendar, summarize tasks.
- **Research:** Search web, summarize articles, extract entities.

## Security & Privacy
- API keys are never exposed in the frontend.
- User logs and data are stored securely in `data/user_logs/`.

## Contributing
Pull requests and issues are welcome! Please follow best practices and add tests for new features.

## Contact
For questions or enterprise support, contact [UmarAzamQureshi](https://github.com/UmarAzamQureshi).
