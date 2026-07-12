import requests

from config.loader import load_search_config


def search_trials(keyword):

    config = load_search_config()["sources"]["clinicaltrials"]

    max_results = config["max_results_per_disease"]

    url = "https://clinicaltrials.gov/api/v2/studies"

    params = {
        "query.term": keyword,
        "pageSize": max_results,
        "sort": "@relevance"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    studies = response.json().get("studies", [])

    results = []

    for study in studies:

        protocol = study.get("protocolSection", {})

        identification = protocol.get(
            "identificationModule",
            {}
        )

        status = protocol.get(
            "statusModule",
            {}
        )

        design = protocol.get(
            "designModule",
            {}
        )

        results.append(
            {
                "nct": identification.get("nctId", ""),
                "title": identification.get("briefTitle", ""),
                "status": status.get("overallStatus", ""),
                "phase": ", ".join(
                    design.get("phases", [])
                ),
                "last_update": status.get(
                    "lastUpdatePostDateStruct",
                    {}
                ).get("date", ""),
                "url": (
                    f"https://clinicaltrials.gov/study/"
                    f"{identification.get('nctId', '')}"
                ),
            }
        )

    return results
