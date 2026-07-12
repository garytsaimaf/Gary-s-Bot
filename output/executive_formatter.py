import re


NUMBER_ICONS = [
    "①️⃣",
    "②️⃣",
    "③️⃣",
    "④️⃣",
    "⑤️⃣",
    "⑥️⃣",
]


def build_executive_message(ai_output):

    text = ai_output.strip()

    text = text.replace(
        "Summary",
        "📌 Summary"
    )

    text = text.replace(
        "Top Intelligence",
        "\n📚 Top Intelligence"
    )

    counter = 0

    def replace_title(match):

        nonlocal counter

        icon = (
            NUMBER_ICONS[counter]
            if counter < len(NUMBER_ICONS)
            else "•"
        )

        counter += 1

        return f"{icon} Title:"

    text = re.sub(
        r"Title:",
        replace_title,
        text,
    )

    text = text.replace(
        "Why it matters:",
        "💡 Why it matters:"
    )

    text = re.sub(
        r"Link:\s*(https?://\S+)",
        r"🔗 LINK (\1)",
        text,
    )

    text = re.sub(
        r"Link:\s*$",
        "🔗 LINK",
        text,
        flags=re.MULTILINE,
    )

    return (
        "🩺 Gary Medical Intelligence Assistant\n\n"
        "Daily Oncology Intelligence\n\n"
        f"{text}"
    )
