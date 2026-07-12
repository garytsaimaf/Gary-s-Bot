import time

from ai.gemini import ask_gemini


def summarize(prompt):

    last_error = None

    for _ in range(3):

        try:

            result = ask_gemini(prompt)

            result = result.replace("**", "")
            result = result.replace("```", "")
            result = result.replace("#", "")

            return result.strip()

        except Exception as e:

            last_error = e

            time.sleep(2)

    raise last_error
