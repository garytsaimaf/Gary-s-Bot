import requests
import xml.etree.ElementTree as ET


def fetch_pubmed_details(pmids):

    if len(pmids) == 0:
        return []

    id_string = ",".join(pmids)

    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        f"esummary.fcgi?db=pubmed&id={id_string}&retmode=xml"
    )

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    root = ET.fromstring(response.text)

    articles = []

    for doc in root.findall(".//DocSum"):

        article = {
            "pmid": "",
            "title": "",
            "journal": "",
            "date": ""
        }

        article["pmid"] = doc.find("Id").text

        for item in doc.findall("Item"):

            name = item.attrib.get("Name")

            if name == "Title":
                article["title"] = item.text or ""

            elif name == "FullJournalName":
                article["journal"] = item.text or ""

            elif name == "PubDate":
                article["date"] = item.text or ""

        articles.append(article)

    return articles
