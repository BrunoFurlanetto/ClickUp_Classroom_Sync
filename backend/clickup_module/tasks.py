import os

import requests
from dotenv import load_dotenv

from backend.clickup_module.clickup_utils import save_list_in_db
from backend.infra.repository.lists_in_clickup_repository import ListsInClickUpRepository
from backend.infra.repository.spaces_repository import SpacesRepository

load_dotenv()


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
