# 🏢 AI Workflow Automation Assistant

An enterprise-style AI workflow automation system built using **Python**, **Streamlit**, and **Google Gemini API**.

The application classifies employee requests and automatically generates structured workflow outputs such as:

- Department routing
- Priority classification
- Issue categorization
- Executive summaries
- Recommended next actions

This project demonstrates practical implementation of **Prompt Engineering**, **LLM orchestration**, and **enterprise AI workflow automation**.

---

# 🚀 Features

✅ AI-powered workflow classification  
✅ Enterprise request routing  
✅ Prompt-engineered structured outputs  
✅ Priority assessment system  
✅ Suggested action generation  
✅ Streamlit frontend interface  
✅ Gemini API integration  
✅ Modular Python architecture  

---

# 🧠 Example Use Cases

The assistant can process requests related to:

- IT support incidents
- HR policy questions
- Finance reimbursement issues
- Security incidents
- Operations requests
- Administrative workflows

---

# 🏗️ Project Architecture

```text
AI-Workflow-Automation/
│
├── .venv/
├── src/
│   ├── llm_helper.py
│   ├── workflow_engine.py
│
├── app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
```

---

# ⚙️ Technologies Used

- Python 3.11
- Streamlit
- Google Gemini API
- Prompt Engineering
- LLM Workflow Automation
- dotenv

---

# 🔄 Workflow Process

## 1️⃣ User Request Input

The employee enters an issue or request through the Streamlit interface.

### Example

```text
VPN access is failing and remote employees cannot connect.
```

---

## 2️⃣ Prompt-Based Classification

The LLM analyzes the request and generates structured workflow information:

- Department
- Priority
- Category
- Summary
- Suggested Action

---

## 3️⃣ Workflow Output Generation

### Example Output

```text
Department: IT Support
Priority: Critical
Category: Network Access Issue
Summary: VPN access is failing for remote employees.
Suggested Action: Escalate to Network Operations team immediately.
```

---

# 📌 Key Engineering Concepts Demonstrated

- Prompt Engineering
- Enterprise AI Automation
- LLM Orchestration
- Structured Output Generation
- AI-based Workflow Routing
- Business Process Automation
- API Integration
- Streamlit UI Development

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI-Workflow-Automation.git
```

---

## Create Virtual Environment

```bash
py -3.11 -m venv .venv
```

---

## Activate Virtual Environment

### PowerShell

```bash
.\.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧪 Sample Test Queries

## IT Support

```text
VPN access is failing and remote employees cannot connect.
```

---

## HR

```text
I need parental leave documentation and policy clarification.
```

---

## Security

```text
Suspicious login attempts detected on multiple employee accounts.
```

---

## Finance

```text
Employee reimbursement for travel expenses has not been processed.
```

---

# 📈 Future Improvements

- Multi-step workflow automation
- Email notification integration
- Database storage
- Role-based access control
- REST API integration
- Workflow history tracking
- n8n / Zapier integration
- Advanced ticket routing

---

# 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- Enterprise AI systems
- Prompt Engineering
- LLM application architecture
- AI workflow automation
- Structured AI outputs
- Business process orchestration
