import streamlit as st

# 세션 상태 초기화
if 'input_text' not in st.session_state:
    st.session_state.input_text = ''

prompt = st.text_input("영상 관련 질문을 입력하세요", key="input_text", placeholder='영상에 대해 자세히 설명해주세요')

process = st.button("영상 분석")

if process:
    
    prompt = st.session_state.input_text + "??"