import feedparser


def search_fda_news(max_results=5):

    rss_url = (
        "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/"
        "press-announcements/rss.xml"
    )

    feed = feedparser.parse(rss_url)

    results = []

    for entry in feed.entries[:max_results]:

        results.append(
            {
                "title": entry.get("title", ""),
                "published": entry.get("published", ""),
                "link": entry.get("link", ""),
            }
        )

    return results
