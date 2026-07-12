import feedparser
from urllib.parse import quote

from config.loader import load_search_config


def search_google_news(keyword, max_results=None):

    config = load_search_config()["sources"]["google_news"]

    if max_results is None:
        max_results = config["max_results_per_keyword"]

    period_days = config["period_days"]

    query = quote(f"{keyword} when:{period_days}d")

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}"
        "&hl=en-US"
        "&gl=US"
        "&ceid=US:en"
    )

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:max_results]:

        original_link = ""

        if hasattr(entry, "links"):

            for link in entry.links:

                href = link.get("href", "")

                if (
                    href.startswith("http")
                    and "news.google.com" not in href
                ):
                    original_link = href
                    break

        if not original_link:
            original_link = entry.link

        articles.append(
            {
                "title": entry.title,
                "link": original_link,
                "published": getattr(entry, "published", ""),
            }
        )

    return articles
