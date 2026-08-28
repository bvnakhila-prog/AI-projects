# Local RAG Pipeline with LangChain (LCEL), ChromaDB & Llama 3

A 100% local, privacy-focused Retrieval-Augmented Generation (RAG) system built with Python, LangChain Expression Language (LCEL), ChromaDB, and Ollama. 

This pipeline allows you to query sensitive internal documents (e.g., company policies) without sending any data to external third-party cloud APIs.

---

## 🌟 Key Features

* **100% Local Processing:** Runs entirely on your local machine using Ollama—zero data leaks or cloud API costs.
* **Modern LCEL Architecture:** Built using LangChain Expression Language (`|` pipe syntax) for clean, maintainable, and deterministic chain execution.
* **Dedicated Vector Embeddings:** Uses `mxbai-embed-large` for high-precision semantic search and indexing inside ChromaDB.
* **Zero Hallucination Grounding:** Custom system prompts restrict Llama 3 to respond strictly using retrieved document context.
* **Automatic Cache Management:** Cleans and resets stale vector stores on execution to prevent outdated context retrievals.

---

## 📐 System Architecture

```text
[ Document (.txt) ]
        │
        ▼
[ Recursive Text Splitter ] ── (Chunk Size: 500, Overlap: 50)
        │
        ▼
[ Ollama Embedding Model ] ── (mxbai-embed-large)
        │
        ▼
[ ChromaDB Vector Store ] ── (Top-k Similarity Search)
        │
        ▼
[ LCEL Pipeline ] ─────────── (Retriever + Prompt + Llama 3 LLM)
        │
        ▼
[ Grounded Answer Output ]


Tech Stack
Language: Python 3.10+

Orchestration: LangChain (v0.3+), langchain-core, langchain-ollama

Vector Database: ChromaDB

Embeddings Model: mxbai-embed-large (via Ollama)

Inference Model: llama3 (via Ollama)


Tech Stack
Language: Python 3.10+

Orchestration: LangChain (v0.3+), langchain-core, langchain-ollama

Vector Database: ChromaDB

Embeddings Model: mxbai-embed-large (via Ollama)

Inference Model: llama3 (via Ollama)


Getting Started
Prerequisites
Python 3.10 or higher installed.

Ollama installed and running. Download from ollama.com.

Pull the required models via your terminal:
ollama pull llama3
ollama pull mxbai-embed-large


Installation & Setup
Clone the Repository:

Bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
Set Up a Virtual Environment:

Windows:

PowerShell
python -m venv august_venv
.\august_venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
💻 Usage
Place your target knowledge base text file named company_policy.txt in the root directory.

Ensure Ollama is running.

Run the pipeline:

Bash
python app.py
📝 License
This project is open-source and available under the MIT License.


---

### Step 2: Push to GitHub Using VS Code GUI

Once all files are created and saved, you can push them to GitHub directly inside VS Code without memorizing Git commands:

1. **Log in to GitHub on VS Code (if not already logged in):**
   * Click on the **Accounts icon** (bottom-left corner of VS Code) and sign in with your GitHub account.
2. **Open the Source Control Tab:**
   * Click on the **Source Control** icon on the left sidebar of VS Code (or press `Ctrl + Shift + G`).
3. **Publish to GitHub:**
   * Click the blue **"Publish to GitHub"** button.
   * Select **"Publish to GitHub Public Repository"**.
   * Pick `RAG with local LLM` (or rename it if prompted).
   * Uncheck `august_venv` or `chroma_db` if they show up (your `.gitignore` should hide them automatically).
   * Click **OK**.

VS Code will automatically initialize Git, create the GitHub repository under your account, commit your files, and push everything live!

