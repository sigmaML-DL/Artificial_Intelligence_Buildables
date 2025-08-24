import streamlit as st
from transformers import pipeline, AutoTokenizer
from textblob import TextBlob
from langdetect import detect, DetectorFactory
import langcodes

DetectorFactory.seed = 42  # deterministic language detection

st.set_page_config(page_title="Text Analysis Tool", layout="wide")
st.title("📝 Text Analysis Tool ")

# ------------------------------
# Load models once at startup
# ------------------------------
@st.cache_resource
def load_summarizers():
    return {
        "distilbart": pipeline("summarization", model="sshleifer/distilbart-cnn-12-6"),
        "t5-small": pipeline("summarization", model="t5-small")
    }

@st.cache_resource
def load_tokenizers():
    return {
        "gpt2": AutoTokenizer.from_pretrained("gpt2", use_fast=True),
        "bert-base-uncased": AutoTokenizer.from_pretrained("bert-base-uncased", use_fast=True)
    }

summarizers = load_summarizers()
tokenizers = load_tokenizers()

# ------------------------------
# Helper functions
# ------------------------------
def summarize_text(text, model_name, max_len=120, min_len=40):
    if model_name == "t5-small":
        text = "summarize: " + text
    out = summarizers[model_name](text, max_length=max_len, min_length=min_len, do_sample=False)
    return out[0]["summary_text"].strip()

def detect_language(text):
    try:
        lang_code = detect(text)
        return langcodes.get(lang_code).language_name().capitalize()
    except Exception:
        return "Unknown"

def sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.polarity
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return {"sentiment": sentiment, "polarity": round(float(polarity), 3)}

def tokenize(text, tokenizer):
    enc = tokenizer(text, add_special_tokens=True)
    return len(enc["input_ids"])

# ------------------------------
# Sidebar options
# ------------------------------
model_id = st.sidebar.selectbox("Select Summarization Model", ["distilbart", "t5-small"])
show_lang = st.sidebar.checkbox("Show Language Detection", value=True)
show_sent = st.sidebar.checkbox("Show Sentiment Analysis", value=True)
show_tokens = st.sidebar.checkbox("Show Token Counts", value=True)

# ------------------------------
# Main input
# ------------------------------
text_input = st.text_area("Enter your text here:", height=200)

if st.button("Analyze") and text_input.strip():
    st.subheader("🔹 Original Text")
    st.write(text_input)

    # Summarization
    summary = summarize_text(text_input, model_id)
    st.subheader("🟢 Summary")
    st.write(summary)

    # Language detection
    if show_lang:
        lang = detect_language(text_input)
        st.subheader("🌐 Language Detection")
        st.write(f"Detected language: **{lang}**")

    # Sentiment analysis
    if show_sent:
        sentiment = sentiment_analysis(text_input)
        st.subheader("💬 Sentiment Analysis")
        st.write(f"Sentiment: **{sentiment['sentiment']}** (Polarity: {sentiment['polarity']})")

    # Tokenization comparison
    if show_tokens:
        st.subheader("🔢 Token Counts (GPT-2 vs BERT)")
        gpt_count = tokenize(text_input, tokenizers["gpt2"])
        bert_count = tokenize(text_input, tokenizers["bert-base-uncased"])
        st.write(f"**GPT-2:** {gpt_count} tokens")
        st.write(f"**BERT:** {bert_count} tokens")
