import os
import requests

from dotenv import load_dotenv

from infra.repository.lists_in_clickup_repository import ListsInClickUpRepository
from infra.repository.spaces_repository import SpacesRepository

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
        # 'priority': check_priority(due_datetime),
    }

    r = requests.post(url=url, json=new_task, headers=request_header)

    return r.status_code, r.json()['id']


def delete_task_in_clickup(task_id):
    url = "https://api.clickup.com/api/v2/task/" + task_id

    request_header = {
        'Authorization': os.getenv('clickup_api_key'),
        'Content-Type': 'application/json'
    }

    r = requests.delete(url, headers=request_header)


def verify_lists():
    spaces = SpacesRepository().select_all()
    id_lists_in_db = [list_db.list_id for list_db in ListsInClickUpRepository().select_all()]

    for space in spaces:
        url = f'https://api.clickup.com/api/v2/space/{space.space_id}/list'

        query = {
            "archived": "false"
        }

        request_header = {
            'Authorization': os.getenv('clickup_api_key'),
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=request_header, params=query)
        lists = response.json()['lists']

        for req_list in lists:
            if req_list['id'] in id_lists_in_db:
                save_list_in_db(req_list)


def save_list_in_db(new_list):
    ListsInClickUpRepository().insert(
        list_id=new_list['id'],
        list_name=new_list['name'],
        clickup_space=new_list['space']['id']
    )

    # TODO: Put new list discovery or error warnings
