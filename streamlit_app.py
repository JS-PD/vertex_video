import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
from googleapiclient.discovery import build

# Streamlit Cloud 환경 변수에서 서비스 계정 키 파일 내용 가져오기
credentials_info = st.secrets["gcp_service_account"]["GOOGLE_APPLICATION_CREDENTIALS"]

# 서비스 계정 인증 정보 생성
credentials = service_account.Credentials.from_service_account_info(credentials_info)

# GCS 클라이언트 초기화 (인증 정보 포함)
storage_client = storage.Client(credentials=credentials)
