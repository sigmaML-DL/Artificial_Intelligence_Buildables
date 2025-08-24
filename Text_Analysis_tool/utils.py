from transformers import pipeline
from textblob import TextBlob
from langdetect import detect, DetectorFactory
import textstat

DetectorFactory.seed = 42
_SUMMARIZERS = {}

def get_summarizer(model_id: str):
    if model_id not in _SUMMARIZERS:
        _SUMMARIZERS[model_id] = pipeline("summarization", model=model_id)
    return _SUMMARIZERS[model_id]

def summarize_text(text: str, model_id: str,
                   max_length: int, min_length: int, do_sample: bool) -> str:
    if not text.strip():
        return ""
    summarizer = get_summarizer(model_id)
    in_text = text if "t5" not in model_id else f"summarize: {text}"
    try:
        out = summarizer(in_text, max_length=max_length,
                         min_length=min_length, do_sample=do_sample)
        return out[0]["summary_text"].strip()
    except Exception:
        return text.strip()[:max_length]

def detect_language(text: str) -> str:
    if not text.strip():
        return "unknown"
    try:
        return detect(text)
    except Exception:
        return "unknown"

def sentiment_analysis(text: str):
    blob = TextBlob(text or "")
    s = blob.sentiment
    return {"polarity": float(s.polarity), "subjectivity": float(s.subjectivity)}

def writing_style_metrics(text: str):
    safe = text if len(text.split()) >= 3 else "This is minimal text for stats."
    return {
        "flesch_reading_ease": textstat.flesch_reading_ease(safe),
        "word_count": len(safe.split()),
        "char_count": len(safe),
    }
