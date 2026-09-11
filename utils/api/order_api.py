from utils.request import request


def get_order(base_url, headers):
    url = base_url + "/get"

    response = request(
        "GET",
        url,
        headers=headers
    )

    return response


def create_order(base_url, headers, order_data):
    url = base_url + "/post"

    response = request(
        "POST",
        url,
        headers=headers,
        data=order_data
    )

    return response