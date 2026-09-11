from utils.request import request
from utils.api_path import USER_PATH


def get_user(base_url, headers):
    url = base_url + USER_PATH

    response = request(
        "GET",
        url,
        headers=headers
    )

    return response


def get_employee(base_url, headers, name):
    url = base_url + USER_PATH + "?name=" + name

    response = request(
        "GET",
        url,
        headers=headers
    )

    return response