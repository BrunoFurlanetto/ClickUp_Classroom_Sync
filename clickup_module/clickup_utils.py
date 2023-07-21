import os
from datetime import datetime, timedelta
from pathlib import Path

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

    if r.status_code != 200:
        print('List not found in ClickUp, check the ID registered in the database')
