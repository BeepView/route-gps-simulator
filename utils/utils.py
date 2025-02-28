import requests


def post(url: str, data: dict, api_key: str) -> requests.Response:
    headers = {"Authorization": api_key}
    return requests.post(url, json=data, headers=headers)
