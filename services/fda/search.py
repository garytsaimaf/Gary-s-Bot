import feedparser
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime

from config.loader import load_search_config


def search_fda_news():

    config = load_search_config()["sources"]["fda"]

    max_results = config["max_results"]
    period_days = config["period_days"]

    cutoff = datetime.utcnow() - timedelta(days=period_days)

    rss_url = (
        "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/"
        "press-announcements/rss.xml"
    )

    feed = feedparser.parse(rss_url)

    results = []

    for entry in feed.entries:

        try:
            published = parsedate_to_datetime(
                entry.get("published", "")
            )

            if published.tzinfo is not None:
                published = published.replace(tzinfo=None)

        except Exception:
            continue

        if published < cutoff:
            continue

        results.append(
            {
                "title": entry.get("title", ""),
                "published": entry.get("published", ""),
                "link": entry.get("link", ""),
            }
        )

        if len(results) >= max_results:
            break

    return results
