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

Review ALL records.

These are structured oncology intelligence records.

Tasks:

1. Read ALL records.

2. Remove duplicate events.

3. Rank by:

- Disease Area
- Clinical Impact
- APAC Relevance
- Company Relevance

4. Select ONLY Top 6.

5. Produce ONE Executive Summary.

Requirements

Executive Summary:
Maximum 50 words.

Each Top Intelligence:

Title

Why it matters (≤20 words)

Link

Structured Records

{payload}

"""

    return ask_gemini(prompt)
