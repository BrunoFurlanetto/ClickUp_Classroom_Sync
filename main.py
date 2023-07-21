import os

from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

from classroom_module.auth import authentication
from classroom_module.classroom_utils import consult_courses
from classroom_module.config.scopes import scopes
from clickup_module.clickup_utils import create_task_in_list
from infra.repository.courses_in_classroom_repository import CoursesInClassroomRepository

# --------------------------------- Block to check login requirement ---------------------------------------------------
credentials = None

if os.path.exists('token.json'):
    credentials = Credentials.from_authorized_user_file('token.json', scopes)

if not credentials or not credentials.valid:
    credentials = authentication(credentials)
# ----------------------------------------------------------------------------------------------------------------------

try:
    courses_and_works = consult_courses(credentials, 'ACTIVE')
    print(courses_and_works[0])
    # for course in courses_and_works:
    #     course_in_clickup = CoursesInClassroomRepository().get(course_id=course['course_id'])
    #
    #     if course_in_clickup.clickup_list_id == '6-901000498029-1':
    #         for work in course['course_works']:
    #             create_task_in_list(
    #                 course_in_clickup.clickup_list_id,
    #                 work['name'],
    #                 work['description'],
    #                 work['link_to_work'],
    #                 work['due_date']
    #             )
except HttpError as error:
    print('An error occurred: %s' % error)
