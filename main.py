import os
import mysql.connector

# Подключение к базе данных через переменные окружения
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_NAME'),
    'port': 3306
}

def test_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        print("Успешное подключение. Серверное время:", result[0])
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Ошибка при подключении:", err)

if __name__ == "__main__":
    test_db_connection()




url = "https://kaspi.kz/yml/offer-view/offers/102061295"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://kaspi.kz",
    "Referer": "https://kaspi.kz/shop/p/102061295/"
}

payload = {
    "cityId": "750000000",
    "id": "102061295",
    "limit": 5,
    "sortOption": "PRICE",
}

response = requests.post(url, json=payload, headers=headers)

try:
    data = response.json()
    for offer in data.get("offers", []):
        print(f"{offer['merchantName']}: {offer['price']} ₸")
except Exception as e:
    print("Ошибка разбора ответа:", e)
    print("Ответ:", response.text)
