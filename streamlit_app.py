import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage
from googleapiclient.discovery import build

# GCS에서 파일 다운로드
storage_client = storage.Client()
bucket = storage_client.bucket("psychic-expanse-425002-r3-bucket-01")
blob = bucket.blob("secret.json")
with open('temp_credentials.json', 'wb') as file_obj:
    blob.download_to_file(file_obj)

credentials = service_account.Credentials.from_service_account_file(
    "temp_credentials.json"
)
storage_client = storage.Client(credentials=credentials)

# Google API 클라이언트 생성 (예: Google Sheets API)
service = build('sheets', 'v4', credentials=credentials)

# Google Sheets API 사용 예시
sheet = service.spreadsheets().get(spreadsheetId='your-spreadsheet-id').execute()
st.write(sheet)

