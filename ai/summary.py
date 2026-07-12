from ai.prompt import SYSTEM_PROMPT
from ai.provider import summarize


def generate_summary(report_text):

    prompt = (
        SYSTEM_PROMPT
        + "\n\n"
        + report_text
    )

    return summarize(prompt)
