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

    if isinstance(message, dict):

        payload = {
            "to": user,
            "messages": [message]
        }

    else:

        payload = {
            "to": user,
            "messages": [
                {
                    "type": "text",
                    "text": message
                }
            ]
        }

    response = requests.post(
        LINE_PUSH_API,
        headers=headers,
        json=payload
    )

    print(response.status_code)
    print(response.text)

    response.raise_for_status()
