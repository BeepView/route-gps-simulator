import requests


def post(url: str, data: dict):
    return requests.post(url, json=data)
