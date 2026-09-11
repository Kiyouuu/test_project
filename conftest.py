import pytest
import json
from utils.request import request
from utils.data_loader import load_json

with open("config.json", "r") as f:
    config = json.load(f)

@pytest.fixture
def get_config():
    return config

@pytest.fixture
def base_url(get_config):
    return get_config["base_url"]

@pytest.fixture
def login_data(get_config):
    return get_config["login_data"]

@pytest.fixture
def token(test_username):
    print("当前用户:", test_username)
    url = "https://postman-echo.com/post"

    data = {
        "username": test_username,
        "password": "123456"
    }

    response = request(
        "POST",
        url,
        data=data
    )

    result = response.json()

    token = result["json"]["username"]

    return token

@pytest.fixture
def headers(token):
    headers = {
        "Authorization": "Bearer " + token
    }

    return headers

@pytest.fixture(params=["admin", "test"])
def test_username(request):
    return request.param

@pytest.fixture
def login_user(test_username):
    return {
        "username": test_username,
        "password": "123456"
    }

@pytest.fixture
def user_factory():

    def create_user(username):
        return {
            "username": username,
            "password": "123456"
        }

    return create_user