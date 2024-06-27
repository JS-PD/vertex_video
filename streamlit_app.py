import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
from googleapiclient.discovery import build

# Streamlit Cloud 환경 변수에서 서비스 계정 키 파일 내용 가져오기
print(st.secrets["gcp_service_account"]["GOOGLE_APPLICATION_CREDENTIALS"])
