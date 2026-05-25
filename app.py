#AI-Workflow-Automation\app.py

import streamlit as st

from src.workflow_engine import classify_ticket


st.set_page_config(page_title="AI Workflow Automation")

st.title("🏢 AI Workflow Automation Assistant")

st.write(
    "AI-powered enterprise workflow classification system."
)

user_input = st.text_area(
    "Enter employee issue/request:"
)

if st.button("Process Request"):

    if user_input.strip() == "":

        st.warning("Please enter a request.")

    else:

        result = classify_ticket(user_input)

        st.subheader("Workflow Classification")

        st.code(result)