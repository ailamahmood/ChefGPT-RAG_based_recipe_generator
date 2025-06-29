# query_engine.py
import os
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings

# Set Groq API key for accessing the LLM (replace this key with your secure key)
os.environ["OPENAI_API_KEY"] = "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"

# Path to the pre-built FAISS index
INDEX_PATH = "index/faiss_combined_index"

# Function to get a recipe based on user input query
def get_recipe_from_query(user_query):
    # Load the same embedding model used to build the index
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Load the FAISS vector index with document embeddings
    vectorstore = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

    # Set up the LLM using Groq's LLaMA 3 model via OpenAI-compatible API
    llm = ChatOpenAI(
        model="llama3-70b-8192",
        base_url="https://api.groq.com/openai/v1",
        temperature=0.3,  # Lower temperature for more deterministic output
        max_tokens=600   # Limit on response length
    )

    # Create a RetrievalQA chain that combines the retriever with the LLM
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", k=4),  # Retrieves top 4 most similar chunks
        return_source_documents=False  # We're not returning the source chunks, just the final answer
    )

    # Custom prompt to guide the LLM to return a well-formatted recipe
    prompt = f"""
You are a recipe expert. Based on the following query, return a well-structured recipe. Do not mention whether the recipe is an exact match or not. Your output must include:

1. **Recipe Name**
2. **Ingredients**
3. **Instructions/Steps**

Add 2-3 lines note in end.

User Query: {user_query}
"""
    # Run the RetrievalQA chain with the prompt and return the response
    result = qa.run(prompt)
    return result.strip()
