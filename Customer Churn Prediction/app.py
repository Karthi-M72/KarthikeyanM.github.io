import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide",
)

st.sidebar.header("About This Project")
st.sidebar.markdown("""
This is a Machine Learning solution designed to predict the probability of **customer churn**. The goal is to identify at-risk customers early for targeted intervention.
""")

st.sidebar.subheader("Technical Details")
st.sidebar.markdown("""
- **Core Algorithm:** Optimized XGBoost Classifier
- **Preprocessing:** Includes **One-Hot Encoding**, **StandardScaler**, and **SMOTE** (to handle class imbalance).
- **Performance:** Achieved a robust **97.54% Accuracy**.
""")

st.sidebar.subheader("Impact")
st.sidebar.markdown("The model's predictions drive strategic actions to minimize revenue loss and improve customer lifetime value.")
st.sidebar.markdown("---")
st.sidebar.write("Made by Karthikeyan")

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "model", "preprocessor.pkl")
STYLE_PATH = os.path.join(BASE_DIR, "style.css")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(PREPROCESSOR_PATH, "rb") as f:
        preprocessor = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model or preprocessor: {e}")
    st.stop()

try:
    with open(STYLE_PATH) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Custom CSS not found, using default Streamlit style.")

st.markdown("<h1 class='title'>Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Fill in the details below. Each input has a clear explanation so anyone can understand what it means.</p>",
    unsafe_allow_html=True,
)


vmail_map = {
    "Very Low": 0,
    "Low": 5,
    "Medium": 15,
    "High": 30,
    "Very High": 50,
}
day_calls_map = {
    "Very Low": 20,
    "Low": 60,
    "Medium": 100,
    "High": 150,
    "Very High": 200,
}
eve_calls_map = {
    "Very Low": 20,
    "Low": 60,
    "Medium": 100,
    "High": 150,
    "Very High": 200,
}
night_calls_map = {
    "Very Low": 20,
    "Low": 60,
    "Medium": 100,
    "High": 150,
    "Very High": 200,
}
intl_calls_map = {
    "Very Low": 0,
    "Low": 2,
    "Medium": 5,
    "High": 10,
    "Very High": 20,
}

with st.form("churn_form"):
    st.markdown("<div class='section-header'>Customer Profile</div>", unsafe_allow_html=True)
    account_length = st.slider("How long the customer has been with the company (days)", 0, 500, 120)
    international_plan = st.selectbox("Does the customer have an International Calling Plan?", ["yes", "no"])
    vmail_plan = st.selectbox("Does the customer have a Voicemail Plan?", ["yes", "no"])

    st.markdown("<div class='section-header'>Usage Details</div>", unsafe_allow_html=True)

    vmail_option = st.select_slider("Average Monthly Voicemail Volume", options=list(vmail_map.keys()), value="Medium")
    vmail_message = vmail_map[vmail_option]

    day_option = st.select_slider("Average Monthly Daytime Call Volume", options=list(day_calls_map.keys()), value="Medium")
    day_calls = day_calls_map[day_option]
    day_charge = round(day_calls * 0.30, 2)

    eve_option = st.select_slider("Average Monthly Evening Call Volume", options=list(eve_calls_map.keys()), value="Medium")
    eve_calls = eve_calls_map[eve_option]
    eve_charge = round(eve_calls * 0.15, 2)

    night_option = st.select_slider("Average Monthly Night Call Volume", options=list(night_calls_map.keys()), value="Medium")
    night_calls = night_calls_map[night_option]
    night_charge = round(night_calls * 0.10, 2)

    intl_option = st.select_slider("Average Monthly International Calls", options=list(intl_calls_map.keys()), value="Low")
    international_calls = intl_calls_map[intl_option]
    international_charge = round(international_calls * 0.90, 2) if international_calls > 0 else 2.7

    st.markdown("<div class='section-header'>Service Interaction</div>", unsafe_allow_html=True)
    custServ_calls = st.slider("Number of times the customer called Customer Service", 0, 10, 1)

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame([[
        account_length, international_plan, vmail_plan, vmail_message,
        day_calls, day_charge, eve_calls, eve_charge,
        night_calls, night_charge, international_calls,
        international_charge, custServ_calls
    ]], columns=[
        'account_length', 'international_plan', 'vmail_plan', 'vmail_message',
        'day_calls', 'day_charge', 'eve_calls', 'eve_charge',
        'night_calls', 'night_charge', 'international_calls',
        'international_charge', 'custServ_calls'
    ])

    with st.spinner("Running prediction..."):
        try:
            processed = preprocessor.transform(input_data)
            prediction = model.predict(processed)[0]
            prob = model.predict_proba(processed)[0][1]

            st.success("Prediction complete!")

            if prediction == 1:
                st.markdown(
                    f"<div class='prediction-card churn'>Likely to Churn<br>Probability: {prob:.2%}</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"<div class='prediction-card no-churn'>Not Likely to Churn<br>Probability: {prob:.2%}</div>",
                    unsafe_allow_html=True,
                )

            result_text = f"Customer is {'likely' if prediction == 1 else 'not likely'} to churn with probability {prob:.2%}"
            report = f"""
Customer Churn Prediction Report

Customer Profile
----------------
Account Length: {account_length} days
International Plan: {international_plan}
Voicemail Plan: {vmail_plan}
Voicemail Messages: {vmail_option} (mapped to {vmail_message})

Usage Details
-------------
Daytime Calls: {day_option} (mapped to {day_calls}, cost ≈ ${day_charge})
Evening Calls: {eve_option} (mapped to {eve_calls}, cost ≈ ${eve_charge})
Night Calls: {night_option} (mapped to {night_calls}, cost ≈ ${night_charge})
International Calls: {intl_option} (mapped to {international_calls}, cost ≈ ${international_charge})

Service Interaction
-------------------
Customer Service Calls: {custServ_calls}

Prediction
----------
{result_text}
"""

            st.download_button("Download Report", report, file_name="churn_report.txt")

        except Exception as e:
            st.error(f"Error during prediction: {e}")
