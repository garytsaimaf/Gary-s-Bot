import os

from google import genai


def ask_gemini(prompt):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing.")

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash-lite"
    )

    client = genai.Client(
        api_key=api_key
    )

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return response.text.strip()
