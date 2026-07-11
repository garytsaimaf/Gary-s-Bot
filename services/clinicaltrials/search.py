import requests


def search_trials(keyword, max_results=5):

    url = "https://clinicaltrials.gov/api/v2/studies"

    params = {
        "query.term": keyword,
        "pageSize": max_results,
    }

    response = requests.get(url, params=params, timeout=30)

    response.raise_for_status()

    data = response.json()

    studies = data.get("studies", [])

    results = []

    for study in studies:

        protocol = study.get("protocolSection", {})

        identification = protocol.get("identificationModule", {})

        status = protocol.get("statusModule", {})

        design = protocol.get("designModule", {})

        results.append(
            {
                "nct": identification.get("nctId", ""),
                "title": identification.get("briefTitle", ""),
                "status": status.get("overallStatus", ""),
                "phase": ", ".join(design.get("phases", [])),
            }
        )

    return results
