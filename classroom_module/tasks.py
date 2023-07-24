from googleapiclient.discovery import build

from classroom_module.auth import get_credentials
from clickup_module.clickup_utils import create_list
from infra.repository.courses_in_classroom_repository import CoursesInClassroomRepository


def verify_new_courses():
    service = build('classroom', 'v1', credentials=get_credentials())
    results = service.courses().list().execute()
    courses = results.get('courses', [])

    for course in courses:
        if course['courseState'] == 'ACTIVE':
            if not CoursesInClassroomRepository().get(course_id=int(course['id'])):
                create_list(course)
