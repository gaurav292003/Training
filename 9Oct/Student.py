from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    grade: str

@app.get("/students", response_model=List[Student])
def get_students():
    return [
        {"id": 1, "name": "Alice", "grade": "A"},
        {"id": 2, "name": "Bob", "grade": "B"},
        {"id": 3, "name": "Charlie", "grade": "A"},
        {"id": 4, "name": "David", "grade": "C"},
        {"id": 5, "name": "Eva", "grade": "B"},
    ]

@app.get("/", response_class=HTMLResponse)
def serve_html():
    with open("UI.html", "r", encoding="utf-8") as f:
        return f.read()
