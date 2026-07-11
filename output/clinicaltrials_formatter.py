def format_clinical_trials_section(trials):

    lines = []

    lines.append("--------------------------------")
    lines.append("")
    lines.append("🧪 ClinicalTrials.gov")
    lines.append("")

    if len(trials) == 0:

        lines.append("No Clinical Trial found.")
        lines.append("")

        return lines

    lines.append(f"Found {len(trials)} trial(s)")
    lines.append("")

    for index, trial in enumerate(trials, start=1):

        lines.append(f"{index}. {trial['title']}")

        if trial["phase"]:
            lines.append(f"Phase: {trial['phase']}")

        if trial["status"]:
            lines.append(f"Status: {trial['status']}")

        if trial["nct"]:
            lines.append(
                f"https://clinicaltrials.gov/study/{trial['nct']}"
            )

        lines.append("")

    return lines
