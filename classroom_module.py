from datetime import datetime, timedelta

from googleapiclient.discovery import build


def consult_courses(credentials, status_course=None):
    service = build('classroom', 'v1', credentials=credentials)
    results = service.courses().list().execute()
    courses = results.get('courses', [])
    courses_and_works = []

    if not courses:
        return 'No courses found'

    if status_course:
        for course in courses:
            if course['courseState'] == status_course:
                courses_and_works.append({
                    'course_id': course['id'],
                    'course_name': course['name'],
                    'course_work': consult_works(course, service),
                })
    else:
        for course in courses:
            courses_and_works.append({
                'course_id': course['id'],
                'course_name': course['name'],
                'course_work': consult_works(course, service),
            })

    return courses_and_works


def consult_works(course, service):
    course_work_results = service.courses().courseWork().list(courseId=course['id']).execute()
    course_work = course_work_results.get('courseWork', [])
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

            works.append({
                'id': work['id'],
                'name': work['title'],
                'due_date': due_date_in_datetime,
                'description': work.get('description', ''),
                'link_to_work': work.get('alternateLink')
            })

        return works
