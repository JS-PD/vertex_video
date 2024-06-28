import json

json_data = """
{
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkq...",
    "client_email": "my-email@my-project.iam.gserviceaccount.com",
    "client_id": "1234567890",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/my-email%40my-project.iam.gserviceaccount.com"
}
"""

try:
    loaded_json = json.loads(json_data)
    print("JSON is valid!")
except json.JSONDecodeError as e:
    print(f"JSON parsing error: {e}")
