from config.loader import load_topics
from output.report import build_daily_report
from output.formatter import (
    format_pubmed_section,
    format_google_news_section,
)

from line.push import push_text

from services.pubmed.search import search_pubmed
from services.pubmed.fetch import fetch_pubmed_details
from services.google.news import search_google_news


def main():

    config = load_topics()

    keyword = config["test_topic"]

    results = []

    results.append("🩺 GMIA Daily Oncology Intelligence")
    results.append("")
    results.append(f"Topic: {keyword}")
    results.append("")

    # -----------------------
    # PubMed
    # -----------------------

    pmids = search_pubmed(keyword)

    if len(pmids) == 0:

        articles = []

    else:

        articles = fetch_pubmed_details(pmids)

    results.extend(format_pubmed_section(articles))

    # -----------------------
    # Google News
    # -----------------------

    news = search_google_news(keyword)

    results.extend(format_google_news_section(news))

    message = build_daily_report(results)

    print(message)

    push_text(message)


if __name__ == "__main__":
    main()
