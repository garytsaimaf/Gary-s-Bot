def format_fda_section(news):

    lines = []

    lines.append("--------------------------------")
    lines.append("")
    lines.append("🏛️ FDA Updates")
    lines.append("")

    if len(news) == 0:

        lines.append("No FDA updates found.")
        lines.append("")

        return lines

    lines.append(f"Found {len(news)} update(s)")
    lines.append("")

    for index, item in enumerate(news[:3], start=1):

        lines.append(f"{index}. {item['title']}")

        if item.get("published"):
            lines.append(f"Published: {item['published']}")

        if item.get("link"):
            lines.append(item["link"])

        lines.append("")

    return lines
