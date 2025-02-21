🚀 Fraud Detection System (Machine Learning & FastAPI)
🔗 Live Web App: Click Here to Try!
💻 GitHub Repository: fraud-detection-ml
📌 Project Overview
This AI-powered Fraud Detection System identifies fraudulent transactions in real-time using Machine Learning (XGBoost, Scikit-Learn) and is deployed with FastAPI (Backend) & Streamlit (Frontend).

✅ Key Features:
🔹 Real-Time Fraud Prediction – Users enter transaction data & get instant fraud probability.
🔹 Machine Learning Model – Uses XGBoost, trained on an imbalanced credit card fraud dataset.
🔹 FastAPI Backend – Hosted on Google Cloud Run for real-time predictions.
🔹 Streamlit Web UI – Provides an easy-to-use frontend, deployed on Streamlit Cloud.

📌 Tech Stack Used
🏗 Machine Learning & Data Science
Python
XGBoost
Scikit-Learn
Imbalanced-Learn
Pandas & NumPy
Matplotlib & Seaborn (for visualization)
🌍 Backend (FastAPI API on Google Cloud)
FastAPI
Uvicorn
Joblib (for model serialization)
Deployed on: Google Cloud Run
🎨 Frontend (Web UI on Streamlit Cloud)
Streamlit
Requests (to connect with FastAPI)
Deployed on: Streamlit Cloud
📌 Project Structure
bash
Copy
Edit
fraud-detection-ml/
│── data/                    # Folder for raw and processed datasets (ignored in Git)
│── models/                  # Folder for trained machine learning models (ignored in Git)
│── reports/                 # Generated reports, confusion matrices, etc.
│── scripts/                 # Helper scripts for training & deployment
│── fraud_detection.ipynb     # Jupyter Notebook for model training
│── app.py                    # FastAPI backend (Deployed on Google Cloud Run)
│── streamlit_app.py          # Streamlit frontend (Deployed on Streamlit Cloud)
│── Dockerfile                # Configuration for deploying FastAPI on Google Cloud Run
│── requirements.txt          # All dependencies for FastAPI & Streamlit
│── .gitignore                # Excludes large files & unnecessary folders
│── .gcloudignore             # Excludes unnecessary files from Google Cloud deployment
└── README.md                 # Project documentation (this file)
📌 How to Run the Project Locally
✅ 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/himanshu-dandle/fraud-detection-ml.git
cd fraud-detection-ml
✅ 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ 3. Run FastAPI Backend (Local Server)
bash
Copy
Edit
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
🔹 API will be available at http://localhost:8000/
🔹 Test it using Postman or cURL.

✅ 4. Run Streamlit Web UI (Local App)
bash
Copy
Edit
streamlit run streamlit_app.py
🔹 This will open the web app at http://localhost:8501/
🔹 Users can input transaction data & check fraud probability!

📌 How to Deploy (For Advanced Users)
🚀 Deploying Backend (FastAPI) on Google Cloud Run
bash
Copy
Edit
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/fraud-api
gcloud run deploy fraud-api --image gcr.io/YOUR_PROJECT_ID/fraud-api --platform managed --region us-central1 --allow-unauthenticated
🔹 This will host the FastAPI backend online for public use.

🚀 Deploying Web UI (Streamlit) on Streamlit Cloud
1️⃣ Upload the project to GitHub
2️⃣ Go to Streamlit Cloud
3️⃣ Select your GitHub Repo
4️⃣ Set the Main File Path → streamlit_app.py
5️⃣ Click Deploy 🚀

🔹 After a few minutes, your public Streamlit App will be live!

📌 API Usage (Example Request & Response)
✅ Request Example (POST Request)
📌 Send JSON data to FastAPI for fraud detection:

json
Copy
Edit
{
    "V1": -1.359,
    "V2": -0.072,
    "V3": 2.536,
    "V4": 1.378,
    "V5": -0.338,
    "V6": 0.462,
    "V7": 0.239,
    "V8": 0.098,
    "V9": 0.363,
    "V10": 0.090,
    "V11": -0.551,
    "V12": -0.617,
    "V13": -0.991,
    "V14": -0.311,
    "V15": 1.468,
    "V16": -0.470,
    "V17": 0.207,
    "V18": 0.025,
    "V19": 0.403,
    "V20": 0.251,
    "V21": -0.018,
    "V22": 0.277,
    "V23": -0.110,
    "V24": 0.066,
    "V25": 0.128,
    "V26": -0.189,
    "V27": 0.133,
    "V28": -0.021,
    "Hour": 12.5
}
✅ Response Example (Fraud Prediction)
json
Copy
Edit
{
    "prediction": 0,
    "fraud_probability": 0.02
}
🔹 prediction: 0 → Safe Transaction
🔹 prediction: 1 → Fraud Detected! 🚨

📌 Future Improvements
✅ Enhance Model Performance – Try LSTM, Random Forest, or Neural Networks
✅ Add More Features – Use additional fraud indicators like location & device ID
✅ Improve UI – Display graphs & probability distributions in Streamlit

📌 Contributors
👨‍💻 Himanshu Dandle
📌 GitHub: himanshu-dandle
📌 LinkedIn: Himanshu Dandle

🔹 If you like this project, give it a ⭐ on GitHub! 🚀

