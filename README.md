
# Basic LLM Chain with LangChain

## 📌 Project Overview

This project demonstrates the basic use of LangChain to build an LLM-powered application using a simple LLM Chain.

The objective is to understand how prompts, models, and chains work together to generate responses using a Large Language Model (LLM).

---

## 🧠 What is an LLM Chain?

An LLM Chain is a simple pipeline that:

1. Receives an input.
2. Formats it using a Prompt Template.
3. Sends it to a Large Language Model.
4. Returns the generated response.

It is the fundamental building block for more advanced AI systems.

---

## 🏗 Architecture

User Input → PromptTemplate → LLM → Output

---

## 🛠 Technologies Used

- Python 3.11
- LangChain
- Google Gemini (LLM)
- Python-dotenv

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone <repo_link>
cd LangChain-Basic-LLM-Chain
````

### 2️⃣ Create virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## 🚀 Running the Application

```bash
python main.py
```

The system will prompt for input and generate a response using the LLM.

---

## 🎯 Learning Outcomes

* Understanding Prompt Templates
* Using LangChain to call an LLM
* Managing environment variables
* Structuring a basic AI application

---

## 📌 Conclusion

This project introduces the fundamental concepts of LangChain and LLM-based applications, serving as the foundation for building more advanced systems such as Retrieval-Augmented Generation (RAG).

