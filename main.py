from googleapiclient.discovery import build
from rocketry import Rocketry
from rocketry.conds import daily, after_fail

from classroom_module.auth import get_credentials
from infra.repository.works_in_clickup_repository import WorksInClickUpRepository
from notifications.notifications import Alert

app = Rocketry()


@app.task(daily.between('14', '20'), execution='thread')
def verify_new_works():
    service = build('classroom', 'v1', credentials=get_credentials())
    results = service.courses().list().execute()
    courses = results.get('courses', [])

    for course in courses:
        course_work_results = service.courses().courseWork().list(courseId=course['id']).execute()
        course_work = course_work_results.get('courseWork', [])

        for work in course_work:
            if not WorksInClickUpRepository().get(work_id=int(work['id'])):
                Alert(
                    f'New Work in {course["name"]}',
                    f'New Work present in {course["name"]}, initiated sync!'
                ).warning()

                raise Exception()


app.task(daily.between('14', '20'), func_name='verify_new_courses', path='classroom_module/tasks.py', execution='thread')
app.task(daily.between('14', '20'), func_name='verify_lists', path='clickup_module/tasks.py', execution='thread')
app.task(after_fail(verify_new_works), func_name='add_new_work_in_clickup', path='main_task.py', execution='thread')

if __name__ == "__main__":
    app.run()
