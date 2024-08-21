import streamlit as st
import google.generativeai as genai

st.title("Welcome to Gemini chatbot")

genai.configure(api_key="AIzaSyBVIDQ57PbmY5vaAWR5JoYYLCaJTDbq6oE")

text = st.text_input("Enter your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message(text)
st.write(response.text)