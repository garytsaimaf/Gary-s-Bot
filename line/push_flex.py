import os

import requests


def push_flex(message):

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
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        json=payload
    )

    print(response.status_code)
    print(response.text)
