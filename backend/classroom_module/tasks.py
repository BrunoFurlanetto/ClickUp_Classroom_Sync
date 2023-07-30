from googleapiclient.discovery import build

from backend.classroom_module.auth import get_credentials
from backend.clickup_module.clickup_utils import create_list
from backend.infra.repository.courses_in_classroom_repository import CoursesInClassroomRepository


def verify_new_courses():
    service = build('classroom', 'v1', credentials=get_credentials())
    results = service.courses().list().execute()
    courses = [course for course in results.get('courses', []) if course['courseState'] == 'ACTIVE']

    for course in courses:
        if course['courseState'] == 'ACTIVE':
            if not CoursesInClassroomRepository().get(course_id=int(course['id'])):

                list_id = create_list(course)

                if list_id:
                    CoursesInClassroomRepository().insert(
                        course_id=course['id'],
                        course_name=course['name'],
                        clickup_list_id=int(list_id),
                    )
