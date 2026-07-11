def build_daily_report(results):

    report = []

    report.append("🩺 Gary Medical Intelligence Assistant")
    report.append("")
    report.append("Daily Oncology Intelligence")
    report.append("")

    for item in results:
        report.append(item)

    return "\n".join(report)
