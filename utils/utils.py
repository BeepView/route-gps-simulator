import requests


def post(url: str, data: dict):
    headers = {"Authorization": "something"}
    return requests.post(url, json=data, headers=headers)
