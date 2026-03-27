
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def summarize_incident_tool(text: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Summarize this industrial incident in one sentence: {text}"
        )
        return response.text

    except:
        # fallback summary if quota fails
        return text[:80] + "..."