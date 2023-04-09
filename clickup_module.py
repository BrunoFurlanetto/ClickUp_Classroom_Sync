import requests
from local_settings import *


def new_task_in_list(list_id):
    url = f'https://api.clickup.com/api/v2/list/{list_id}/task'
    request_header = {
        'Authorization': clickup_api_key,
        'Content-Type': 'application/json'
    }

    new_task = {
        'name': 'Teste',
        'description': 'Testando a funcionalidade de criar atividades'
    }

    r = requests.post(url=url, json=new_task, headers=request_header)
