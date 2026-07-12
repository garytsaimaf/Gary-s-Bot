from ai.prompt import SYSTEM_PROMPT
from ai.provider import summarize


def generate_summary(report_text):

    prompt = f"""
{SYSTEM_PROMPT}

========================

{report_text}
"""

    try:

        result = summarize(prompt)

        return result.strip()

    except Exception as e:

        return (
            "Executive Summary\n"
            "AI service temporarily unavailable.\n\n"
            "Top Intelligence\n"
            "No AI analysis available."
        )
