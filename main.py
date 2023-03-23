import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from auth import authentication
from local_settings import *

# --------------------------------- Block to check login requirement ---------------------------------------------------
credentials = None

if os.path.exists('token.json'):
    credentials = Credentials.from_authorized_user_file('token.json', scopes)

if not credentials or not credentials.valid:
    credentials = authentication(credentials)
# ----------------------------------------------------------------------------------------------------------------------

try:
    service = build('classroom', 'v1', credentials=credentials)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')

    # Prints the names of the first 10 courses.
    print('Courses:')
    for course in courses:
        if course['courseState'] == 'ACTIVE':
            course_work_results = service.courses().courseWork().list(courseId=course['id']).execute()
            course_work = course_work_results.get('courseWork', [])

            if not course_work:
                print(f'course: {course["name"]}: No course work found.')
            else:
                # Print the course work for the course
                for work in course_work:
                    # work_title = work.get('title')
                    # work_description = work.get('description')
                    # print(f'course: {course["name"]} - course work: {work_title}')
                    print(work)
                    break

except HttpError as error:
    print('An error occurred: %s' % error)
