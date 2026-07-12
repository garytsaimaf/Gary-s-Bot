from config.loader import load_topics

from services.pubmed.search import search_pubmed
from services.pubmed.fetch import fetch_pubmed_details

from services.google.news import search_google_news
from services.clinicaltrials.search import search_trials
from services.gsk.search import search_gsk_news
from services.fda.search import search_fda_news
from services.nhi.search import search_nhi_news

from processing.normalizer import normalize

from ai.review import review

from output.executive_formatter import build_executive_message

from line.push import push_text


def main():

    config = load_topics()

    keyword = config["test_topic"]

    pmids = search_pubmed(keyword)

    if pmids:
        pubmed = fetch_pubmed_details(pmids)
    else:
        pubmed = []

    google_news = search_google_news(keyword)

    clinical_trials = search_trials(keyword)

    gsk = search_gsk_news()

    fda = search_fda_news()

    nhi = search_nhi_news()

    records = normalize(
        pubmed,
        google_news,
        clinical_trials,
        gsk,
        fda,
        nhi,
    )

    ai_output = review(records)

    message = build_executive_message(ai_output)

    print(message)

    push_text(message)


if __name__ == "__main__":
    main()
