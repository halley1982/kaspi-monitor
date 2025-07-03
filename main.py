import requests

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
