#  LangChain-Groq Chatbot with Streamlit (Basic GenAI Chatbot)


[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-mayank.streamlit.app/)


This is a **basic Generative AI chatbot** built using **LangChain**, **Groq API (Gemma 2B/9B)**, and **Streamlit**. It answers user queries using an LLM in real-time, without chat history or RAG.

---

## 🔧 Features

-  Uses **Gemma 2B/9B via Groq** for fast and intelligent responses.
-  Built with **LangChain** for prompt structuring.
-  Simple **Streamlit UI** for user input/output.
-  Adjustable **temperature** and **max_tokens**.
-  **No RAG** (Retrieval-Augmented Generation).
-  **No Chat History/Memory** — stateless Q&A model.

---

##  How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/MayankSethi27/Chatbot-Q-A.git
   cd Chatbot-Q-A
   ```
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ``` 
4. Create the .streamlit/secrets.toml file:
   ```bash
   LANGCHAIN_API_KEY = "your_langchain_api_key"
   LANGCHAIN_PROJECT = "your_langsmith_project"
   GROQ_API_KEY = "your_groq_api_key"
   ```
5. Launch the chatbot:
   ```bash
   streamlit run "Chatbot-Q&A.py"
   ```
---

## Project Structure
   ```bash
   Chatbot-Q-A/
├── Chatbot-Q&A.py
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── secrets.toml  # not committed
   ```
---
## Notes
- This is a stateless chatbot — it does not remember previous user inputs.

- Ideal for beginners to understand the basics of building GenAI apps.

- Easily deployable on Streamlit Cloud


 
