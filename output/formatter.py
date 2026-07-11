def format_pubmed_section(articles):

    lines = []

    lines.append("📚 PubMed")
    lines.append("")

    if len(articles) == 0:

        lines.append("No PubMed articles found.")
        lines.append("")

        return lines

    lines.append(f"Found {len(articles)} article(s)")
    lines.append("")

    for index, article in enumerate(articles, start=1):

        lines.append(f"{index}. {article['title']}")

        lines.append(f"Journal: {article['journal']}")

        lines.append(f"Published: {article['date']}")

        lines.append(
            f"https://pubmed.ncbi.nlm.nih.gov/{article['pmid']}/"
        )

        lines.append("")

    return lines


def format_google_news_section(news):

    lines = []

    lines.append("--------------------------------")
    lines.append("")
    lines.append("📰 Google News")
    lines.append("")

    if len(news) == 0:

        lines.append("No Google News found.")
        lines.append("")

        return lines

    lines.append(f"Found {len(news)} news article(s)")
    lines.append("")

    for index, item in enumerate(news, start=1):

        lines.append(f"{index}. {item['title']}")

        lines.append(f"Published: {item['published']}")

        lines.append(item["link"])

        lines.append("")

    return lines
