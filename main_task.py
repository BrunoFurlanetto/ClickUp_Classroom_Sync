from googleapiclient.errors import HttpError

from classroom_module.auth import get_credentials
from classroom_module.classroom_utils import consult_courses
from clickup_module.clickup_utils import create_task_in_list, delete_task_in_clickup
from infra.repository.courses_in_classroom_repository import CoursesInClassroomRepository
from infra.repository.works_in_clickup_repository import WorksInClickUpRepository

from notifications.notifications import Alert


def add_new_work_in_clickup():
    try:
        courses_and_works = consult_courses(get_credentials(), 'ACTIVE')

        for course in courses_and_works:
            course_in_clickup = CoursesInClassroomRepository().get(course_id=int(course['course_id']))

            for work in course['course_works']:
                status_code, work_id = create_task_in_list(
                    course_in_clickup.clickup_list_id,
                    work['name'],
                    work['description'],
                    work['link_to_work'],
                    work['due_date']
                )

                if status_code == 200:
                    try:
                        WorksInClickUpRepository().insert(
                            work_id=work['id'],
                            task_clickup_id=work_id,
                            work_title=work['name'],
                            due_date=work['due_date'],
                            description=work['description'],
                            link_to_work=work['link_to_work'],
                            classrom_course_id=course['course_id'],
                        )
                    except Exception as e:
                        Alert('DB error', f'Error connecting to local database!({e})').error()
                        delete_task_in_clickup(work_id)
    except HttpError as error:
        Alert('Conecion error', f'Error when trying to communicate with the APIs!({error})').error()
