import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

@st.cache_resource
def get_model():
    return genai.GenerativeModel("gemini-2.5-flash")

model = get_model()
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("🎮 AI Visual Novel")

st.sidebar.title("Story Settings")

genre = st.sidebar.selectbox(
    "Select Genre",
    ["Fantasy", "Horror", "Sci-Fi", "Comedy", "Mystery"]
)

art_style = st.sidebar.selectbox(
    "Art Style",
    ["Anime", "Realistic", "Pixel Art", "Oil Painting", "Cyberpunk"]
)

st.write("Selected Genre:", genre)
st.write("Selected Art Style:", art_style)

prompt = f"""
Start a {genre} adventure.

Keep it around 80 words.

The story should feel immersive.
"""

if st.button("Start Adventure"):

    response = st.session_state.chat.send_message(prompt)

    st.write(response.text)