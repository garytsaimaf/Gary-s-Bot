from typing import List, Dict


def normalize(
    pubmed,
    google_news,
    clinical_trials,
    gsk,
    fda,
    nhi,
) -> List[Dict]:

    data = []

    for item in pubmed:
        data.append(
            {
                "source": "PubMed",
                "type": "Journal",
                "title": item.get("title", ""),
                "journal": item.get("journal", ""),
                "date": item.get("pubdate", ""),
                "link": item.get("url", ""),
            }
        )

    for item in google_news:
        data.append(
            {
                "source": "Google News",
                "type": "News",
                "title": item.get("title", ""),
                "journal": "",
                "date": item.get("published", ""),
                "link": item.get("link", ""),
            }
        )

    for item in clinical_trials:
        data.append(
            {
                "source": "ClinicalTrials.gov",
                "type": "Clinical Trial",
                "title": item.get("title", ""),
                "journal": "",
                "date": "",
                "link": item.get("url", ""),
                "phase": item.get("phase", ""),
                "status": item.get("status", ""),
            }
        )

    for item in gsk:
        data.append(
            {
                "source": "GSK",
                "type": "Press Release",
                "title": item.get("title", ""),
                "journal": "",
                "date": item.get("published", ""),
                "link": item.get("link", ""),
            }
        )

    for item in fda:
        data.append(
            {
                "source": "FDA",
                "type": "FDA Update",
                "title": item.get("title", ""),
                "journal": "",
                "date": item.get("published", ""),
                "link": item.get("link", ""),
            }
        )

    for item in nhi:
        data.append(
            {
                "source": "Taiwan NHI",
                "type": "NHI Announcement",
                "title": item.get("title", ""),
                "journal": "",
                "date": item.get("published", ""),
                "link": item.get("link", ""),
            }
        )

    return data
