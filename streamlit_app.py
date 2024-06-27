import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Streamlit Secrets에서 경로 가져오기
credentials_path = st.secrets["gcp_service_account"]["credentials_path"]

# 클라우드 스토리지에서 JSON 파일 읽어오기
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Google API 클라이언트 생성 (예: Google Sheets API)
service = build('sheets', 'v4', credentials=credentials)

# Google Sheets API 사용 예시
sheet = service.spreadsheets().get(spreadsheetId='your-spreadsheet-id').execute()
st.write(sheet)
