from fastapi import FastAPI
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from backend.prompt import CHATBOT_PROMPT

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class ChatInput(BaseModel):
    job_description: str
    message: str

memory = ConversationBufferMemory(memory_key="history", return_messages=False)

prompt = PromptTemplate(
    input_variables=["job_description", "history", "user_input"],
    template=CHATBOT_PROMPT,
)

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Interview Coach Chatbot"
    }
)

@app.post("/chat")
def chat(data: ChatInput):
    history = memory.load_memory_variables({}).get("history", "")
    final_prompt = prompt.format(
        job_description=data.job_description,
        history=history,
        user_input=data.message
    )
    response = llm.invoke(final_prompt)
    memory.save_context({"input": data.message}, {"output": response.content})
    return {"reply": response.content}
