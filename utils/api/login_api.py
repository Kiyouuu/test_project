from utils.request import request
from utils.api_path import LOGIN_PATH


def login(base_url, username, password):
    data = {
        "username": username,
        "password": password
    }

    response = request(
        "POST",
        base_url + LOGIN_PATH,
        data=data
    )

    return response