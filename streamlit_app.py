import os
import json

import streamlit as st

# Secrets에서 JSON 데이터 로드
credentials_info = json.loads(st.secrets["google_credentials"])
credentials_path = '/tmp/credentials.json'

# 임시 파일에 인증 정보를 저장
with open(credentials_path, 'w') as f:
    json.dump(credentials_info, f)


print(credentials_path)
