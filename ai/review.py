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

Below is structured oncology intelligence collected today.

Read ALL records before making any judgement.

Tasks

1. Remove duplicated events.

2. Prioritize by:

- Disease Area
- Clinical Impact
- APAC Relevance
- Company Relevance

3. Select ONLY the six most important updates.

4. Produce ONE Executive Summary.

Return ONLY the requested format.

Structured Records

{payload}
"""

    return ask_gemini(prompt)
