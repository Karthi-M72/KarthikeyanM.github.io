import streamlit as st
import pickle
import pandas as pd

# ===========================
# Load model + preprocessor
# ===========================
model = pickle.load(open("model.pkl", "rb"))
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered",
    page_icon="📊",
)

# ===========================
# Custom CSS
# ===========================
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ===========================
# App Header
# ===========================
st.markdown("<h1 class='title'>📊 Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Enter customer details to predict churn likelihood</p>", unsafe_allow_html=True)

# ===========================
# Input Form
# ===========================
with st.form("churn_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior_citizen = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, step=1)

    with col2:
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=0.1)
        total_charges = st.number_input("Total Charges", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🚀 Predict")

# ===========================
# Prediction
# ===========================
if submitted:
    input_data = pd.DataFrame([[
        gender, senior_citizen, partner, dependents, tenure,
        phone_service, internet_service, contract,
        monthly_charges, total_charges
    ]], columns=[
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
        'PhoneService', 'InternetService', 'Contract',
        'MonthlyCharges', 'TotalCharges'
    ])

    processed = preprocessor.transform(input_data)
    prediction = model.predict(processed)[0]
    prob = model.predict_proba(processed)[0][1]

    if prediction == 1:
        st.markdown(f"<div class='card red'>⚠️ Likely to Churn<br><span class='prob'>Probability: {prob:.2%}</span></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='card green'>✅ Not Likely to Churn<br><span class='prob'>Probability: {prob:.2%}</span></div>", unsafe_allow_html=True)
