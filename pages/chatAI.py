import openai
import streamlit as st


with st.sidebar:
    st.success("""chatAI使用gpt-3.5-turbo-0301模型，是chatGPT的略微简化版本。""")
    st.warning("""Tips 小技巧\n
    1. 把话说清楚点
    2. Specify the answer format
    3. 把模型当做一个中学生，
    让模型逐步思考或讨论利弊。
    """)
if 'history' not in st.session_state:
    st.session_state['history'] = []
usrInput=st.text_area("用户输入")
TemperatureOptions={"非常严谨":0.0,"严谨":0.2,"平衡":0.4,"富有创造力":0.7}
modelTemperature=st.select_slider("模型创造力", options=["非常严谨","严谨","富有创造力","整活"],value="严谨")
if st.button("提交"):
    # region 构造对话
    messageHistory=[{"role": "system", "content": "You are a helpful AI assistant."}]
    for i in range(len(st.session_state['history'])):
        if i % 2 == 0:
            messageHistory.append({"role": "user", "content": st.session_state['history'][i]})
        else:
            messageHistory.append({"role": "assistant", "content": st.session_state['history'][i]})
    messageHistory.append({"role": "user", "content": usrInput})
    response=openai.ChatCompletion.create(
      model="gpt-3.5-turbo-0301",
      messages=messageHistory,
        temperature=TemperatureOptions[modelTemperature],
    )
    # endregion
    st.info("AI回答")
    # response
    answer=response["choices"][0]["message"]["content"]
    answer
    st.session_state['history'].append(usrInput)
    st.session_state['history'].append(answer)

if st.button("开启新对话（清空历史）"):
    st.session_state['history'] = []

st.session_state['history']
