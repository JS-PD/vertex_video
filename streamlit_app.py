# youtube_pipline.ipynb
from vertexai.generative_models import GenerativeModel, Part
import vertexai
import os
from dotenv import load_dotenv

from google.cloud import storage
from pytube import YouTube

import streamlit as st

# API 키 정보 로드
load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "secret.json"

vertexai.init(project=os.environ['GOOGLE_CLOUD_PROJECT_ID'], location="asia-northeast3")

def download_youtube(url):
    yt = YouTube(url) # YouTube 객체 생성    
    stream = yt.streams.get_highest_resolution() # 가장 높은 해상도의 스트림 선택
    # 현재 디렉토리에 동영상 다운로드
    file_path = stream.download(output_path="./videos")
    #print("Download complete!")
    st.sidebar.warning('영상을 다운로드하고 있습니다', icon="⚠️")
    return file_path

def upload_to_gcs(bucket, file_path, file_name): 
    # bucket에 파일을 업로드할 blob 객체 생성
    blob = bucket.blob(file_name) 
    # blob 객체를 통해 로컬 파일을 버킷에 업로드
    blob.upload_from_filename(file_path)
    st.sidebar.warning('영상을 분석하고 있습니다', icon="⚠️")
    #print("Upload complete!")

def delete_video(bucket, file_name, file_path):
    blob = bucket.blob(file_name)
    blob.delete()
    if os.path.exists(file_path):
        os.remove(file_path)
    st.sidebar.warning('처리가 완료었습니다', icon="⚠️")
    #print("Delete complete!")

bucket_name = os.environ['GOOGLE_CLOUD_BUCKET_ID']
bucket = storage.Client().bucket(bucket_name)
#url = "https://youtu.be/ZNjS9M0qJak?si=qMA9ONScwqBU8JSN"

video_url = st.text_input("Youtube URL을 입력하세요", 'https://youtu.be/WENUvclwo18?si=CngwTn2onM7PzZcP')

prompt = st.text_input("영상 관련 질문을 입력하세요", '영상에 대해 자세히 설명해주세요')

process = st.button("영상 분석")

if video_url:
    st.video(video_url)


if process:

    file_path = download_youtube(video_url)
    file_name = os.path.basename(file_path) 
    upload_to_gcs(bucket, file_path, file_name)
    video = Part.from_uri(
        uri=f"gs://{bucket_name}/{file_name}",
        mime_type="video/mp4",
    )
    prompt = prompt + ' 영상에 대한 설명을 단락으로 나누어 500자 이상으로 자세히 설명해주세요. 주요 문구나 강조해야할 부분이 있다면 강조 표시를 해주세요'

    print(prompt)
    contents = [prompt, video]

    model = GenerativeModel("gemini-1.5-pro-001")
    responses = model.generate_content(contents, stream=True)
    #IPython.display.display(IPython.display.Video(file_path, width=800 ,embed=True))

    #video_file = open(url, 'rb')
    #video_bytes = video_file.read()

    responses = model.generate_content(contents, stream=True)
    for response in responses:
        print(response.text.strip(), end="")
        st.markdown(response.text.strip())

    #print("\n\n")
    delete_video(bucket, file_name, file_path)

