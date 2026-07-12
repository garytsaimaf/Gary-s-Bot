def article_button(title, url):

    return {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
            "type": "uri",
            "label": title,
            "uri": url
        }
    }


def separator():

    return {
        "type": "separator",
        "margin": "md"
    }
