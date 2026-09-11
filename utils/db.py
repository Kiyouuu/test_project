import pymysql


def get_connection():
    connection = pymysql.connect(
        host="192.168.183.128",
        port=3306,
        user="root",
        password="123456",
        database="yubei",
        charset="utf8mb4"
    )

    return connection


def query(sql, params=None):
    connection = get_connection()

    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

if __name__ == "__main__":
    result = query(
        "SELECT * FROM emp"
    )

    print(result)