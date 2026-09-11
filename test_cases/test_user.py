from utils.request import request
from utils.api_path import USER_PATH
from utils.api.user_api import get_user
import allure
import pytest

@pytest.mark.regression
@allure.title("用户接口测试")

def test_user(headers, base_url):
    response = get_user(base_url, headers)

    print(response.json())

def test_username(test_username):
    print(test_username)