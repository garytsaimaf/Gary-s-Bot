import feedparser


def search_nhi_news(max_results=5):

    rss_url = "https://www.nhi.gov.tw/rss?uid=3258"

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
