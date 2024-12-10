import requests
import credentials

token = credentials.bot_token
url = f"https://api.telegram.org/bot{token}/getUpdates"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for result in data['result']:
        print("Chat ID:", result['message']['chat']['id'])
else:
    print("Error:", response.status_code, response.text)