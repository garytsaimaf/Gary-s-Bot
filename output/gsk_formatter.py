def format_gsk_section(news):

    lines = []

    lines.append("--------------------------------")
    lines.append("")
    lines.append("🏢 GSK Press Releases")
    lines.append("")

    if len(news) == 0:

        lines.append("No GSK press releases found.")
        lines.append("")

        return lines

    lines.append(f"Found {len(news)} press release(s)")
    lines.append("")

    for index, item in enumerate(news, start=1):

        lines.append(f"{index}. {item['title']}")

        if item.get("published"):
            lines.append(f"Published: {item['published']}")

        if item.get("link"):
            lines.append(item["link"])

        lines.append("")

    return lines
