import logging
import requests
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    filename="logs/test.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

logger = logging.getLogger(__name__)

def request(method, url, data=None, headers=None):

    logger.info(f"开始发送 {method} 请求：{url}")

    try:
        if method == "GET":
            response = requests.get(
                url,
                headers=headers,
                timeout=5
            )

        elif method == "POST":
            response = requests.post(
                url,
                json=data,
                headers=headers,
                timeout=5
            )

        elif method == "PUT":
            response = requests.put(
                url,
                json=data,
                headers=headers,
                timeout=5
            )

        elif method == "DELETE":
            response = requests.delete(
                url,
                headers=headers,
                timeout=5
            )

        else:
            raise ValueError("不支持的请求方法")

    except Exception as e:
        logger.error(f"请求发生异常：{e}")
        raise

    response.raise_for_status()

    logger.info(f"请求成功，状态码：{response.status_code}")

    return response