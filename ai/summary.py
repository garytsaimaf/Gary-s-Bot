from ai.prompt import SYSTEM_PROMPT
from ai.provider import summarize


def generate_summary(report_text):

    prompt = (
        SYSTEM_PROMPT
        + "\n\n"
        + report_text
    )

    try:

        return summarize(prompt)

    except Exception:

        return (
            "No major oncology updates requiring immediate "
            "attention were identified, or the AI summary "
            "service is temporarily unavailable."
        )
