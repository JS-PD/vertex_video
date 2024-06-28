import os
import json
import streamlit as st

try:
    # JSON 데이터 파싱
    credentials_info = json.loads(st.secrets["google_credentials"])
    credentials_path = '/tmp/credentials.json'

    # 임시 파일에 인증 정보 저장
    with open(credentials_path, 'w') as f:
        json.dump(credentials_info, f)

    # 환경 변수 설정
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
except json.JSONDecodeError as e:
    st.error(f"JSON parsing error: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")

st.markdown(st.secrets["google_credentials"])
