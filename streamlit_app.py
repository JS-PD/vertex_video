import os
import json
import base64
import streamlit as st

# Base64 인코딩된 문자열을 디코딩하여 JSON 객체로 변환
decoded_credentials = base64.b64decode(st.secrets["encoded_google_credentials"])
credentials_info = json.loads(decoded_credentials)
credentials_path = '/tmp/credentials.json'

# 임시 파일에 인증 정보를 저장
with open(credentials_path, 'w') as f:
    json.dump(credentials_info, f)

# 환경 변수 설정
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

print(decoded_credentials)
