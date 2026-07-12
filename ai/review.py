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

Below are today's structured oncology intelligence records.

IMPORTANT

Every record already contains a source URL.

Always preserve the original URL.

Never leave the Link field empty.

If a record contains a URL, output EXACTLY the same URL.

Never replace it.

Never omit it.

Review ALL records.

Remove duplicated events.

Select ONLY the six highest-priority intelligence.

Return EXACTLY the requested format.

Structured Records

{payload}
"""

    return ask_gemini(prompt)
