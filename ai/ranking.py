from ai.summary import generate_summary


def build_ai_brief(report):

    prompt = f"""
You are an APAC Senior Medical Advisor in solid tumors.

Review the oncology intelligence below.

Tasks:

1. Write ONE Executive Summary in <=50 words.

2. Select ONLY the 8 most important updates.

Priority order:
- Disease Area
- Clinical impact
- APAC relevance
- Company relevance

For each selected update use EXACTLY this format:

Title:
Why it matters:
Link:

Keep "Why it matters" under 20 words.

====================

{report}
"""

    return generate_summary(prompt)
