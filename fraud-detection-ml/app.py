import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn

# Load trained model
model = joblib.load("models/XGBoost.pkl")

# Initialize FastAPI
app = FastAPI()

# Define expected JSON request format
class TransactionData(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Hour: float  # Using "Hour" instead of "Log_Amount"

@app.get("/")
def home():
    return {"message": "Fraud Detection API is Running on Google Cloud Run!"}

@app.post("/predict/")
def predict_fraud(data: TransactionData):
    df = pd.DataFrame([data.dict()])  # Convert input JSON to DataFrame

    # Ensure column names match the model's expected features
    expected_features = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                         'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
                         'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',
                         'Hour']  # Using "Hour"

    df = df[expected_features]  # Reorder features to match training data

    # Predict fraud probability
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0, 1]

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }

# Run FastAPI using dynamic port selection for Google Cloud Run
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    uvicorn.run(app, host="0.0.0.0", port=port)
