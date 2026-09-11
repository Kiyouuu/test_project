import pytest
from utils.api.order_api import get_order, create_order


@pytest.mark.regression
def test_get_order(headers, base_url):
    response = get_order(base_url, headers)

    assert response.status_code == 200


@pytest.mark.regression
def test_create_order(headers, base_url):
    order_data = {
        "product": "手机",
        "price": 3999,
        "quantity": 1
    }

    response = create_order(
        base_url,
        headers,
        order_data
    )

    result = response.json()

    assert response.status_code == 200
    assert result["json"]["product"] == "手机"
    assert result["json"]["price"] == 3999
    assert result["json"]["quantity"] == 1