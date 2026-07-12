import json

from ai.gemini import ask_gemini
from ai.prompt import SYSTEM_PROMPT


def review(records):

    payload = json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
    )

    prompt = f"""
{SYSTEM_PROMPT}

Below are today's oncology intelligence records.

Review ALL records before making any decision.

You are expected to think like an experienced GSK APAC Medical Advisor.

Do not simply summarize.

Identify scientific insights that may influence:

- Scientific engagement
- Evidence communication
- Competitive intelligence
- Medical strategy
- Future congress discussions
- Biomarker strategy
- Unmet medical needs

Structured Records

{payload}
"""

    return ask_gemini(prompt)
