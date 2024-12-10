import requests
import credentials

def send_message_via_telegram(chat_id, message):
    token = credentials.bot_token
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Create the payload for the message
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    # Perform the POST request
    response = requests.post(url, json=payload)

    # Check the response
    if response.status_code == 200:
        print(f"Message sent: {response.json()}")
    else:
        print(f"Error sending message: {response.status_code} - {response.text}")

send_message_via_telegram(credentials.chat_id, "Hello, this is a test message!")