import os

from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

from auth import authentication
from classroom import consult_courses
from local_settings import *

# --------------------------------- Block to check login requirement ---------------------------------------------------
credentials = None

if os.path.exists('token.json'):
    credentials = Credentials.from_authorized_user_file('token.json', scopes)

if not credentials or not credentials.valid:
    credentials = authentication(credentials)
# ----------------------------------------------------------------------------------------------------------------------

try:
    courses_and_work = consult_courses(credentials, 'ACTIVE')
except HttpError as error:
    print('An error occurred: %s' % error)
