from dotenv import load_dotenv
import os   
import streamlit as st
import google.generativeai as genai  

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  

PERSONAS = {
    "General Assistant": "You are a helpful, friendly, and knowledgeable AI assistant. Provide clear and accurate information.",
    "Code Tutor": "You are an expert programming tutor. Explain coding concepts clearly with examples. Ask follow-up questions to ensure understanding.",
    "Creative Writer": "You are a creative writing assistant. Help with brainstorming, storytelling, and creative projects. Be imaginative and inspiring.",
    "Data Analyst": "You are a data analysis expert. Help interpret data, suggest analysis methods, and explain statistical concepts clearly.",
    "Business Consultant": "You are a professional business consultant. Provide strategic advice, market insights, and practical business solutions.",
}

st.set_page_config(page_title="Bot",page_icon="🤖 ",layout="wide")
st.title("Conversation Bot with Gemini")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "persona" not in st.session_state:
    st.session_state.persona = "General Assistant"

if "chat" not in st.session_state:
    # Start Gemini chat with selected persona
    st.session_state.chat = genai.GenerativeModel("gemini-1.5-pro-002").start_chat(
        history=[{"role": "system", "parts": [PERSONAS[st.session_state.persona]]}]
    )

with st.sidebar:
    st.header("Configuration")
    persona = st.selectbox("Choose AI Persona:", list(PERSONAS.keys()), key="persona_select")

    if persona != st.session_state.persona:
        st.session_state.persona = persona
        st.session_state.chat_history = []
        st.session_state.chat = genai.GenerativeModel("gemini-1.5-pro-002").start_chat(
            history=[{"role": "system", "parts": [PERSONAS[persona]]}]
        )
        st.rerun()

    # Clear conversation
    if st.button("Clear Conversation"):
        st.session_state.chat_history = []
        st.session_state.chat = genai.GenerativeModel("gemini-1.5-pro-002").start_chat(
            history=[{"role": "system", "parts": [PERSONAS[st.session_state.persona]]}]
        )
        st.rerun()

def get_response(question):
    try:
        response = st.session_state.chat.send_message(question, stream=False)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

user_input = st.text_input("", placeholder="Type your message here...", key="input")
submit = st.button("Send")

if submit and user_input:
    # Save user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

st.subheader("Conversation")

for message in st.session_state.chat_history:
    role = message["role"]
    content = message["content"]
    st.write(f"**{role.capitalize()}**: {content}")
