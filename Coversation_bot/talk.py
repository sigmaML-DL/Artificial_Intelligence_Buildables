from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTERAI_API_KEY")
)

PERSONAS = {
    "General Assistant": "You are a helpful and knowledgeable AI assistant.",
    "Code Tutor": "You are an expert programming tutor. Explain clearly with examples.",
    "Creative Writer": "You are a creative writing assistant. Be imaginative and inspiring.",
}

st.set_page_config(page_title="Echo", page_icon="🌀", layout="wide")
st.title("Echo - Your AI Companion")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat_history_archive" not in st.session_state:
    st.session_state.chat_history_archive = []
if "persona" not in st.session_state:
    st.session_state.persona = "General Assistant"

with st.sidebar:
    persona = st.selectbox("Category", list(PERSONAS.keys()))
    if persona != st.session_state.persona:
        st.session_state.persona = persona
        st.session_state.chat_history = []
        st.rerun()

    if st.button("Clear"):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")
    if st.button("History"):
        st.write("### Chat History")
        if not st.session_state.chat_history_archive:
            st.info("No past conversations yet.")
        else:
            for i, conv in enumerate(st.session_state.chat_history_archive, 1):
                st.write(f"**Conversation {i}:**")
                for msg in conv:
                    st.write(f"{msg['role'].capitalize()}: {msg['content']}")
                st.markdown("---")

def get_response(question):
    try:
        messages = [{"role": "system", "content": PERSONAS[st.session_state.persona]}]
        messages += st.session_state.chat_history
        messages.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3.1:free", 
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

user_input = st.text_input("", placeholder="Type your message here...")
if st.button("Send") and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    answer = get_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": answer})

    st.session_state.chat_history_archive.append(list(st.session_state.chat_history))
    st.session_state.chat_history = [{"role": "assistant", "content": answer}]


st.subheader("Conversation")
for msg in st.session_state.chat_history:
    if msg["role"] == "assistant":
        st.write(msg["content"])
