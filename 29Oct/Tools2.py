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

def word_count(text: str) -> str:
    """Count the number of words in a sentence."""
    word_count = len(text.split())
    return f"Your sentence has {word_count} words."

def reverse_text(text: str) -> str:
    """Reverse the given sentence or word order."""
    reversed_sentence = " ".join(text.split()[::-1])
    return f"Reversed: {reversed_sentence}"

def vocabulary_helper(word: str) -> str:
    """Provide a synonym or definition for a word."""
    prompt = f"Provide a synonym or a short definition for the word '{word}'."
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def convert_case(text: str, case: str) -> str:
    """Convert text to uppercase or lowercase."""
    if case == "upper":
        return text.upper()
    elif case == "lower":
        return text.lower()
    else:
        return "Error: Invalid case command. Use 'upper' or 'lower'."

def repeat_word(word: str, times: int) -> str:
    """Repeat a word a specified number of times."""
    return " ".join([word] * times)

def get_history(memory) -> str:
    """Fetch previous conversation history."""
    messages = memory.load_memory_variables({}).get("chat_history", [])
    if not messages:
        return "No conversation history found."

    # Extract content from each message object using the `role` attribute
    history = "\n".join([f"You: {msg.content}" if msg.type == "human" else f"Agent: {msg.content}" for msg in messages])
    return f"Conversation history:\n{history}"

# ------------------------------------------------------------
# 4. Initialize memory
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Mini Language Utility Bot ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    # Handle Word Count command
    if user_input.lower().startswith("count"):
        text = " ".join(user_input.split()[1:]).strip()
        if text:
            result = word_count(text)
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": result})
        else:
            print("Agent: Please provide the sentence you want to count the words of.")
        continue

    # Handle Reverse Text command
    if user_input.lower().startswith("reverse"):
        text = " ".join(user_input.split()[1:]).strip()
        if text:
            result = reverse_text(text)
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": result})
        else:
            print("Agent: Please provide the sentence or words you want to reverse.")
        continue

    # Handle Vocabulary Helper command (define)
    if user_input.lower().startswith("define"):
        word = " ".join(user_input.split()[1:]).strip()
        if word:
            result = vocabulary_helper(word)
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": result})
        else:
            print("Agent: Please provide a word to define.")
        continue

    # Handle Uppercase/Lowercase command
    if user_input.lower().startswith("upper") or user_input.lower().startswith("lower"):
        case = "upper" if user_input.lower().startswith("upper") else "lower"
        text = " ".join(user_input.split()[1:]).strip()
        if text:
            result = convert_case(text, case)
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": result})
        else:
            print("Agent: Please provide the text you want to convert to upper or lower case.")
        continue

    # Handle Word Repeater command
    if user_input.lower().startswith("repeat"):
        parts = user_input.split()
        # Ensure the format is correct: repeat <word> <number>
        if len(parts) == 3 and parts[1].isalpha() and parts[2].isdigit():
            word = parts[1]
            times = int(parts[2])
            result = repeat_word(word, times)
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": result})
        else:
            print("Agent: Please use the format 'repeat <word> <number>'. Example: repeat hello 3")
        continue

    # Handle History command
    if user_input.lower() == "history":
        history = get_history(memory)
        print("Agent:", history)
        continue

    # Default: use LLM for other inputs (fallback)
    try:
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})
    except Exception as e:
        print("Error:", e)
