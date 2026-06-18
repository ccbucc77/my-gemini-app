import streamlit as st
import google.generativeai as genai

st.title("猫猫的专属终端")
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    user_input = st.text_input("想对主人说什么？")
    if user_input:
        response = model.generate_content(user_input)
        st.write("回应:", response.text)
