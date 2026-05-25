#AI-Workflow-Automation\src\workflow_engine.py

from src.llm_helper import generate_response


def classify_ticket(user_input):

    prompt = f"""
    You are an enterprise AI workflow assistant.

    Analyze the employee request and classify it.

    Return STRICTLY in this format:

    Department: <department>
    Priority: <Low/Medium/High/Critical>
    Category: <category>
    Summary: <short summary>
    Suggested Action: <recommended next step>

    Example departments:
    - IT Support
    - HR
    - Finance
    - Operations
    - Security
    - Administration

    User Request:
    {user_input}
    """

    response = generate_response(prompt)

    return response