import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("My AI Chatbot")

personality = st.sidebar.selectbox(
    "Choose Personality",
    ["Helpful", "Funny", "Teacher", "Professional"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_message := st.chat_input("Say something..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    prompt = f"""
You are a {personality} AI assistant.

User: {user_message}
"""

    response = model.generate_content(prompt)

    with st.chat_message("assistant"):
        st.write(response.text)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )