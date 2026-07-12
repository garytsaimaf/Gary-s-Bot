from line.flex import article_button


def build_flex(summary, articles):

    body = []

    body.append(
        {
            "type": "text",
            "text": "🩺 Gary Medical Intelligence Assistant",
            "weight": "bold",
            "size": "lg"
        }
    )

    body.append(
        {
            "type": "text",
            "text": "📌 Summary",
            "weight": "bold",
            "margin": "xl"
        }
    )

    body.append(
        {
            "type": "text",
            "text": summary,
            "wrap": True,
            "size": "sm"
        }
    )

    body.append(
        {
            "type": "text",
            "text": "📚 Top Intelligence",
            "weight": "bold",
            "margin": "xl"
        }
    )

    numbers = [
        "①",
        "②",
        "③",
        "④",
        "⑤",
        "⑥"
    ]

    for i, item in enumerate(articles):

        body.append(
            {
                "type": "text",
                "text": f"{numbers[i]} {item['title']}",
                "weight": "bold",
                "wrap": True,
                "margin": "lg"
            }
        )

        body.append(
            {
                "type": "text",
                "text": item["why"],
                "wrap": True,
                "size": "sm"
            }
        )

        body.append(
            article_button(
                "🔗 Open Article",
                item["link"]
            )
        )

        body.append(separator())

    return {
        "type": "flex",
        "altText": "Daily Oncology Intelligence",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": body
            }
        }
    }
