import os, json
from config import *
from utils import summarize_text, detect_language, sentiment_analysis, writing_style_metrics

def analyze_text(text: str, model_id: str = DEFAULT_SUM_MODEL):
    return {
        "original_text": text,
        "summary": summarize_text(text, model_id, SUMMARIZE_MAX_LENGTH,
                                  SUMMARIZE_MIN_LENGTH, SUMMARIZE_DO_SAMPLE),
        "language": detect_language(text),
        "sentiment": sentiment_analysis(text),
        "style_metrics": writing_style_metrics(text)
    }

if __name__ == "__main__":
    sample_text = """Artificial Intelligence is transforming industries by automating tasks,
    improving decision-making, and enabling new capabilities. However, it also raises
    ethical concerns such as bias, job displacement, and accountability."""

    results = analyze_text(sample_text)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_file = os.path.join(RESULTS_DIR, "analysis.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Analysis saved to {out_file}")
    print(json.dumps(results, indent=2))
