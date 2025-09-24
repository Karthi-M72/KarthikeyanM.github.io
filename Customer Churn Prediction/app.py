import streamlit as st
import pandas as pd
import pickle
import os

# ===========================
# Paths
# ===========================
BASE_DIR = os.path.dirname(__file__)  # Folder containing app.py
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "model", "preprocessor.pkl")
STYLE_PATH = os.path.join(BASE_DIR, "style.css")

# ===========================
# Load model + preprocessor
# ===========================
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file not found at {MODEL_PATH}")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

try:
    with open(PREPROCESSOR_PATH, "rb") as f:
        preprocessor = pickle.load(f)
except FileNotFoundError:
    st.error(f"Preprocessor file not found at {PREPROCESSOR_PATH}")
    st.stop()
except Exception as e:
    st.error(f"Error loading preprocessor: {e}")
    st.stop()

# ===========================
# Load CSS
# ===========================
if os.path.exists(STYLE_PATH):
    with open(STYLE_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning(f"CSS file not found at {STYLE_PATH}. Using default styling.")

# ===========================
# Page Config
# ===========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="centered",
)

# ===========================
# App Header
# ===========================
st.markdown("<h1 class='title'>Customer Churn Prediction</h1>", unsafe_allow_html=True)
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

    submitted = st.form_submit_button("Predict")

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

    try:
        processed = preprocessor.transform(input_data)
        prediction = model.predict(processed)[0]
        prob = model.predict_proba(processed)[0][1]

        if prediction == 1:
            st.markdown(f"<div class='card red'>Likely to Churn<br><span class='prob'>Probability: {prob:.2%}</span></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='card green'>Not Likely to Churn<br><span class='prob'>Probability: {prob:.2%}</span></div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error during prediction: {e}")
