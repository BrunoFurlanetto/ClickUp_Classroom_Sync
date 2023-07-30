from datetime import datetime
import os
import requests
from dotenv import load_dotenv

from backend.infra.repository.lists_in_clickup_repository import ListsInClickUpRepository
from backend.infra.repository.spaces_repository import SpacesRepository
from backend.notifications.notifications import Alert

load_dotenv()


def create_task_in_list(list_id, work_name, description, work_link, due_datetime):
    url = f'https://api.clickup.com/api/v2/list/{list_id}/task'

    request_header = {
        'Authorization': os.getenv('clickup_api_key'),
        'Content-Type': 'application/json'
    }

    new_task = {
        'name': work_name,
        'description': f'{description}\n\n{work_link}',
        'due_date_time': True,
        'due_date': int(due_datetime.timestamp() * 1000) if due_datetime else None,
        'priority': check_priority(due_datetime),
    }

    r = requests.post(url=url, json=new_task, headers=request_header)

    if r.status_code != 200:
        Alert(
            'Conection with ClickUp API Failed',
            f'Connection to ClickUp API failed while trying to add a task. Classroom course not synced ({r.json()["err"]})'
        ).warning()

    return r.status_code, r.json()['id']


def check_priority(due_date):
    diff = datetime.today() - due_date

    if diff.days < 15:
        return 4
    elif 15 < diff.days < 20:
        return 3
    elif 20 < diff.days < 30:
        return 2
    else:
        return 1


def delete_task_in_clickup(task_id):
    url = "https://api.clickup.com/api/v2/task/" + task_id

    request_header = {
        'Authorization': os.getenv('clickup_api_key'),
        'Content-Type': 'application/json'
    }

    r = requests.delete(url, headers=request_header)


def save_list_in_db(new_list):
    ListsInClickUpRepository().insert(
        list_id=new_list['id'],
        list_name=new_list['name'],
        clickup_space=new_list['space']['id']
    )


def create_list(course):
    space_id = SpacesRepository().select_all()[0].space_id
    url = f'https://api.clickup.com/api/v2/space/{space_id}/list'

    request_header = {
        'Authorization': os.getenv('clickup_api_key'),
        'Content-Type': 'application/json'
    }

    new_list = {
        'name': course['name'],
        'content': course['section']
    }

    r = requests.post(url=url, json=new_list, headers=request_header)

    if r.status_code == 200:
        data = r.json()

        try:
            ListsInClickUpRepository().insert(
                list_id=data['id'],
                list_name=data['name'],
                clickup_space=data['space']['id']
            )

            return data['id']
        except Exception as e:
            Alert(
                'New list not save in local database',
                f'New list, related to {course["name"]}, was not saved in local database. Necessary action! ({e})'
            ).error()
    elif r.json()['err'] == 'List name taken':
        return ListsInClickUpRepository().get(list_name=course['name']).list_id
    else:
        Alert(
            'Connection with ClickUp API Failed',
            f'Connection to ClickUp API failed while trying to add a list. Classroom course not synced ({r.json()["err"]})'
        ).warning()


def delete_list(list_id):
    url = f'https://api.clickup.com/api/v2/list/{list_id}'

    headers = {
        "Content-Type": "application/json",
        "Authorization": os.getenv('clickup_api_key')
    }

    response = requests.delete(url, headers=headers)

    if response.status_code != 200:
        Alert(
            'Connection with ClickUp API Failed',
            f'Connection to ClickUp API failed while trying to delete a list. There are remote lists not saved in the '
            f'local database! ({response.json()["err"]})'
        ).warning()
