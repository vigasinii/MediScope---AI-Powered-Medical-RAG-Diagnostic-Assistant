# MediScope's Diagnostic Assistant

## Overview
MediScope's Diagnostic Assistant is an AI-powered tool that analyzes medical images and documents, providing diagnostic insights and assisting with medical queries. The application utilizes a Retrieval-Augmented Generation (RAG) system for enhanced information retrieval and integrates a local large language model (LLM) for AI-driven responses.

## Features
- **Medical Image & Document Analysis**: Upload PNG, JPG, JPEG, or PDF files for AI-based analysis.
- **AI Chatbot**: Ask questions based on uploaded medical documents or general medical topics.
- **Retrieval-Augmented Generation (RAG)**: Enhances AI responses by retrieving relevant medical knowledge.
- **Local LLM Integration**: Uses `meditron-7b.Q4_K_M.gguf` with CTransformers for on-device inference.
- **Vector Database (Qdrant)**: Stores and retrieves embeddings for efficient search and response generation.
- **FastAPI Backend**: Provides API endpoints for querying the RAG system.
- **Streamlit Frontend**: User-friendly interface with interactive components.

## Project Structure
```
├── app.py          # Main Streamlit app for user interface
├── config.py       # Configuration file (API keys and settings)
├── home.py         # Landing page with navigation buttons
├── ingest.py       # Loads and indexes PDF documents into the vector database
├── rag.py          # FastAPI-based retrieval-augmented generation (RAG) system
├── retriever.py    # Queries vector database for relevant document retrieval
└── README.md       # Project documentation
```

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Streamlit
- FastAPI
- LangChain
- SentenceTransformer
- Qdrant
- PyPDF2
- Google Generative AI SDK (if using Gemini model)
- CTransformers

### Setup
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the vector database (Qdrant) locally:
   ```sh
   docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
   ```
4. Download Meditron 
https://huggingface.co/TheBloke/meditron-7B-GGUF/blob/main/meditron-7b.Q4_K_M.gguf

## Usage
### Running the Application
**Note:** Each component must be run in a **separate terminal** in the following order.

```sh
# 1️⃣ Run the Ingestion Pipeline  
python ingest.py  

# 2️⃣ Start the FastAPI RAG Backend  
uvicorn rag:app --reload --host 127.0.0.1 --port 8000  
This may take about 2-3 to show up after the query is given, please do not refresh

# 3️⃣ Run the Streamlit App  
streamlit run app.py  

# 4️⃣ Start the Home Page  
streamlit run home.py



## Configuration
Edit `config.py` to update the API key for Google Generative AI if required:
```python
api_key = "YOUR_API_KEY"
```

## How It Works
1. **Ingestion**: `ingest.py` loads and processes medical PDFs, converting them into embeddings stored in Qdrant.
2. **Retrieval**: `retriever.py` fetches relevant content based on user queries.
3. **LLM Response**: `rag.py` processes queries with Meditron LLM, generating insightful answers.
4. **Frontend Interaction**: Users interact with the AI model via the `app.py` Streamlit UI.

## Disclaimer
This tool provides AI-generated insights but **is not a replacement for professional medical advice**. Always consult a healthcare professional for medical decisions.

## Testing
Home: 
![image](https://github.com/user-attachments/assets/3d60d69f-9bf3-4f46-a213-47369e63adf3)

Diagnostic Assistant Testing:

![WhatsApp Image 2025-02-26 at 10 45 03_ef3c1cf7](https://github.com/user-attachments/assets/d1bc23b5-9b40-4e53-be89-72a49607b95d)

![image](https://github.com/user-attachments/assets/9f637a1b-38ad-4799-a1e9-fddb62430d8a)

![Screenshot 2025-02-26 110424](https://github.com/user-attachments/assets/00e0ad54-f012-4ba8-a708-7fd426913495)

![Screenshot 2025-02-26 111600](https://github.com/user-attachments/assets/848efac8-c71b-40f3-865f-374a47a2579d)

![Screenshot 2025-02-26 111626](https://github.com/user-attachments/assets/1aa5f3b4-6978-4935-8bc7-396d962fe3b5)

