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
V1 = st.number_input("V1", value=st.session_state.default_values[0], format="%.6f")
V2 = st.number_input("V2", value=st.session_state.default_values[1], format="%.6f")
V3 = st.number_input("V3", value=st.session_state.default_values[2], format="%.6f")
V4 = st.number_input("V4", value=st.session_state.default_values[3], format="%.6f")
V5 = st.number_input("V5", value=st.session_state.default_values[4], format="%.6f")
V6 = st.number_input("V6", value=st.session_state.default_values[5], format="%.6f")
V7 = st.number_input("V7", value=st.session_state.default_values[6], format="%.6f")
V8 = st.number_input("V8", value=st.session_state.default_values[7], format="%.6f")
V9 = st.number_input("V9", value=st.session_state.default_values[8], format="%.6f")
V10 = st.number_input("V10", value=st.session_state.default_values[9], format="%.6f")
V11 = st.number_input("V11", value=st.session_state.default_values[10], format="%.6f")
V12 = st.number_input("V12", value=st.session_state.default_values[11], format="%.6f")
V13 = st.number_input("V13", value=st.session_state.default_values[12], format="%.6f")
V14 = st.number_input("V14", value=st.session_state.default_values[13], format="%.6f")
V15 = st.number_input("V15", value=st.session_state.default_values[14], format="%.6f")
V16 = st.number_input("V16", value=st.session_state.default_values[15], format="%.6f")
V17 = st.number_input("V17", value=st.session_state.default_values[16], format="%.6f")
V18 = st.number_input("V18", value=st.session_state.default_values[17], format="%.6f")
V19 = st.number_input("V19", value=st.session_state.default_values[18], format="%.6f")
V20 = st.number_input("V20", value=st.session_state.default_values[19], format="%.6f")
V21 = st.number_input("V21", value=st.session_state.default_values[20], format="%.6f")
V22 = st.number_input("V22", value=st.session_state.default_values[21], format="%.6f")
V23 = st.number_input("V23", value=st.session_state.default_values[22], format="%.6f")
V24 = st.number_input("V24", value=st.session_state.default_values[23], format="%.6f")
V25 = st.number_input("V25", value=st.session_state.default_values[24], format="%.6f")
V26 = st.number_input("V26", value=st.session_state.default_values[25], format="%.6f")
V27 = st.number_input("V27", value=st.session_state.default_values[26], format="%.6f")
V28 = st.number_input("V28", value=st.session_state.default_values[27], format="%.6f")
Hour = st.number_input("Transaction Hour (0-23)", value=st.session_state.default_values[28], min_value=0, max_value=23)

# API URL (Google Cloud Run)
API_URL = "https://fraud-api-941838659836.us-central1.run.app/predict/"

# Function to send request to FastAPI
def get_prediction():
    data = {
        "V1": V1, "V2": V2, "V3": V3, "V4": V4, "V5": V5, "V6": V6, "V7": V7, "V8": V8, "V9": V9, "V10": V10,
        "V11": V11, "V12": V12, "V13": V13, "V14": V14, "V15": V15, "V16": V16, "V17": V17, "V18": V18, "V19": V19,
        "V20": V20, "V21": V21, "V22": V22, "V23": V23, "V24": V24, "V25": V25, "V26": V26, "V27": V27, "V28": V28,
        "Hour": Hour
    }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["prediction"], result["fraud_probability"]
    else:
        return None, None

# Add a "Randomize Values" button
if st.button("🎲 Randomize Values"):
    update_random_values()

# Button to send request
if st.button("🔍 Check Fraud"):
    prediction, probability = get_prediction()
    
    if prediction is not None:
        if prediction == 1:
            st.error(f"🚨 Fraud Detected! (Probability: {probability:.6f})")
        else:
            st.success(f"✅ Transaction is Safe! (Probability of Fraud: {probability:.6f})")
    else:
        st.error("⚠ Error connecting to API. Please try again.")
