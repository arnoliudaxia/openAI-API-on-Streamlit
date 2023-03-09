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
    st.warning("""Tips 小技巧\n
    1. Specify the language
    2. 给AI写个开头，比如函数头
    3. 指定使用库
    4. 使用函数内注释来说明函数的作用
    5. 给AI举个例子
    """)
    st.error("目前CodeX的服务器压力比较大，响应无法保证。")
    # st.markdown()
    modelSelect=st.radio("选用哪个模型?",("code-davinci-002","code-cushman-001"))
    string=""
    if modelSelect=="code-davinci-002":
        """最强大的模型，可以翻译人说的话到代码，也支持插入编写"""
        string=st.text_area("code-davinci-002")
    if modelSelect=="code-cushman-001":
        """比Davinci更快更轻量"""
        string=st.text_area("code-cushman-001")
    isOneLine=st.checkbox("只输出一行", value=False)
    isOneString=st.checkbox('只输出一个字符串（prompt中包含")', value=False)
    maxToken=st.slider("回答长度限制", 30, 2048 if modelSelect=="code-cushman-001" else 8000, 256)
    stopToken=[]
    if isOneLine:
        stopToken.append("\n")
    if isOneString:
        stopToken.append('"')
    if st.button("提交"):
        res = openai.Completion.create(
            model=modelSelect,
            prompt=string,
            temperature=0,
            max_tokens=maxToken,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=stopToken
        )
        st.balloons()
        st.code(res["choices"][0]["text"])