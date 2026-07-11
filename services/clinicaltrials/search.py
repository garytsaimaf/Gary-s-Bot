import requests


def search_trials(keyword, max_results=5):

    url = (
        "https://clinicaltrials.gov/api/query/study_fields"
        "?expr="
        + keyword
        + "&fields=NCTId,BriefTitle,OverallStatus,Phase"
        + "&min_rnk=1"
        + f"&max_rnk={max_results}"
        + "&fmt=json"
    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    data = response.json()

    studies = data["StudyFieldsResponse"]["StudyFields"]

    results = []

    for study in studies:

        results.append(
            {
                "nct": study["NCTId"][0] if study["NCTId"] else "",
                "title": study["BriefTitle"][0] if study["BriefTitle"] else "",
                "status": study["OverallStatus"][0] if study["OverallStatus"] else "",
                "phase": study["Phase"][0] if study["Phase"] else "",
            }
        )

    return results
