import os
import requests

from dotenv import load_dotenv


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
