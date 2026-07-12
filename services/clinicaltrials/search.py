import requests
from datetime import datetime, timedelta

from config.loader import load_search_config


def search_trials(keyword):

    config = load_search_config()["sources"]["clinicaltrials"]

    max_results = config["max_results_per_disease"]
    period_days = config["period_days"]

    start_date = (
        datetime.utcnow() - timedelta(days=period_days)
    ).strftime("%Y-%m-%d")

    url = "https://clinicaltrials.gov/api/v2/studies"

    params = {
        "query.term": keyword,
        "pageSize": max_results,
        "query.lastUpdatePostDate": f"AREA[LastUpdatePostDate]RANGE[{start_date},MAX]"
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
