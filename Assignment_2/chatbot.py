# Creating a Multipersonality chatbot

import streamlit as st 

st.title("MULTIVERSE OF CHATBOTS")
personality=st.selectbox("Who do you want to talk",["Career Guide","Data Analyst Trainer"," Personal ADVISOR"])

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
user_message=st.text_input(f"Hello! Let's chat, I'm your {personality}")

if st.button("SEND"):
    if user_message:
        ai_prompt=f"You are now a {personality}, Respond to the message staying completely in the character. Message is {user_message}"

        with st.spinner("In progress...."):
            response=client.models.generate_content(
                model="gemini-2.5-flash",
                contents=ai_prompt
            )
            st.success("Message Recieved !")
            st.write(response.text)
    else:
        st.warning("TextBox is empty, please write some text!")

