import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time

# Custom CSS for improved styling
st.markdown(
    """
    <style>
        .big-title {
            font-size: 3.5rem !important;
            font-weight: bold;
            text-align: center;
            color: #00C8FF;
            text-shadow: 2px 2px 10px rgba(0, 200, 255, 0.8);
        }
        .sub-title {
            font-size: 1.4rem;
            text-align: center;
            color: #CCCCCC;
            margin-bottom: 30px;
        }
        .section-title {
            font-size: 2rem;
            font-weight: bold;
            margin-top: 40px;
            color: #FFFFFF;
            border-bottom: 2px solid #00C8FF;
            padding-bottom: 5px;
        }
        .feature-card {
            background: linear-gradient(135deg, rgba(0,200,255,0.2), rgba(255,255,255,0.1));
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 15px;
            transition: transform 0.2s ease-in-out;
        }
        .feature-card:hover {
            transform: scale(1.05);
        }
        .metric-card {
            background: linear-gradient(135deg, rgba(0,200,255,0.2), rgba(255,255,255,0.1));
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        .metric-card h3 {
            font-size: 2rem;
            font-weight: bold;
        }
        .metric-card p {
            font-size: 1.2rem;
            color: #CCCCCC;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display hero image in a stylish way

# Title and Subtitle
st.markdown("<p class='big-title'>🚀 Welcome to MediScope</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>🩺 Smarter Healthcare, Faster Insights</p>", unsafe_allow_html=True)

# Features Section
st.markdown("<p class='section-title'>Why Choose MediScope?</p>", unsafe_allow_html=True)
cols = st.columns(2)
with cols[0]:
    st.markdown("<div class='feature-card'>💬 AI-Powered Medical Assistant</div>", unsafe_allow_html=True)
    st.markdown("<div class='feature-card'>🔎 Smart Medical Knowledge Retrieval (RAG)</div>", unsafe_allow_html=True)
with cols[1]:
    st.markdown("<div class='feature-card'>🛑 ICU Risk Prediction for Critical Patients</div>", unsafe_allow_html=True)
    st.markdown("<div class='feature-card'>📊 Real-time Patient Monitoring & Insights</div>", unsafe_allow_html=True)

# KPI Cards
st.markdown("<p class='section-title'>Real-Time Patient Statistics</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.metric("Heart Rate (BPM)", "72", "+2")
col2.metric("Oxygen Levels (%)", "98", "-1")
col3.metric("ICU Risk Score", "45", "+5")

# Additional Attractive Metrics Section
st.markdown("<p class='section-title'>Vital Signs and Stats</p>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='metric-card'><h3>Temperature (°C)</h3><p>36.8°C</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-card'><h3>Blood Pressure</h3><p>120/80 mmHg</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'><h3>Respiratory Rate</h3><p>18 Breaths/min</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-card'><h3>Temperature Trends</h3><p>Increasing</p></div>", unsafe_allow_html=True)

# ICU Risk Gauge
st.markdown("<p class='section-title'>Live ICU Risk Gauge</p>", unsafe_allow_html=True)
icu_risk = st.progress(0)
for i in range(1, 101, 10):
    time.sleep(0.1)
    icu_risk.progress(i)

# Graphs Section
st.markdown("<p class='section-title'>ICU Risk Prediction Over Time</p>", unsafe_allow_html=True)
time_series = pd.DataFrame({'Time': np.arange(1, 21), 'ICU Risk Score': np.random.randint(20, 100, 20)})
fig1 = px.line(time_series, x='Time', y='ICU Risk Score', title='ICU Risk Score Over Time', markers=True)
st.plotly_chart(fig1)

st.markdown("<p class='section-title'>Patient Health Trends</p>", unsafe_allow_html=True)
health_trends = pd.DataFrame({
    'Day': np.arange(1, 15),
    'Heart Rate': np.random.randint(60, 100, 14),
    'Oxygen Levels': np.random.randint(85, 100, 14)
})
fig2 = px.line(health_trends, x='Day', y=['Heart Rate', 'Oxygen Levels'], title='Heart Rate & Oxygen Levels Trend')
st.plotly_chart(fig2)

# Footer
st.markdown("---")
st.write("© 2025 MediScope - AI-Powered Medical Insights")
