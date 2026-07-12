from config.loader import load_topics

from services.pubmed.search import search_pubmed
from services.pubmed.fetch import fetch_pubmed_details

from services.google.news import search_google_news
from services.clinicaltrials.search import search_trials
from services.gsk.search import search_gsk_news
from services.fda.search import search_fda_news
from services.nhi.search import search_nhi_news

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

from output.report import build_daily_report
from output.executive_formatter import build_executive_message

from ai.ranking import build_ai_brief

from line.push import push_text


def main():

    config = load_topics()

    keyword = config["test_topic"]

    results = []

    results.append("Topic: " + keyword)
    results.append("")

    pmids = search_pubmed(keyword)

    if pmids:
        articles = fetch_pubmed_details(pmids)
    else:
        articles = []

    results.extend(format_pubmed_section(articles))

    news = search_google_news(keyword)
    results.extend(format_google_news_section(news))

    trials = search_trials(keyword)
    results.extend(format_clinical_trials_section(trials))

    gsk = search_gsk_news()
    results.extend(format_gsk_section(gsk))

    fda = search_fda_news()
    results.extend(format_fda_section(fda))

    nhi = search_nhi_news()
    results.extend(format_nhi_section(nhi))

    report = build_daily_report(results)

    ai_result = build_ai_brief(report)

    message = build_executive_message(ai_result)

    print(message)

    push_text(message)


if __name__ == "__main__":
    main()
