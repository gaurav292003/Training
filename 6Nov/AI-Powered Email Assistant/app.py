# email_assistant_app.py
import streamlit as st
import requests

# Define FastAPI URL (use your backend's URL here)
FASTAPI_URL = "http://localhost:8000/process_email"  # Change if hosted elsewhere

# Streamlit Interface
st.title("AI-Powered Email Assistant")

# Input area for email content
email_content = st.text_area("Paste your email content here:")

if email_content:
    # Send email content to FastAPI for processing
    response = requests.post(FASTAPI_URL, json={"email_content": email_content})

    if response.status_code == 200:
        result = response.json()
        summary = result.get("summary")
        reply = result.get("reply")

        # Display the summary and generated reply
        st.subheader("Email Summary:")
        st.write(summary)

        st.subheader("Generated Reply:")
        st.write(reply)
    else:
        st.write("Error processing the email.")
