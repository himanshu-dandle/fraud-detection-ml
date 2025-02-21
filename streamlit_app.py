import streamlit as st
import requests
import random

# Set up the Streamlit UI
st.title("💳 Fraud Detection System")
st.write("Enter transaction details and click 'Check Fraud'.")

# Function to generate random transaction values
def generate_random_values():
    return [round(random.uniform(-3, 3), 6) for _ in range(28)] + [random.randint(0, 23)]

# Initialize session state if not already set
if "default_values" not in st.session_state:
    st.session_state.default_values = generate_random_values()

# Function to update session state for new random values
def update_random_values():
    st.session_state.default_values = generate_random_values()
    st.rerun()

# Input fields with default values from session state
features = [f"V{i}" for i in range(1, 29)] + ["Hour"]
user_inputs = {}

for i, feature in enumerate(features):
    if feature == "Hour":
        user_inputs[feature] = st.number_input(feature, value=st.session_state.default_values[i], min_value=0, max_value=23)
    else:
        user_inputs[feature] = st.number_input(feature, value=st.session_state.default_values[i], format="%.6f")

# API URL (Google Cloud Run)
API_URL = "https://fraud-api-941838659836.us-central1.run.app/predict/"

# Function to send request to FastAPI
def get_prediction(data):
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        result = response.json()

        # Check if expected fields are present in the response
        if "prediction" in result and "fraud_probability" in result:
            return result["prediction"], result["fraud_probability"]
        else:
            st.error("⚠ API returned an unexpected response format.")
            return None, None
    except requests.exceptions.RequestException as e:
        st.error(f"⚠ API request failed: {str(e)}")
        return None, None

# Add a "Randomize Values" button
if st.button("🎲 Randomize Values"):
    update_random_values()

# Button to send request
if st.button("🔍 Check Fraud"):
    prediction, probability = get_prediction(user_inputs)

    if prediction is not None:
        if prediction == 1:
            st.error(f"🚨 Fraud Detected! (Probability: {probability:.6f})")
        else:
            st.success(f"✅ Transaction is Safe! (Probability of Fraud: {probability:.6f})")
    else:
        st.error("⚠ Error connecting to API. Please try again.")
