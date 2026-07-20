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
You are an AI Visual Novel engine.

Genre: {genre}

Art Style: {art_style}

Return ONLY valid JSON.

The JSON format must be:

{{
    "story_text":"Story here",

    "image_prompt":"Detailed image prompt",

    "options":[
        "Choice 1",
        "Choice 2",
        "Choice 3"
    ]
}}

Rules:

1. Do NOT use markdown.

2. Do NOT use ```.

3. Return ONLY JSON.

4. Story should be around 80 words.

5. Image prompt should be highly detailed.

6. Generate exactly 3 choices.
"""

if st.button("Start Adventure"):
    response = st.session_state.chat.send_message(prompt)
    data = json.loads(response.text)
    story = data["story_text"]
    image_prompt = data["image_prompt"]
    options = data["options"]



#-----------------------------------------------------------
st.subheader("📖 Story")
st.write(story)

st.subheader("🎨 Image Prompt")
st.write(image_prompt)

st.subheader("🎮 Choose Your Action")
for option in options:
    if st.button(option):
        st.write("You selected:", option)
