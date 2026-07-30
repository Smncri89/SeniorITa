from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents="Rispondi solo OK"
    )

    print(response.text)

except Exception as e:
    print("ERRORE GEMINI:")
    print(e)