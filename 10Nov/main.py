from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Create logs directory safely
os.makedirs("logs", exist_ok=True)

# ---------- LOGGING TO FILE ----------
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = FastAPI()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct:free"

class Query(BaseModel):
    text: str


@app.post("/chat")
async def chat(body: Query):

    logging.info(f"User Input: {body.text}")

    prompt = f"""
You are a simple assistant.
Perform exactly one task:
- If user says "add X and Y", return only the sum.
- If user says "today date", return only today's date in YYYY-MM-DD format.
- If user says "reverse WORD", return only the reversed word.

Return **only the answer**, nothing else. No explanations.

User: {body.text}
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": prompt}
        ],
        "temperature": 0.0
    }

    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                json=payload, headers=headers
            )

        reply = r.json()["choices"][0]["message"]["content"].strip()

        # log output
        logging.info(f"Model Output: {reply}")

        return {"reply": reply}

    except Exception as e:
        logging.error(f"Error: {e}")
        return {"reply": "Backend error occurred"}
