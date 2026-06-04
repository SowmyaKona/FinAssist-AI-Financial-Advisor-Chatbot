# 💰 FinAssist AI – Financial Advisor Chatbot

## 📖 Overview

FinAssist AI is a Generative AI-powered Financial Advisor Chatbot built using Google's Gemini API and Streamlit. The chatbot helps users understand personal finance concepts such as budgeting, saving, investing, taxation, insurance, and financial planning through natural conversations.

The application follows production-grade AI engineering practices including modular architecture, secure API key management, prompt engineering, logging, exception handling, conversation memory, and token optimization.

---

# 🚀 Features

### Financial Education

* Budget planning guidance
* Savings strategies
* Investment education
* Taxation basics
* Financial planning concepts
* Insurance awareness

### AI Capabilities

* Multi-turn conversations
* Context-aware responses
* Prompt-engineered financial assistance
* Educational financial guidance
* Conversation memory

### Engineering Features

* Gemini API integration
* Secure API key management
* Modular project structure
* Logging and monitoring
* Exception handling
* Token usage optimization
* Streamlit-based interactive UI

---

# 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit User Interface
 │
 ▼
Prompt Layer
(prompts.py)
 │
 ▼
Gemini Service Layer
(gemini_service.py)
 │
 ▼
Google Gemini API
 │
 ▼
Response Processing
 │
 ▼
Financial Guidance Response
```

---

# 📂 Project Structure

```text
finassist-ai/
│
├── app.py
├── gemini_service.py
├── prompts.py
├── logger.py
├── chatbot.log
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Google GenAI SDK
* Python Dotenv
* Logging Module

---

# ⚙️ Installation

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

# 🧠 Prompt Engineering

The chatbot uses a structured system prompt with:

### Role-Based Instructions

* Acts as a Financial Advisor Chatbot
* Provides educational financial guidance
* Explains financial concepts clearly

### Domain Constraints

* No personalized financial advice
* No stock recommendations
* No guaranteed returns
* No investment decision-making

### Safety Measures

* Encourages responsible financial planning
* Recommends consulting certified financial advisors for important financial decisions

---

# 🔒 Security Features

* API keys stored using environment variables
* Sensitive credentials excluded from source code
* Modular architecture for maintainability
* Controlled system prompts

---

# 📈 Token Optimization

To reduce API costs and improve efficiency:

* Only recent conversation messages are sent to Gemini
* Conversation history is limited to maintain context
* Optimized prompt construction

---

# 📝 Logging and Monitoring

The application maintains logs for:

* API requests
* Successful responses
* Runtime errors
* Exception tracking

Log file:

```text
chatbot.log
```

---

# ⚠️ Disclaimer

FinAssist AI is designed for educational and informational purposes only.

The chatbot:

* Does not provide personalized financial advice
* Does not recommend specific stocks or investments
* Does not guarantee profits or returns
* Does not replace professional financial consultation

Always consult a qualified financial advisor before making investment or financial decisions.

---

# 🔮 Future Enhancements

* Retrieval-Augmented Generation (RAG)
* Financial knowledge base integration
* Investment calculators
* Expense tracking dashboard
* Portfolio analysis
* User authentication
* Cloud deployment
* Financial document analysis


---

