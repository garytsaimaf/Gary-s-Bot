import re


def parse_ai_output(text):

    summary = ""

    articles = []

    lines = text.splitlines()

    mode = None

    current = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Summary"):
            mode = "summary"
            continue

        if line.startswith("Top Intelligence"):
            mode = "top"
            continue

        if mode == "summary":
            summary += line + " "

        elif mode == "top":

            if line.startswith("Title:"):

                if current:
                    articles.append(current)

                current = {
                    "title": line.replace("Title:", "").strip(),
                    "why": "",
                    "link": ""
                }

            elif line.startswith("Why it matters:"):

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
