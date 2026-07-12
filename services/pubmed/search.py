import requests
import xml.etree.ElementTree as ET

from config.loader import load_search_config


def search_pubmed(keyword):

    config = load_search_config()["sources"]["pubmed"]

    max_results = config["max_results_per_disease"]
    period_days = config["period_days"]

    search_term = (
        f'("{keyword}"[Title/Abstract])'
        f' AND ("last {period_days} days"[PDat])'
    )

    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        f"?db=pubmed"
        f"&term={requests.utils.quote(search_term)}"
        f"&sort=pub+date"
        f"&retmax={max_results}"
    )

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    root = ET.fromstring(response.text)

    ids = []

    for item in root.findall("IdList/Id"):

        if item.text:

            ids.append(item.text)

    return ids
