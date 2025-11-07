from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# ✅ CORS so frontend (index.html) can call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow all for development
    allow_credentials=True,
    allow_methods=["*"],      # Accept POST, OPTIONS, etc.
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
HISTORY_FILE = "qa-history.json"

class Prompt(BaseModel):
    query: str


def save_history(question, answer):
    entry = {"question": question, "answer": answer}

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


@app.post("/generate")
async def generate_response(prompt: Prompt):

    # ✅ 2. Validate empty query
    if not prompt.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt.query}
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(OPENROUTER_URL, json=payload, headers=headers)
        data = response.json()

        answer = data["choices"][0]["message"]["content"]

        # ✅ 3. Save to qa-history.json
        save_history(prompt.query, answer)

        return {"response": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
