import json
import pytest
from utils.request import request
import allure
from utils.api_path import LOGIN_PATH
from utils.data_loader import load_json
from utils.api.login_api import login


test_data = load_json("test_data/login_data.json")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "data",
    test_data,
    ids=[item["case_name"] for item in test_data]
)
@allure.title("登录接口测试")
def test_login(data, base_url):

    username = data["username"]
    password = data["password"]
    expected_status = data["expected_status"]

    url = base_url + LOGIN_PATH

    with allure.step("发送登录请求"):
        allure.attach(
        str(data),
        "请求参数",
        allure.attachment_type.TEXT
    )

    response = login(base_url, username, password)

    with allure.step("获取响应"):
        result = response.json()

        allure.attach(
            str(result),
            "响应内容",
            allure.attachment_type.TEXT
    )

    with allure.step("验证登录结果"):
        # assert response.status_code == expected_status
        assert result["json"]["username"] == username
        assert result["json"]["password"] == password

def test_login_user(login_user, base_url):

    response = request(
        "POST",
        base_url + LOGIN_PATH,
        data=login_user
    )

    result = response.json()

    assert response.status_code == 200
    assert result["json"]["username"] == login_user["username"]
    assert result["json"]["password"] == login_user["password"]

def test_login_factory(user_factory, base_url):
    user1 = user_factory("admin")
    user2 = user_factory("guest")

    response1 = request(
        "POST",
        base_url + LOGIN_PATH,
        data=user1
    )
    response2 = request(
        "POST",
        base_url + LOGIN_PATH,
        data=user2
    )
    result1 = response1.json()
    result2 = response2.json()

    assert result1["json"]["username"] == user1["username"]
    assert result1["json"]["password"] == user1["password"]

    assert result2["json"]["username"] == user2["username"]
    assert result2["json"]["password"] == user2["password"]

@pytest.mark.skip(reason="暂时跳过测试")
def test_skip():
    print("这个测试不会执行")