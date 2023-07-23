from googleapiclient.discovery import build

from classroom_module.auth import get_credentials
from infra.repository.courses_in_classroom_repository import CoursesInClassroomRepository
from notifications.notifications import Alert


def verify_new_courses():
    service = build('classroom', 'v1', credentials=get_credentials())
    results = service.courses().list().execute()
    courses = results.get('courses', [])

    for course in courses:
        if not CoursesInClassroomRepository().get(course_id=int(course['id'])):
            Alert(
                'New course in Classroom',
                f'{course["name"]} not in the local database, plase register and link to a ClickUp list!'
            ).warning()

            break
