# main.py (FastAPI backend)
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# FastAPI initialization
app = FastAPI()

# Define the model for incoming email data
class EmailData(BaseModel):
    email_content: str

# Memory to store previous conversation context (for a chat-like history)
memory = ConversationBufferMemory(memory_key="history", return_messages=False)

# Define the email summarization prompt
summary_prompt = "Please summarize the following email content: {email_content}"
reply_prompt = "Based on the email content, generate a professional and polite response: {email_content}"

# Set up Langchain and OpenRouter Mistral for summarization and reply generation
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",  # You can adjust this to the actual OpenRouter model name
    api_key=os.getenv("OPENROUTER_API_KEY"),  # Load API key from .env
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Email Assistant"
    }
)

# Define PromptTemplate for summarization
summary_template = PromptTemplate(
    input_variables=["email_content"],
    template=summary_prompt,
)

# Define PromptTemplate for reply generation
reply_template = PromptTemplate(
    input_variables=["email_content"],
    template=reply_prompt,
)

# Define a POST endpoint for processing the email
@app.post("/process_email")
def process_email(data: EmailData):
    logging.debug(f"Received email content: {data.email_content}")

    # Load history from memory for the context
    history = memory.load_memory_variables({}).get("history", "")
    logging.debug(f"Conversation history: {history}")

    # Prepare final prompts for summarizing and generating the reply
    summary_final_prompt = summary_template.format(email_content=data.email_content)
    reply_final_prompt = reply_template.format(email_content=data.email_content)

    # Generate summary
    logging.debug(f"Summary prompt: {summary_final_prompt}")
    summary_response = llm.invoke(summary_final_prompt)
    logging.debug(f"Summary Response: {summary_response.content}")

    # Generate reply
    logging.debug(f"Reply prompt: {reply_final_prompt}")
    reply_response = llm.invoke(reply_final_prompt)
    logging.debug(f"Reply Response: {reply_response.content}")

    # Save context to memory (email content and generated replies)
    memory.save_context({"input": data.email_content}, {"output": summary_response.content})
    memory.save_context({"input": data.email_content}, {"output": reply_response.content})

    # Return both summary and reply
    return {"summary": summary_response.content, "reply": reply_response.content}
