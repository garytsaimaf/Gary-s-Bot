import feedparser
from urllib.parse import quote


def search_google_news(keyword, max_results=5):

    query = quote(keyword)

    url = (
        "https://news.google.com/rss/search?"
        f"q={query}&hl=en-US&gl=US&ceid=US:en"
    )

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:max_results]:

        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })

    return articles
