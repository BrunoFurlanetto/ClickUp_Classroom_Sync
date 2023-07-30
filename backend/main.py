from googleapiclient.discovery import build
from rocketry import Rocketry
from rocketry.conds import daily, after_fail

from classroom_module.auth import get_credentials
from infra.repository.works_in_clickup_repository import WorksInClickUpRepository
from notifications.notifications import Alert
from utils import test_connection, Loger
import argparse

global logger
app = Rocketry()
app.task(daily.between('14', '20'), func_name='verify_new_courses', path='backend/classroom_module/tasks.py')
app.task(daily.between('14', '20'), func_name='verify_lists', path='backend/clickup_module/tasks.py')


@app.task(daily.between('14', '20'))
def verify_new_works():
    logger.info('Initiated')
    test_connection()
    logger.info('Connection success')
    service = build('classroom', 'v1', credentials=get_credentials())
    results = service.courses().list().execute()
    courses = [c for c in results.get('courses', []) if c["courseState"] == "ACTIVE"]
    logger.info(f'Courses in class consulted. Find {len(courses)} courses active.')

    for course in courses:
        if course['courseState'] == 'ACTIVE':
            course_work_results = service.courses().courseWork().list(courseId=course['id']).execute()
            course_work = course_work_results.get('courseWork', [])
            logger.info(f'Course consult initiate: {course["name"]}')

            for work in course_work:
                if not WorksInClickUpRepository().get(work_id=int(work['id'])):
                    logger.info(f'Work {work["name"]} not in local database')

                    Alert(
                        f'New Work in {course["name"]}',
                        f'New Work present in {course["name"]}, initiated sync!'
                    ).warning()

                    raise Exception()

    logger.info(f'Finish consult. All Synced')


app.task(after_fail(verify_new_works), func_name='add_new_work_in_clickup', path='backend/main_task.py')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--logger", dest="logger", help="Log level", default=1, type=int)
    args = parser.parse_args()
    logger = Loger(args.logger)

    app.run()
