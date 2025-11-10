import streamlit as st
import requests

st.title("Mini AI Tool")

user_input = st.text_input("Enter query (ex: Add 45 and 35)")

if st.button("Submit"):
    if user_input.strip():
        r = requests.post("http://localhost:8000/chat", json={"text": user_input})

        try:
            result = r.json().get("reply", "No reply returned")
            st.success(result)
        except:
            st.error("Invalid response from backend")
