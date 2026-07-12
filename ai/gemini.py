import os

from google import genai


_cached_model = None


def get_model(client):

    global _cached_model

    if _cached_model:
        return _cached_model

    print("========== AVAILABLE GEMINI MODELS ==========")

    preferred = []

    for model in client.models.list():

        name = model.name

        print(name)

        supported = getattr(model, "supported_actions", None)

        if supported is None:
            supported = getattr(model, "supported_generation_methods", [])

        if (
            "generateContent" in supported
            and "embedding" not in name.lower()
        ):
            preferred.append(name)

    print("=============================================")

    if not preferred:
        raise RuntimeError("No generateContent model available.")

    preferred.sort()

    _cached_model = preferred[0]

    print(f"Using Gemini model: {_cached_model}")

    return _cached_model


def ask_gemini(prompt):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing.")

    client = genai.Client(api_key=api_key)

    model = get_model(client)

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return response.text.strip()
