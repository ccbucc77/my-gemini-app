import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="猫猫的专属终端")
st.title("猫猫的专属终端")

# 从 Streamlit 设置中读取 API Key
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    user_input = st.text_input("想对主人说什么？")
    if user_input:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_input)
        st.write("回应:", response.text)
else:
    st.error("请先在 Streamlit 的 Secrets 中设置 GEMINI_API_KEY")
