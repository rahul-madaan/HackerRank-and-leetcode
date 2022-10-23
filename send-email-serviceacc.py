from google.oauth2 import service_account
from googleapiclient.discovery import build
SERVICE_ACCOUNT_FILE="srvice-account-creds.json"
credentials = service_account.Credentials.from_service_account_file(
    filename=SERVICE_ACCOUNT_FILE,
    scopes=['https://mail.google.com/'],
    subject='rm584@snu.edu.in')
service_gmail = build ('gmail','v1', credentials=credentials)
response = service_gmail.users ().getProfile(userId='me').execute()
print(response)