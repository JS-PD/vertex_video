import os
import json
import streamlit as st

try:
    # JSON 데이터 파싱
json_data = 
"""
{
  \" type\" : \" service_account\" ,
  \" project_id\" : \" psychic-expanse-425002-r3\" ,
  \" private_key_id\" : \" 42abbe4cda156c487f8af36ca742be554e4ba154\" ,
  \" private_key\" : \" -----BEGIN PRIVATE KEY-----\\n MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCZlXR4jdDPRQcV\\n 10TRrMsU6Z3Nv6IdT/U2x0QnenTFCq/hFUpLWz1mkpGbQAZBLzMwXRbUZ6Uwe4yL\\n ILrvBtYc6bTtySqnqlRIbYgKO5JMS7M9FodMoxyQqwChcSEKyMxvJWs6l/n9kGLt\\n sOKW1KggAjzfXFi3m21AkJ0f/j35NZ0lcdVOYhoB0kTWxaT6ff9LRkYSWf6cl/sF\\n vWcrKbwsfnoyhdyGFy3P1SJZsZYqo/R5x3m6a8HT5HoiwMh3NctQ9+UwUFEIGhzs\\n aOj0CRBU0ktdkMxhknuBKMqnvXuDAiZQ5cKC5z8M2ihNiQRsOIs2LpsyosCEqyMX\\n WN/pU4b5AgMBAAECggEAC4HLY3HqrHDlTkFd/mC2KYe0Y1NBk/Um7/b/l/6gi5fY\\n pCJaeelo4QvHvYxPO6iL6wp6eKkYUxjap5zo7JpERg/LlspM+Bl2raOJPw0GEdHV\\n KNVMh1UsQXmSd0YY3ew8BvLUhSQYXqNoChuH6pmdzCImyexrGDycs6ryHtDHd2mr\\n dvKQx6aYkKjdpdfDFCtx+Js8b2JODwz+rUshJkG9O5z48pv2XJFabSJw9WsujU2D\\n ad6qaZ5OrIELvXLGMttyZQ+imm3XpRO9+UJtrddtcScO7RkBsBO5HMEwDNNxyVlZ\\n mKehourV1iBma8PfJK2vwESgISI3uqcu6mjWj64HNQKBgQDLMpLtCMfvJiysMkeT\\n a7R9ya8KWeTmd1p3XpeX+gbSEg2vYc5fHUZOFLr0P0efOn/3bQKuN48dPborrpf/\\n TvSirA7+znWn7ezJzWO5fRmw1xXJcXd47e5AvCjnbJ4IslBmlUIhO2x+b5qddgLb\\n i1fzWiFOk4nJzqH3WYUS081gnQKBgQDBfmXPWksoRugrtPWEEI1Oxn2RN5CqBBrs\\n XaIaqhxBMNyAcHPfCD/HvGmeAcxpYIQW8QCUfjkujD98qNDWhfK1DwEvyUFgmTmW\\n RaUdhAqqFJC46t080gZq5F6kQ1+l3fFYMOF8rWS843Z9tUTCkn/9Oh/dcPpyAYvO\\n gTggAVRrDQKBgBRHxuxLfRD8YWcKWaR4Enqff43r7PGnperWERFFDhs3XBBOFbfe\\n hx7R6Nrp2e8lepIqWiMjPnBvsb4cXeVIbxgxTgnWd128XG7DxhlESCUjQnRpk8AJ\\n F0d0wCxg5eD+UxH6AbCpaqmv3+GpXp2k6bFLJJngFdeDfRzf3W1EoHHtAoGBAINo\\n MARuMfSckzh7oPGbvBvvuX9R2TFdsFsuC9VICgBMCrQ/qrGhjI89ag0g843tOkfK\\n TLaMMpFmNgeXLp1CQt6r3gZyC7Bq3y0rB0PQVN3FMbQj7TRM/obBqXStPNwMqsdW\\n Cwz9RRjy8ZnV7Wimzb1QKCvfenbKjgQkxdUWkhpRAoGAMzooyU0PiahMn9uHFOYe\\n tRTKTh2cInzY943mK8BwFX01+GHc5rSMedwZP7JFxeS7c8x5KkJWdcB15ia3hrOR\\n wMU1kW43pEwwUuIWLFXkbu1qvvpYo2zVySEkxiSGPkLOeqweT7vvu4tcT0cebTUi\\n 4SXo3mCCm4thEJ+NlbpqMKQ=\\n -----END PRIVATE KEY-----\\n \" ,
  \" client_email\" : \" vertex-gemini-api@psychic-expanse-425002-r3.iam.gserviceaccount.com\" ,
  \" client_id\" : \" 101856695395600940799\" ,
  \" auth_uri\" : \" https://accounts.google.com/o/oauth2/auth\" ,
  \" token_uri\" : \" https://oauth2.googleapis.com/token\" ,
  \" auth_provider_x509_cert_url\" : \" https://www.googleapis.com/oauth2/v1/certs\" ,
  \" client_x509_cert_url\" : \" https://www.googleapis.com/robot/v1/metadata/x509/vertex-gemini-api%40psychic-expanse-425002-r3.iam.gserviceaccount.com\" ,
  \" universe_domain\" : \" googleapis.com\" 
}


"""
    credentials_info = json.loads(json_data)
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
