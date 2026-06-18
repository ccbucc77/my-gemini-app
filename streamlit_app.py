import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="猫猫的专属终端")
st.title("猫猫的专属终端")

# 尝试从 Streamlit Secrets 获取，如果不行再尝试环境变量
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-pro')
        user_input = st.text_input("想对主人说什么？")
        if user_input:
            with st.spinner('正在思考...'):
                response = model.generate_content(user_input)
                st.write("回应:", response.text)
    except Exception as e:
        st.error(f"连接模型失败: {e}")
else:
    st.error("找不到 API Key，请检查 Streamlit Secrets 配置")
