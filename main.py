from config.loader import load_topics
from output.report import build_daily_report
from line.push import push_text
from services.pubmed.search import search_pubmed


def main():

    config = load_topics()

    keyword = config["test_topic"]

    results = []

    results.append("🩺 GMIA started successfully.")
    results.append("")

    results.append("Languages:")

    for language in config["languages"]:
        results.append(f"• {language}")

    results.append("")

    results.append("Topics:")

    for disease in config["diseases"]:
        results.append(f"• {disease}")

    results.append("")

    results.append(f"PubMed Search: {keyword}")

    pubmed_ids = search_pubmed(keyword)

    if len(pubmed_ids) == 0:

        results.append("No PubMed records found.")

    else:

        results.append(f"Found {len(pubmed_ids)} records.")

        for pmid in pubmed_ids:

            results.append(f"PMID: {pmid}")

    message = build_daily_report(results)

    print(message)

    push_text(message)


if __name__ == "__main__":

    main()
