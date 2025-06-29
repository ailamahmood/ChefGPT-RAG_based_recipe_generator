# ChefGPT 🍽️ – RAG-Based Recipe Generator

ChefGPT is a **Retrieval-Augmented Generation (RAG)**-based AI system designed to generate personalized recipes based on available ingredients and user preferences. It combines a large corpus of recipe data with vector-based semantic search and generative AI to provide relevant, creative, and useful recipe suggestions.

## 🚀 Features

- 🥦 Input-based recipe generation using ingredients and dietary preferences.
- 📚 Vector store created from 60,000+ recipes and 67+ recipe books.
- 🧠 Uses FAISS for efficient similarity search.
- 🗣️ Natural language responses generated via LLM (OpenAI GPT-4 or similar).
- 🌍 Future-ready architecture for cuisine-specific generation and filtering.

---

## 🧩 Architecture

User Input (Ingredients, Preferences)
↓
Query Construction
↓
Semantic Search (FAISS + Embedded Recipes)
↓
Relevant Recipe Context (Top-K)
↓
Prompt to LLM (RAG)
↓
Generated Recipe (Name, Ingredients, Steps)


---

## 📦 Dataset

- **67 Recipe Books (PDFs)** – Converted to text and embedded
- Preprocessing done using `langchain`, `PyMuPDF`, `pandas`, and `tqdm`.


---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/chefgpt.git
cd chefgpt

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
