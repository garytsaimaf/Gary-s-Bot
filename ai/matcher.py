from difflib import SequenceMatcher


def normalize(text):

    return (
        text.lower()
        .replace(":", "")
        .replace(",", "")
        .replace(".", "")
        .replace("(", "")
        .replace(")", "")
        .replace("-", " ")
        .replace("/", " ")
        .strip()
    )


def similarity(a, b):

    return SequenceMatcher(
        None,
        normalize(a),
        normalize(b)
    ).ratio()


def attach_links(records, articles):

    for article in articles:

        best = None
        best_score = 0

        for record in records:

            score = similarity(
                article["title"],
                record["title"]
            )

            if score > best_score:
                best_score = score
                best = record

        if best and best_score >= 0.55:

            article["link"] = best.get(
                "link",
                ""
            )

            article["source"] = best.get(
                "source",
                ""
            )

        else:

            article["link"] = ""

            article["source"] = ""

    return articles
