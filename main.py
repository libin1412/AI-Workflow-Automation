#AI-Workflow-Automation\main.py

from src.workflow_engine import classify_ticket


if __name__ == "__main__":

    user_request = """
    SAP login is not working and finance team
    cannot access invoices.
    """

    result = classify_ticket(user_request)

    print("\nWORKFLOW RESULT:\n")

    print(result)