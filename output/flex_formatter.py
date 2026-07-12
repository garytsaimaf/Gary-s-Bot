from line.flex import article_button, separator


NUMBER = [
    "①️⃣",
    "②️⃣",
    "③️⃣",
    "④️⃣",
    "⑤️⃣",
    "⑥️⃣"
]


def build_flex(summary, articles):

    contents = []

    contents.append({
        "type": "text",
        "text": "🩺 早安 This is ONCOLOGY Hawkeye Daily Update",
        "weight": "bold",
        "size": "lg"
    })

    contents.append({
        "type": "text",
        "text": "📌 Summary",
        "weight": "bold",
        "margin": "xl"
    })

    contents.append({
        "type": "text",
        "text": summary,
        "wrap": True,
        "size": "sm"
    })

    contents.append({
        "type": "text",
        "text": "📚 Top Intelligence",
        "weight": "bold",
        "margin": "xl"
    })

    for i, item in enumerate(articles):

        contents.append({

            "type": "text",

            "text": f"{NUMBER[i]} {item['title']}",

            "wrap": True,

            "weight": "bold",

            "margin": "lg"

        })

        contents.append({

            "type": "text",

            "text": item["why"],

            "wrap": True,

            "size": "sm"

        })

        contents.append({

            "type": "text",

            "text": f"Source: {item['source']}",

            "size": "xs",

            "color": "#888888"

        })

        contents.append(

            article_button(

                "🔗 Open Article",

                item["link"]

            )

        )

        contents.append(

            separator()

        )

    return {

        "type": "flex",

        "altText": "Daily Oncology Intelligence",

        "contents": {

            "type": "bubble",

            "body": {

                "type": "box",

                "layout": "vertical",

                "contents": contents

            }

        }

    }
