import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# ------------------------------------------------------------
# 2. Initialize the Mistral model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    temperature=0.4,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)


# ------------------------------------------------------------
# 3. Define helper tools
# ------------------------------------------------------------

def summarize(text: str) -> str:
    """Summarize a long passage or conversation history."""
    prompt = f"Please summarize the following text into a concise form:\n\n{text}\n\nSummary:"
    try:
        response = llm.invoke(prompt)
        return response.content.strip()  # Ensure the output is stripped of any extra spaces
    except Exception as e:
        return f"Error: {str(e)}"


def improve(text: str) -> str:
    """Improves the text to make it clearer and more professional."""
    prompt = f"Improve the following text for clarity and professionalism: {text}"
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def sentiment_analysis(text: str) -> str:
    """Analyze the sentiment of the text."""
    prompt = f"Classify the sentiment of the following text as Positive, Negative, or Neutral:\n\n{text}\n\nPlease output only the sentiment classification."
    try:
        response = llm.invoke(prompt)
        sentiment = response.content.strip().lower()

        if sentiment not in ["positive", "negative", "neutral"]:
            sentiment = "Unable to classify sentiment correctly."
        return f"The sentiment is {sentiment.capitalize()}."
    except Exception as e:
        return f"Error: {str(e)}"


def task_priority(text: str) -> str:
    """Classifies the task priority based on urgency."""
    prompt = f"Classify the task in terms of priority (high, medium, low): {text}"
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def note_keeper(action: str, note: str = None) -> str:
    """Store and retrieve personal notes."""
    if action == "note" and note:
        return f"Noted: {note}"
    elif action == "get":
        # Simulate retrieving stored notes (in this case, just a single example)
        return "You currently have 1 note: 'Remember to email the project report tomorrow.'"
    else:
        return "Invalid action or missing note."


# ------------------------------------------------------------
# 4. Initialize memory
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    # Handle Summarization command
    if user_input.lower().startswith("summarize"):
        text = " ".join(user_input.split()[1:]).strip()
        if text:
            summary = summarize(text)
            print("Agent:", summary)
            memory.save_context({"input": user_input}, {"output": summary})
        else:
            print("Agent: Please provide the text you want to summarize.")
        continue

    # Handle Sentiment Analysis command
    if user_input.lower().startswith("analyze"):
        text = " ".join(user_input.split()[1:]).strip()
        if text:
            sentiment = sentiment_analysis(text)
            print("Agent:", sentiment)
            memory.save_context({"input": user_input}, {"output": sentiment})
        else:
            print("Agent: Please provide the text you want to analyze.")
        continue

    # Handle Task Priority command
    if user_input.lower().startswith("priority"):
        task = " ".join(user_input.split()[1:]).strip()
        priority = task_priority(task)
        print("Agent:", priority)
        memory.save_context({"input": user_input}, {"output": priority})
        continue

    # Handle Note Command
    if user_input.lower().startswith("note"):
        note = " ".join(user_input.split()[1:]).strip()
        if note:
            note_response = note_keeper("note", note)
            print("Agent:", note_response)
            memory.save_context({"input": user_input}, {"output": note_response})
        else:
            print("Agent: Please specify the note you want to save.")
        continue

    # Handle Get Notes Command
    if "get notes" in user_input.lower():
        notes = note_keeper("get")
        print("Agent:", notes)
        memory.save_context({"input": user_input}, {"output": notes})
        continue

    # Handle Improve command
    if user_input.lower().startswith("improve"):
        text_to_improve = " ".join(user_input.split()[1:]).strip()
        if text_to_improve:
            improved_text = improve(text_to_improve)
            print("Agent:", improved_text)
            memory.save_context({"input": user_input}, {"output": improved_text})
        else:
            print("Agent: Please provide the text you want to improve.")
        continue

    # Default: use LLM for other inputs
    try:
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})
    except Exception as e:
        print("Error:", e)
