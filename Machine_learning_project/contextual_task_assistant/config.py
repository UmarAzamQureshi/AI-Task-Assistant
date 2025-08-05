# Configuration settings for the contextual task assistant project

# Paths
DATA_DIR = "data/"
USER_LOGS_DIR = DATA_DIR + "user_logs/"
MODELS_DIR = DATA_DIR + "models/"
EMBEDDINGS_DIR = DATA_DIR + "embeddings/"

# Model parameters
MODEL_TYPE = "default_model"
EMBEDDING_DIMENSION = 300

# Logging settings
LOGGING_LEVEL = "INFO"
LOG_FILE = "logs/interaction.log"

# Other constants
MAX_CONTEXT_LENGTH = 512
MIN_TASK_PRIORITY = 1
MAX_TASK_PRIORITY = 10