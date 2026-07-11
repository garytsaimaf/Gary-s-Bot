import os
import requests

CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
USER_ID = os.getenv("LINE_USER_ID")


def push_text(message):
    url = "https://api.line.me/v2/bot/message/push"

    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    body = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=body)

    print(response.status_code)
    print(response.text)
print("Token length:", len(CHANNEL_ACCESS_TOKEN) if CHANNEL_ACCESS_TOKEN else 0)
print("Token starts with:", CHANNEL_ACCESS_TOKEN[:10] if CHANNEL_ACCESS_TOKEN else "None")
