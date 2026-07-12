def article_button(url):

    return {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
            "type": "uri",
            "label": "🔗 Open Article",
            "uri": url
        }
    }


def separator():

    return {
        "type": "separator",
        "margin": "md"
    }
