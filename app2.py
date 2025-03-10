import streamlit as st
import google.generativeai as genai
from config import api_key

# Configure AI Model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Define UI
st.title("🫀 AI-Powered Injury Severity Prediction ")
st.write("Fill in the patient details below to get an AI-assisted diagnosis.")

# Define numerical and binary (Yes/No) features
numerical_features = [
    "AGE", "TLC", "GLUCOSE", "CREATININE", "EF", "HB", 
    "PLATELETS", "UREA", "BNP", "HIGH_RISK_SCORE"
]

binary_features = [
    "SMOKING", "ALCOHOL", "DM", "HTN", "CAD", "PRIOR CMP", "CKD", 
    "RAISED CARDIAC ENZYMES", "SEVERE ANAEMIA", "ANAEMIA", "STABLE ANGINA", 
    "ACS", "STEMI", "ATYPICAL CHEST PAIN", "HEART FAILURE", "HFREF", 
    "HFNEF", "VALVULAR", "CHB", "SSS", "AKI", "CVA INFRACT", "CVA BLEED", 
    "AF", "VT", "PSVT", "CONGENITAL", "UTI", "NEURO CARDIOGENIC SYNCOPE",
    "ORTHOSTATIC", "INFECTIVE ENDOCARDITIS", "DVT", "CARDIOGENIC SHOCK", 
    "SHOCK", "PULMONARY EMBOLISM", "CHEST INFECTION", "GENDER_M", "RURAL_U", 
    "TYPE OF ADMISSION-EMERGENCY/OPD_O", "Internal_Bleeding_Location_None"
]

# User inputs
st.subheader("🔢 Numerical Inputs")
input_data = {}

col1, col2 = st.columns(2)
for i, feature in enumerate(numerical_features):
    col = col1 if i % 2 == 0 else col2
    input_data[feature] = col.slider(f"{feature}:", 0.0, 100.0, 50.0)

st.subheader("✅ Yes/No Inputs")
cols = st.columns(4)
for i, feature in enumerate(binary_features):
    with cols[i % 4]:
        input_data[feature] = int(st.checkbox(feature))  # Convert to 0/1

# Rule-based classification
if st.button("🚀 Predict Severity"):
    age = input_data["AGE"]
    ef = input_data["EF"]
    risk_score = input_data["HIGH_RISK_SCORE"]

    # High severity conditions
    if (
        age > 65 or ef < 35 or risk_score > 75 or
        input_data["CARDIOGENIC SHOCK"] or input_data["PULMONARY EMBOLISM"] or
        input_data["HEART FAILURE"]  # Now always Severe
    ):
        severity = "Severe"
    elif (
        40 <= age <= 65 or 35 <= ef <= 50 or 50 <= risk_score <= 75 or
        input_data["ACS"]
    ):
        severity = "Moderate"
    else:
        severity = "Mild"

    # Additional Predictions
    internal_bleeding = "High Risk" if input_data["CVA BLEED"] or input_data["SEVERE ANAEMIA"] else "Low Risk"
    cardiac_event_risk = "High" if input_data["HEART FAILURE"] or input_data["CAD"] or ef < 40 else "Low"
    icu_admission = "Recommended" if risk_score > 80 or input_data["CARDIOGENIC SHOCK"] else "Not Required"
    
    # Generate AI Diagnosis
    user_input_text = "\n".join([f"{key}: {value}" for key, value in input_data.items()])
    ai_prompt = f"Based on the following patient data, provide a detailed AI diagnosis:\n{user_input_text}"
    response = model.generate_content([ai_prompt])
    ai_diagnosis = response.text if response and response.text else "AI could not generate a diagnosis."
    
    st.success(f"🔍 Predicted Injury Severity: **{severity}**")
    st.markdown("### 🏥 AI Diagnosis")
    st.write(ai_diagnosis)
    
    st.markdown("### 🔬 Additional Predictions")
    st.write(f"🩸 **Risk of Internal Bleeding:** {internal_bleeding}")
    st.write(f"❤️ **Likelihood of Cardiac Event:** {cardiac_event_risk}")
    st.write(f"🏥 **ICU Admission Required?** {icu_admission}")
