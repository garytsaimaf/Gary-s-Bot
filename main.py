from config.loader import load_topics
from output.report import build_daily_report

from output.formatter import (
    format_pubmed_section,
    format_google_news_section,
)

from output.clinicaltrials_formatter import (
    format_clinical_trials_section,
)

from output.gsk_formatter import (
    format_gsk_section,
)

from output.fda_formatter import (
    format_fda_section,
)

from output.nhi_formatter import (
    format_nhi_section,
)

from line.push import push_text

from services.pubmed.search import search_pubmed
from services.pubmed.fetch import fetch_pubmed_details

from services.google.news import search_google_news

from services.clinicaltrials.search import search_trials

from services.gsk.search import search_gsk_news

from services.fda.search import search_fda_news

from services.nhi.search import search_nhi_news


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

    # -----------------------
    # ClinicalTrials.gov
    # -----------------------

    trials = search_trials(keyword)

    results.extend(format_clinical_trials_section(trials))

    # -----------------------
    # GSK Press Releases
    # -----------------------

    gsk_news = search_gsk_news()

    results.extend(format_gsk_section(gsk_news))

    # -----------------------
    # FDA Updates
    # -----------------------

    fda_news = search_fda_news()

    results.extend(format_fda_section(fda_news))

    # -----------------------
    # NHI Announcements
    # -----------------------

    nhi_news = search_nhi_news()

    results.extend(format_nhi_section(nhi_news))

    message = build_daily_report(results)

    print(message)

    push_text(message)


if __name__ == "__main__":
    main()
