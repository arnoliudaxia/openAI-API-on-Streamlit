import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Hello OpenAI")

st.success("在左侧选择你想使用的AI助手")