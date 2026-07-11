from config.loader import load_topics
from output.report import build_daily_report
from line.push import push_text

from services.pubmed.search import search_pubmed
from services.pubmed.fetch import fetch_pubmed_details


def main():

    config = load_topics()

    keyword = config["test_topic"]

    results = []

    results.append("🩺 GMIA Daily Oncology Intelligence")
    results.append("")
    results.append(f"Topic: {keyword}")
    results.append("")

    pmids = search_pubmed(keyword)

    if len(pmids) == 0:

        results.append("No PubMed articles found.")

    else:

        articles = fetch_pubmed_details(pmids)

        results.append(f"Found {len(articles)} article(s)")
        results.append("")

        for index, article in enumerate(articles, start=1):

            results.append(f"{index}. {article['title']}")

            results.append(f"Journal: {article['journal']}")

            results.append(f"Published: {article['date']}")

            results.append(
                f"https://pubmed.ncbi.nlm.nih.gov/{article['pmid']}/"
            )

            results.append("")

    message = build_daily_report(results)

    print(message)

    push_text(message)


if __name__ == "__main__":
    main()
