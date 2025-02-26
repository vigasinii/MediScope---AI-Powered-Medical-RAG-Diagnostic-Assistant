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

## Usage
### Running the Application
1. **Start the FastAPI RAG Backend**
   ```sh
   uvicorn rag:app --reload --host 127.0.0.1 --port 8000
   ```
2. **Run the Streamlit App**
   ```sh
   streamlit run app.py
   ```
3. **Upload Medical Files**
   - Navigate to the web interface
   - Upload images or PDFs for AI analysis
   - Ask AI-powered medical questions

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

## License
This project is open-source. Feel free to modify and extend it.

