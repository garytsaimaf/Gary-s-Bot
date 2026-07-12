import re


def parse_ai_output(text):

    summary = ""

    articles = []

    mode = None

    current = None

    for raw in text.splitlines():

        line = raw.strip()

        if not line:
            continue

        lower = line.lower()

        if lower.startswith("summary"):
            mode = "summary"
            continue

        if lower.startswith("top intelligence"):
            mode = "top"
            continue

        if mode == "summary":

            summary += line + " "

            continue

        if mode != "top":
            continue

        if line.startswith("Title:"):

            if current:
                articles.append(current)

            current = {
                "title": line.replace(
                    "Title:",
                    ""
                ).strip(),
                "why": "",
                "link": "",
                "source": ""
            }

            continue

        if line.startswith("Why it matters:"):

            if current:

                current["why"] = line.replace(
                    "Why it matters:",
                    ""
                ).strip()

    if current:
        articles.append(current)

    summary = re.sub(
        r"\s+",
        " ",
        summary
    ).strip()

    return summary, articles
