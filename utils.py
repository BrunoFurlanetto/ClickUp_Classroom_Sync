from time import sleep

import requests


class Loger:
    def __init__(self, level):
        self.level = level

    def info(self, msg):
        if self.level >= 1:
            print(f"[ INFO ] {msg}")

    def debug(self, msg):
        if self.level >= 2:
            print(f'[ DEBUG ] {msg}')


def test_connection():
    while True:
        url = 'https://www.google.com'

        try:
            response = requests.get(url, timeout=5)  # Define o tempo limite da solicitação em 5 segundos
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            sleep(300)
        else:
            return
