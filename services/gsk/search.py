import feedparser


def search_gsk_news(max_results=5):

    rss_url = "https://www.gsk.com/en-gb/media/press-releases/rss/"

    feed = feedparser.parse(rss_url)

    results = []

    for entry in feed.entries[:max_results]:

        results.append(
            {
                "title": entry.title,
                "published": entry.published,
                "link": entry.link,
            }
        )

    return results
