def build_executive_message(ai_output):

    return (
        "🩺 Gary Medical Intelligence Assistant\n\n"
        "Daily Oncology Intelligence\n\n"
        + ai_output.strip()
    )
