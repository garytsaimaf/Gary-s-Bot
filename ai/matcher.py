from difflib import SequenceMatcher


def attach_links(records, articles):

    for article in articles:

        best = None

        best_score = 0

        for record in records:

            score = SequenceMatcher(
                None,
                article["title"].lower(),
                record["title"].lower()
            ).ratio()

            if score > best_score:

                best_score = score
                best = record

        if best:

            article["link"] = best.get(
                "link",
                ""
            )

            article["source"] = best.get(
                "source",
                ""
            )

    return articles
