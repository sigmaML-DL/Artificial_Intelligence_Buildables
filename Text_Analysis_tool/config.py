SUMMARIZATION_MODELS = {
    "t5-small": "t5-small",                 # ✅ works
    "bart": "facebook/bart-large-cnn",      # ✅ summarization model
}
DEFAULT_SUM_MODEL = "t5-small"


SUMMARIZE_MAX_LENGTH = 120
SUMMARIZE_MIN_LENGTH = 40
SUMMARIZE_DO_SAMPLE = False

RESULTS_DIR = "data/results"

