import streamlit as st

# Set page config
st.set_page_config(page_title="MediScope's Diagnostic Assistant", layout="wide")

# Custom CSS for the new neon glow effect
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 3.5rem;
            font-weight: bold;
            color: #E0FFFF;
            text-shadow: 0 0 15px #00FFFF, 0 0 30px #0088CC;
            margin-bottom: 5px;
        }
        .subtext {
            text-align: center;
            font-size: 1.8rem;
            font-weight: bold;
            color: #D6D6D6;
            text-shadow: 0 0 8px #0099FF;
            margin-bottom: 25px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
        }
        .custom-button {
            background-color: #00C8FF;
            color: black;
            font-size: 20px;
            font-weight: bold;
            padding: 15px 30px;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s;
            width: 280px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            border: none;
            box-shadow: 0 0 8px #00C8FF, 0 0 16px #0088CC;
        }
        .custom-button:hover {
            background-color: #0088CC;
            box-shadow: 0 0 12px #0088CC, 0 0 24px #005580;
        }
        .disclaimer-box {
            background: #112233;
            color: #00C8FF;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 1rem;
            box-shadow: 0 0 8px #00C8FF;
        }
    </style>
""", unsafe_allow_html=True)

# Main layout
st.markdown("<div class='main-title'>💡 MediScope's</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Diagnostic Assistant</div>", unsafe_allow_html=True)

# Buttons container
st.markdown("""
    <div class="button-container">
        <a href="http://localhost:8505/" target="_self">
            <button class="custom-button">💬 Diagnosis Assistant</button>
        </a>
        <a href="http://127.0.0.1:8000" target="_self">
            <button class="custom-button">📡 Medical RAG</button>
        </a>
    </div>
""", unsafe_allow_html=True)

# Info message
st.markdown("---")
st.markdown('<div class="disclaimer-box">🚀 **Disclaimer:** This platform provides AI-generated insights but is <b>not a replacement for professional medical advice.</b></div>', unsafe_allow_html=True)
