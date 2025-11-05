import streamlit as st
import requests

st.title("Interview Question Generator")

st.write("Paste the Job Description below. The chatbot will use it as context for all conversation.")

job_description = st.text_area("Job Description", height=200)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_msg = st.chat_input("Type here... (e.g., 'Generate questions', 'Harder', 'Behavioral')")

if user_msg and job_description:
    res = requests.post(
        "http://localhost:8000/chat",
        json={"job_description": job_description, "message": user_msg}
    )
    bot_reply = res.json()["reply"]

    st.session_state.messages.append(("You", user_msg))
    st.session_state.messages.append(("AI", bot_reply))

for sender, msg in st.session_state.messages:
    st.chat_message("assistant" if sender == "AI" else "user").write(msg)
