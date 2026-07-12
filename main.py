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
from ai.parser import parse_ai_output
from ai.matcher import attach_links

from output.flex_formatter import build_flex

from line.push import push_text


def unique_by_title(items):

    seen = set()
    results = []

    for item in items:

        title = item.get("title", "").strip().lower()

        if not title:
            continue

        if title in seen:
            continue

        seen.add(title)
        results.append(item)

    return results


def main():

    config = load_topics()

    pubmed_records = []
    google_records = []
    trial_records = []

    for disease in config["disease_priority"]:

        english_keywords = disease.get("english", [])
        mandarin_keywords = disease.get("mandarin", [])

        # ---------- PubMed ----------
        if english_keywords:

            keyword = english_keywords[0]

            pmids = search_pubmed(keyword)

            if pmids:
                pubmed_records.extend(
                    fetch_pubmed_details(pmids)
                )

        # ---------- Google News ----------
        google_keywords = []

        google_keywords.extend(english_keywords)
        google_keywords.extend(mandarin_keywords)

        for keyword in google_keywords:

            google_records.extend(
                search_google_news(keyword)
            )

        # ---------- ClinicalTrials ----------
        if english_keywords:

            keyword = english_keywords[0]

            trial_records.extend(
                search_trials(keyword)
            )

    pubmed_records = unique_by_title(pubmed_records)
    google_records = unique_by_title(google_records)
    trial_records = unique_by_title(trial_records)

    gsk_records = search_gsk_news()
    fda_records = search_fda_news()
    nhi_records = search_nhi_news()

    records = normalize(
        pubmed_records,
        google_records,
        trial_records,
        gsk_records,
        fda_records,
        nhi_records,
    )

    ai_output = review(records)

    summary, articles = parse_ai_output(ai_output)

    articles = attach_links(
        records,
        articles,
    )

    flex = build_flex(
        summary,
        articles,
    )

    push_text(flex)


if __name__ == "__main__":
    main()
