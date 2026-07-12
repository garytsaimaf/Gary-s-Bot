import os
import requests


LINE_PUSH_API = "https://api.line.me/v2/bot/message/push"


def push_text(message):

    token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

    user = os.environ["LINE_USER_ID"]

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "to": user,
        "messages": [
            message
        ]
    }

    response = requests.post(
        LINE_PUSH_API,
        headers=headers,
        json=payload
    )

    print(response.status_code)
    print(response.text)
