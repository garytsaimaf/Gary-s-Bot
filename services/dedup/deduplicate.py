import re


def normalize(text):

    text = text.lower()

    text = re.sub(r"[^a-z0-9 ]", "", text)

    return text.strip()


def remove_duplicates(items):

    seen = set()

    results = []

    for item in items:

        title = item.get("title", "")

        key = normalize(title)

        if key in seen:
            continue

        seen.add(key)

        results.append(item)

    return results
