import os
from google import genai

PREFERRED_MODELS = [
    "models/gemini-3.5-flash",
    "models/gemini-3.1-flash-lite",
    "models/gemini-3.1-flash-lite-preview",
    "models/gemini-2.5-flash",
    "models/gemini-2.0-flash",
]


def ask_gemini(prompt):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing.")

    client = genai.Client(api_key=api_key)

    available = {m.name for m in client.models.list()}

    model = None
    for candidate in PREFERRED_MODELS:
        if candidate in available:
            model = candidate
            break

    if model is None:
        raise RuntimeError("No supported Gemini text model found.")

    print(f"Using Gemini model: {model}")

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return response.text.strip()
