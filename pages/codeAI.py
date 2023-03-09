import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


# region 说明
with st.sidebar:
    st.success(
        """CodeAI
        使用OpenAI的[CodeX](https://platform.openai.com/docs/models/codex), training data contains both natural language and billions of lines of public code from GitHub. 
        \n最擅长 Python, 也精通其他各种语言。
        """)
    st.warning("""Tips 小技巧\n
    1. Specify the language
    2. 给AI写个开头，比如函数头
    3. 告诉AI你用的库
    4. 使用函数内注释来说明函数的作用
    5. 给AI举个例子
    """)
    st.error("目前CodeX的服务器压力比较大，响应无法保证。")
# endregion
# region 模型选择
modelSelect = st.radio("选用哪个模型?", ("code-davinci-002", "code-cushman-001"))
string = ""
if modelSelect == "code-davinci-002":
    """最强大的模型，可以翻译人说的话到代码，也支持插入编写"""
if modelSelect == "code-cushman-001":
    """比Davinci更快更轻量"""
string = st.text_area("用户输入")
# endregion
# region 参数设置
isOneLine = st.checkbox("只输出一行", value=False)
isOneString = st.checkbox('只输出一个字符串（输入中中包含")', value=False)
"长度提示"
defalutMaxToken = 256
if st.button("一两句代码"):
    defalutMaxToken = 30
if st.button("一个简单的函数"):
    defalutMaxToken = 128
if st.button("一份简单的代码文件"):
    defalutMaxToken = 512
maxToken = st.slider("回答长度限制", 30, 2048 if modelSelect == "code-cushman-001" else 8000, defalutMaxToken,
                     key="maxTokenSlider")

stopToken = []
if isOneLine:
    stopToken.append("\n")
if isOneString:
    stopToken.append('"')
# endregion
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