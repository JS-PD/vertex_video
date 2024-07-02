import os
import base64
from dotenv import load_dotenv

import openai

import streamlit as st

# API 키 정보 로드
load_dotenv()

if os.environ['OPENAI_API_KEY'] == "":
    os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]["OPENAI_API_KEY"]

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# ChatGPT Demo")
st.sidebar.header("ChatGPT Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames."""
)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

#base64_image = encode_image("cat.webp")

# # User-provided prompt
if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})

    # st.session_state.messages.append({"role": "user", "content": [
    #         {"type": "text", "text": "다른 고양이로 바꿔줘"},
    #         {"type": "image_url", "image_url": {
    #             "url": f"data:image/png;base64,{base64_image}"}
    #         }
    #     ]})

    with st.chat_message("user"):
        st.write(prompt)
        
client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])

completion = client.chat.completions.create(
    model="gpt-4-turbo",
    #model="gpt-3.5-turbo",
    stream=True,
    messages=st.session_state.messages
    )

import time

final_answer = []
# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            for chunk in completion:
                # chunk 를 저장
                chunk_content = chunk.choices[0].delta.content
                # chunk 가 문자열이면 final_answer 에 추가
                if isinstance(chunk_content, str):
                    final_answer.append(chunk_content)
                    # 토큰 단위로 실시간 답변 출력


        placeholder = st.empty()
        full_response = ''
        for item in final_answer:
            full_response += item
            placeholder.markdown(full_response)
            time.sleep(0.02)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
