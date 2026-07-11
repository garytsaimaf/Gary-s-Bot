import requests


def search_trials(keyword, max_results=5):

    url = "https://clinicaltrials.gov/api/query/studies"

    params = {
        "expr": keyword,
        "fields": "NCTId,BriefTitle,OverallStatus,Phase",
        "min_rnk": 1,
        "max_rnk": max_results,
        "fmt": "json",
    }

    response = requests.get(url, params=params, timeout=30)

    response.raise_for_status()

    data = response.json()

    studies = data.get("StudyFieldsResponse", {}).get("StudyFields", [])

    results = []

    for study in studies:

        results.append(
            {
                "nct": study.get("NCTId", [""])[0],
                "title": study.get("BriefTitle", [""])[0],
                "status": study.get("OverallStatus", [""])[0],
                "phase": study.get("Phase", [""])[0],
            }
        )

    return results
