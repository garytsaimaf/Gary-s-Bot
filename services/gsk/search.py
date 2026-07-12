import feedparser
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime

from config.loader import load_search_config


def search_gsk_news():

    config = load_search_config()["sources"]["gsk"]

    max_results = config["max_results"]
    period_days = config["period_days"]

    cutoff = datetime.utcnow() - timedelta(days=period_days)

    rss_url = "https://www.gsk.com/en-gb/media/press-releases/rss/"

    feed = feedparser.parse(rss_url)

    results = []

    for entry in feed.entries:

        try:
            published = parsedate_to_datetime(entry.published)

            if published.tzinfo is not None:
                published = published.replace(tzinfo=None)

        except Exception:
            continue

        if published < cutoff:
            continue

        results.append(
            {
                "title": entry.title,
                "published": entry.published,
                "link": entry.link,
            }
        )

        if len(results) >= max_results:
            break

    return results
