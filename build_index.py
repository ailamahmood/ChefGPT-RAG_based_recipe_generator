# build_index.py
import os
import pandas as pd
import magic  # For detecting MIME types of files
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Directory paths and file constants
BOOKS_DIR = "data/books"
CSV_PATH = "data/recipes_dataset.csv"
INDEX_PATH = "index/faiss_combined_index"

# Checks if the file is a valid PDF using MIME type
def is_valid_pdf(filepath):
    mime_type = magic.from_file(filepath, mime=True)
    return mime_type == "application/pdf"

# Loads and extracts documents from all PDF books in the specified directory
def load_all_books():
    documents = []
    for filename in os.listdir(BOOKS_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(BOOKS_DIR, filename)

            if not is_valid_pdf(filepath):
                print(f"❌ Skipping {filename}: Not a valid PDF.")
                continue

            try:
                loader = PyPDFLoader(filepath)  # Loads the PDF file
                docs = loader.load()  # Extracts content as documents
                documents.extend(docs)
                print(f"✅ Loaded: {filename} ({len(docs)} pages)")
            except Exception as e:
                print(f"⚠️ Error loading {filename}: {e}")
    return documents

# Converts each row in the CSV into a Document object
def load_csv_as_documents():
    try:
        df = pd.read_csv(CSV_PATH)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return []

    docs = []
    for _, row in df.iterrows():
        content = f"Title: {row.get('title', '')}\nIngredients: {row.get('ingredients', '')}\nInstructions: {row.get('steps', '')}"
        docs.append(Document(page_content=content))
    print(f"✅ Loaded {len(docs)} documents from CSV.")
    return docs

# Main function to build the FAISS index from books and CSV documents
def build_index():
    print("🔍 Loading documents from books and CSV...")
    book_docs = load_all_books()
    csv_docs = load_csv_as_documents()

    # Combine all documents
    all_docs = book_docs + csv_docs
    print(f"📄 Total combined documents: {len(all_docs)}")

    # Split documents into smaller chunks for better embedding and retrieval
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(all_docs)
    print(f"✂️ Split into {len(chunks)} chunks.")

    # Generate embeddings and build FAISS vector index
    print("📦 Generating embeddings and building FAISS index...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_PATH)
    print(f"✅ FAISS index built and saved to '{INDEX_PATH}'.")

# Execute index building if run as a script
if __name__ == "__main__":
    build_index()
