import os

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from classroom_module.config.scopes import scopes
from google.oauth2.credentials import Credentials


def authentication(creds):
    # If there are no (valid) credentials available, let the user log in.
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            '../credentials.json', scopes)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('../token.json', 'w') as token:
        token.write(creds.to_json())

    return creds


def get_credentials():
    credentials = None

    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', scopes)

    if not credentials or not credentials.valid:
        credentials = authentication(credentials)

    return credentials
