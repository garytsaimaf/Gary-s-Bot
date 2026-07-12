import os

from google import genai


client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


def ask_gemini(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    if len(text) > 350:
        text = text[:350]

    return text
