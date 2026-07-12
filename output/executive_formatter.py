import re


def build_executive_message(ai_output):

    text = ai_output.strip()

    text = text.replace("Summary", "📌 Summary")

    text = text.replace(
        "Top Intelligence",
        "\n📚 Top Intelligence"
    )

    numbers = [
        "①️⃣",
        "②️⃣",
        "③️⃣",
        "④️⃣",
        "⑤️⃣",
        "⑥️⃣",
    ]

    count = 0

    def replace_title(match):
        nonlocal count

        if count >= len(numbers):
            prefix = "•"
        else:
            prefix = numbers[count]

        count += 1

        return f"{prefix} {match.group(0)}"

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
        "🔗 LINK",
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
