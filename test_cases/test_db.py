from utils.api.user_api import get_employee
from utils.db import query


def test_api_db_employee(headers, base_url):
    name = "柳岩"

    # 1. 调用员工查询接口
    response = get_employee(
        base_url,
        headers,
        name
    )

    # 2. 验证 API 请求成功
    assert response.status_code == 200

    # 3. 获取 API 返回结果
    result = response.json()

    # 4. 获取 API 返回的员工姓名
    api_name = result["args"]["name"]

    # 5. 查询 MySQL
    db_result = query(
        "SELECT * FROM emp WHERE name=%s",
        (name,)
    )

    # 6. 验证 API 返回的姓名
    assert api_name == name

    # 7. 验证数据库中存在这个员工
    assert len(db_result) > 0

    # 8. 验证 API 和数据库的员工姓名一致
    assert api_name == db_result[0]["name"]

def test_query_old_employee():
    result = query(
        "SELECT * FROM emp WHERE age > %s",
        (50,)
    )

    assert len(result) > 0

    for employee in result:
        assert employee["age"] > 50