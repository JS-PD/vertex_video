# youtube_pipline.ipynb
from vertexai.generative_models import GenerativeModel, Part
import vertexai
import os
import json
import base64
from dotenv import load_dotenv

from google.cloud import storage
from pytube import YouTube

import streamlit as st

# API 키 정보 로드
load_dotenv()

    
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

os.environ['GOOGLE_CLOUD_PROJECT_ID'] = st.secrets["GOOGLE_CLOUD_PROJECT_ID"]
os.environ['GOOGLE_CLOUD_BUCKET_ID'] = st.secrets["GOOGLE_CLOUD_BUCKET_ID"]
