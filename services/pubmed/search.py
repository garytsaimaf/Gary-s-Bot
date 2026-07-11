import requests
import xml.etree.ElementTree as ET


def search_pubmed(keyword, max_results=5):

    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        f"esearch.fcgi?db=pubmed&term={keyword}"
        f"&sort=date&retmax={max_results}"
    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    root = ET.fromstring(response.text)

    ids = []

    for item in root.findall("IdList/Id"):
        ids.append(item.text)

    return ids
