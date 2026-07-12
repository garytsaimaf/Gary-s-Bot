from line.flex import article_button, separator


NUMBER = [
    "1️⃣",
    "2️⃣",
    "3️⃣",
    "4️⃣",
    "5️⃣",
    "6️⃣"
]


def build_flex(summary, articles):

    contents = []

    contents.append({
        "type": "text",
        "text": "‼️Daily ONC Intelligence🔴 ",
        "weight": "bold",
        "size": "md"
    })

    contents.append({
        "type": "text",
        "text": "Daily Oncology Intelligence",
        "size": "xs",
        "color": "#888888",
        "margin": "sm"
    })

    contents.append(separator())

    contents.append({
        "type": "text",
        "text": "📌 Summary",
        "weight": "bold",
        "size": "sm",
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
        "size": "sm",
        "margin": "lg"
    })

    for i, item in enumerate(articles):

        contents.append({
            "type": "text",
            "text": f"{NUMBER[i]}. {item['title']}",
            "weight": "bold",
            "size": "sm",
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

        if item.get("source"):

            contents.append({
                "type": "text",
                "text": f"📍 {item['source']}",
                "size": "xs",
                "color": "#888888",
                "margin": "sm"
            })

        if item.get("link"):

            contents.append(
                article_button(
                    item["link"]
                )
            )

        contents.append(separator())

    return {
        "type": "flex",
        "altText": "早安安安！腫瘤新知推播通知來嘍❤️",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": contents
            }
        }
    }
