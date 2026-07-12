from line.flex import article_button, separator


NUMBER = [
    "①",
    "②",
    "③",
    "④",
    "⑤",
    "⑥"
]


def build_flex(summary, articles):

    contents = []

    contents.append({
        "type": "text",
        "text": "🩺 早安！這是 Oncology HawkEye Daily",
        "weight": "bold",
        "size": "sm"
    })

    contents.append({
        "type": "text",
        "text": "Daily Oncology Intelligence",
        "size": "sm",
        "color": "#888888",
        "margin": "sm"
    })

    contents.append(separator())

    contents.append({
        "type": "text",
        "text": "📌 Summary",
        "weight": "bold",
        "margin": "lg"
    })

    contents.append({
        "type": "text",
        "text": summary,
        "wrap": True,
        "size": "sm"
    })

    contents.append(separator())

    contents.append({
        "type": "text",
        "text": "📚 Top Intelligence",
        "weight": "bold",
        "margin": "lg"
    })

    for i, item in enumerate(articles):

        contents.append({
            "type": "text",
            "text": f"{NUMBER[i]} {item['title']}",
            "weight": "bold",
            "wrap": True,
            "margin": "lg"
        })

        contents.append({
            "type": "text",
            "text": f"💡 {item['why']}",
            "wrap": True,
            "size": "sm",
            "margin": "sm"
        })

        if item["source"]:

            contents.append({
                "type": "text",
                "text": f"📍 {item['source']}",
                "size": "xs",
                "color": "#888888",
                "margin": "sm"
            })

        if item["link"]:

            contents.append(
                article_button(
                    "🔗 Open Article",
                    item["link"]
                )
            )

        contents.append(separator())

    return {
        "type": "flex",
        "altText": "早安 Oncology HawkEye Daily Update",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": contents
            }
        }
    }
