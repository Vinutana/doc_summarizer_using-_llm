# LLM Text Summarizer using Gemini API

This project is a **lightweight Large Language Model (LLM) application** built using the **Google Gemini API**.  
It focuses on a simple but practical use case: **summarizing long text into concise notes for quick revision**.

The goal of this project is to understand how to:
- Use an LLM API correctly
- Design prompts for summarization
- Build a minimal UI using Streamlit
- Perform basic qualitative and semantic evaluation of LLM outputs

---

## 🚀 Features

- Text summarization using Gemini LLM
- Streamlit-based interactive UI
- Secure API key handling using `.env`
- Manual + semantic evaluation of generated outputs
- Beginner-friendly project structure (no RAG, no vector DB)

---

## 📂 Project Structure


llm1/
│── streamlit_app.py # Streamlit app for summarization
│── manual_evaluation.py # Semantic similarity evaluation
│── config.py # Loads Gemini API key
│── requirements.txt # Project dependencies
│── .env # API key (not pushed to GitHub)
│── .gitignore # Ignored files
│── README.md # Project documentation


---

## 🧠 Problem Statement

Students and learners often struggle to revise **large chunks of text** efficiently.

Reading entire notes repeatedly is time-consuming and ineffective.

---

## ✅ Solution

This project uses a **Large Language Model (Gemini)** to:
- Accept long text input
- Generate concise summaries
- Help users quickly revise important concepts

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/LLM_Summarizer_Gemini.git
cd llm1
2. Create a Virtual Environment
bash
Copy code
python -m venv .venv
3. Activate the Virtual Environment
Windows (PowerShell):

powershell
Copy code
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
If PowerShell is restricted, use:

powershell
Copy code
.\.venv\Scripts\activate.bat
4. Install Dependencies
bash
Copy code
pip install -r requirements.txt
5. Set Up Gemini API Key
Create a .env file in the project root:

ini
GEMINI_API_KEY=your_api_key_here
⚠️ Do NOT push .env to GitHub.

▶️ Run the Streamlit App
bash
streamlit run streamlit_app.py
Open the browser link shown in the terminal

Paste text into the input box

Click Summarize

View the generated summary

🧪 Manual & Semantic Evaluation
LLM outputs are evaluated using qualitative checks and semantic similarity.

What is evaluated:
Accuracy of the summary

Preservation of key ideas

Conciseness

Instruction-following behavior

Semantic Similarity Evaluation
The project includes a basic evaluation script using sentence embeddings:

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

def semantic_score(reference, generated):
    ref_emb = model.encode([reference])
    gen_emb = model.encode([generated])
    return cosine_similarity(ref_emb, gen_emb)[0][0]



This provides a rough similarity score (0–1) between:

A reference summary

The LLM-generated output

Note: This metric is used as a supporting signal, not as a definitive evaluation.

📌 Key Learnings
Prompt clarity significantly affects output quality

LLMs can be useful even without retrieval or fine-tuning

Evaluation of LLMs is largely qualitative

Simple, focused projects are better than over-engineered ones

🔮 Future Improvements
Improve prompt design

Add batch evaluation

Add UI-based comparison of outputs

Explore different Gemini models

⚠️ Disclaimer
This project is for learning and demonstration purposes.
It does not claim state-of-the-art performance or production readiness.

📣 Tech Stack
Python
Google Gemini API
Streamlit
Sentence Transformers
scikit-learn

📄 License
This project is open for educational use.


