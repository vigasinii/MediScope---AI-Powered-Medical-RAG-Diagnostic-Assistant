import streamlit as st
import google.generativeai as genai
import imghdr
from PyPDF2 import PdfReader
from config import api_key

# Configure Page
st.set_page_config(page_title="MediScope's Assistant", page_icon="💡", layout="centered")

# Custom CSS for White Chatboxes
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #0D0D0D !important;
            color: #E0E0E0 !important;
        }
        .stButton>button {
            background: linear-gradient(90deg, #00E3FF, #0095FF);
            color: black;
            font-weight: bold;
            border-radius: 12px;
            padding: 12px 24px;
            font-size: 18px;
            border: none;
            transition: 0.3s;
            box-shadow: 0px 0px 12px rgba(0, 227, 255, 0.5);
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #00C3FF, #0075FF);
            box-shadow: 0px 0px 18px rgba(0, 195, 255, 0.8);
        }
        .stTextInput>div>div>input, .stFileUploader>div>div>input {
            background-color: #1A1A1A;
            color: white;
            border-radius: 10px;
            border: 1px solid #00E3FF;
            padding: 12px;
            font-size: 16px;
        }
        h1 {
            text-align: center;
            color: #00E3FF;
            text-shadow: 0px 0px 12px rgba(0, 227, 255, 0.8);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Configure AI Model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# UI Header
st.markdown("<h1>💡MediScope's  </h1>", unsafe_allow_html=True)

st.markdown("""  
    <h3 style="text-align: center;">Diagnostic Assistant</h3>  
""", unsafe_allow_html=True)

st.markdown("---")

# File Upload Section
uploaded_files = st.file_uploader("📤 Upload Medical Image or PDF", type=["png", "jpg", "jpeg", "pdf"], accept_multiple_files=True)
analyze_button = st.button("🔍 Analyze Uploads")

# Store extracted content from uploads
if "file_content" not in st.session_state:
    st.session_state.file_content = ""

# Processing Uploaded Files
if uploaded_files and analyze_button:
    file_content = ""
    for file in uploaded_files:
        file_type = file.type
        st.markdown(f"### 🔎 Processing: {file.name}")
        
        if file_type in ["image/png", "image/jpeg"]:
            st.image(file, caption=f"🖼 {file.name}", use_column_width=True)
            image_data = file.getvalue()
            mime_type = f"image/{imghdr.what(None, h=image_data)}"
            response = model.generate_content(["Analyze the medical image:", {"mime_type": mime_type, "data": image_data}])
            file_content += response.text if response and response.text else ""

        elif file_type == "application/pdf":
            reader = PdfReader(file)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            if text:
                response = model.generate_content(["Summarize the medical document:", text])
                file_content += response.text if response and response.text else ""
            else:
                st.warning("⚠️ Could not extract text from this PDF.")

    st.session_state.file_content = file_content  # Store extracted content
    st.markdown("### 📄 AI Extracted Insights")
    st.write(file_content if file_content else "No insights extracted.")

st.markdown("---")

# AI Chatbot
st.subheader("💬 AI Medical Chatbot")
tab1, tab2 = st.tabs(["📄 Ask from Uploaded Image or Report", "⚕️ General Medical Question"])

with tab1:
    st.write("Ask a question based on the uploaded image or report:")
    pdf_query = st.text_input("🔍 Ask about the uploaded document:")

    if pdf_query:
        with st.spinner("🔎 Analyzing Uploaded File..."):
            chatbot_prompt = f"Use this extracted data: {st.session_state.file_content}\nUser query: {pdf_query}"
            chatbot_response = model.generate_content([chatbot_prompt])
            if chatbot_response and chatbot_response.text:
                st.markdown(f"**AI:** {chatbot_response.text}")
            else:
                st.error("❌ AI could not generate a response. Try again.")

with tab2:
    st.write("Ask a general medical question:")
    medical_query = st.text_input("🔍 Ask a medical-related question:")

    if medical_query:
        with st.spinner("🔎 Thinking..."):
            chatbot_response = model.generate_content([medical_query])
            if chatbot_response and chatbot_response.text:
                st.markdown(f"**AI:** {chatbot_response.text}")
            else:
                st.error("❌ AI could not generate a response. Try again.")

# How It Works Section
with st.expander("ℹ️ How It Works"):
    st.write("""
    1️⃣ **Upload a medical image or PDF**  
    2️⃣ **AI analyzes and extracts insights**  
    3️⃣ **Ask questions from the uploaded document or general medical topics**  
    4️⃣ **Get AI-powered responses instantly**  
    """)

st.success("✅ AI Ready for Analysis & Questions!")
