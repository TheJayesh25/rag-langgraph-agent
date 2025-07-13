# 🧠 LangGraph RAG Agent: Stock Market PDF Query Assistant
A terminal-based LangGraph-powered Retrieval-Augmented Generation (RAG) Agent built to analyze and answer questions based on the Stock Market Performance 2024 PDF. This agent integrates PDF ingestion, vector embedding with OpenAI, ChromaDB for document retrieval, and LangGraph for tool-based LLM orchestration — all in a modular, secure, and real-world ready format.

---
## 🚀 Features
- 🔍 **PDF-Powered RAG Pipeline:** Load and parse PDFs using PyPDFLoader, split them into chunks, and embed them using OpenAIEmbeddings for accurate semantic search.
- 🧱 **ChromaDB Vector Store:** Store embeddings locally using langchain-chroma, enabling persistent document retrieval without reprocessing the PDF every time.
- 🧰 **Tool-Driven Retrieval:** A custom retriever_tool is created and registered as a LangGraph-compatible tool, enabling the agent to autonomously fetch relevant chunks during reasoning.
- 🧠 **LangGraph Agent Workflow:** Built as a conditional LangGraph state machine with two primary nodes:
  - llm: Calls the LLM to reason and potentially trigger a tool.
  - retriever_agent: Executes the tool, fetches matching content, and routes it back.
- 💬 **Conversational Interface:** Interact with the agent via a terminal chat loop with multi-step reasoning and tool calling.
- 🔐 **Security & Modularity:**
   - .env for secrets (OpenAI API Key).
   - Clean separation of graph logic, tools, and system prompting.
   - Checks for file existence, error handling in Chroma setup, and robust tool routing.

---
## 📂 Project Structure

```bash

rag_agent/
│
├── RAG_Agent.py                  # Main LangGraph RAG pipeline and agent setup
├── Stock_Market_Performance_2024.pdf   # Sample PDF document
├── .env                          # Your OpenAI API Key (not tracked in version control)
└── RAG Agent/                    # Chroma persistence directory

```
---
## 📦 Requirements
Install dependencies using:

```bash
pip install -r requirements.txt
```

requirements.txt
```txt
python-dotenv
langchain
langchain-openai
langchain-community
langchain-chroma
openai
tqdm
```

---
Ensure you create a .env file with your OpenAI key:
```
OPENAI_API_KEY=your-key-here
```

## ▶️ Running the Agent
```bash
python RAG_Agent.py
```

Then start chatting:

```
What is your question: How did the Indian market perform in Q1 2024?

The agent will:

Use the system prompt to set context.
Query the ChromaDB for relevant chunks.
Return contextual answers based on the embedded PDF.
```

---
## 🔄 How It Works (LangGraph Flow)
```
    A[User Input] --> B[LLM Node]
    B -->|Tool Call?| C{Should Continue}
    C -->|Yes| D[Retriever Tool]
    D --> B
    C -->|No| E[End]

```
## 💡 Use Cases
1. Analyze earnings reports, research papers, or legal documents via chat.
2. Extendable to multiple tools like charts, summarization, follow-up analysis.
3. Deployable as an API or integrated into a UI (e.g., Streamlit, React).

---
## 📌 Notes
- This is a local prototype — no document is sent to the cloud.
- Privacy and data persistence are respected using local storage and .env secrets.
- File path and chunking configs are easily adjustable.

---
### 🧑‍💻 Author
Jayesh Suryawanshi
- 🧠 Python Developer | 💡 AI Tools Builder | 🌍 Data & Engineering Enthusiast
- 📫 [LinkedIn](https://www.linkedin.com/in/jayesh-suryawanshi-858bb21aa/)
---
### 📃 License
MIT License
