import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Hello OpenAI")
# """本产品调用OpenAI API实现，使用需要用户具备构造prompt的能力。"""
aiType = st.selectbox(
     '你想使用哪个model?',
     ('CodeAI', 'Red', 'Green'))

if aiType == 'CodeAI':
    st.success(
    """CodeAI
    使用OpenAI的[CodeX](https://platform.openai.com/docs/models/codex), training data contains both natural language and billions of lines of public code from GitHub. 
    \n最擅长 Python, 也精通其他各种语言。
    """)
    modelSelect=st.radio("选用哪个模型?",("code-davinci-002","code-cushman-001"))
    string=""
    if modelSelect=="code-davinci-002":
        """最强大的模型，可以翻译人说的话到代码，也支持插入编写"""
        string=st.text_area("code-davinci-002")
    if modelSelect=="code-cushman-001":
        """比Davinci更快更轻量"""
        string=st.text_area("code-cushman-001")
    maxToken=st.slider("回答长度限制", 30, 2048 if modelSelect=="code-cushman-001" else 8000, 256)
    if st.button("提交"):
        res = openai.Completion.create(
            model=modelSelect,
            prompt=string,
            temperature=0,
            max_tokens=maxToken,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        st.balloons()
        st.code(res["choices"][0]["text"])