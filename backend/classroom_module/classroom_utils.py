from datetime import datetime, timedelta

from googleapiclient.discovery import build
from backend.infra.repository.works_in_clickup_repository import WorksInClickUpRepository


def consult_courses(credentials):
    service = build('classroom', 'v1', credentials=credentials)
    results = service.courses().list().execute()
    courses = [course for course in results.get('courses', []) if course["courseState"] == "ACTIVE"]
    courses_and_works = []

    for course in courses:
        course_work_results = service.courses().courseWork().list(courseId=course['id']).execute()
        course_work = course_work_results.get('courseWork', [])

        courses_and_works.append({
            'course_id': course['id'],
            'course_name': course['name'],
            'course_works': consult_works(course_work),
        })

    return courses_and_works


def consult_works(course_work):
    utc_offset = timedelta(hours=-3)
    works = []

    if course_work:
        for work in course_work:
            due_date_in_datetime = None

            if work.get('dueDate', None):
                due_date_in_datetime = datetime(
                    year=work['dueDate']['year'],
                    month=work['dueDate']['month'],
                    day=work['dueDate']['day'],
                    hour=work['dueTime']['hours'],
                    minute=work['dueTime'].get('minutes', 00)
                ) + utc_offset

            if not check_work_in_database(work['id']):
                works.append({
                    'id': work['id'],
                    'name': work['title'],
                    'due_date': due_date_in_datetime,
                    'description': work.get('description', ''),
                    'link_to_work': work.get('alternateLink')
                })

        return works


def check_work_in_database(work_id):
    work_in_database = WorksInClickUpRepository().get(work_id=int(work_id))

    if work_in_database:
        return True
    else:
        return False
