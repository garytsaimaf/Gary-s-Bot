def build_executive_message(ai_result):

    lines = []

    lines.append("🩺 Gary Medical Intelligence Assistant")
    lines.append("")
    lines.append("Daily Oncology Intelligence")
    lines.append("")
    lines.append(ai_result.strip())

    return "\n".join(lines)
