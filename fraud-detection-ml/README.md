# 🚀 Fraud Detection System using Machine Learning  

![GitHub repo size](https://img.shields.io/github/repo-size/himanshu-dandle/fraud-detection-ml?style=flat)  
![GitHub contributors](https://img.shields.io/github/contributors/himanshu-dandle/fraud-detection-ml?color=blue)  
![GitHub last commit](https://img.shields.io/github/last-commit/himanshu-dandle/fraud-detection-ml)  

🔗 **Live Web App:** 👉 [Click Here to Try!](https://fraud-detection-ml-pxygeugketyaekpkctz52d.streamlit.app/)


💻 **GitHub Repository:** 👉 [fraud-detection-ml](https://github.com/himanshu-dandle/fraud-detection-ml)  

---

## 📌 **Project Overview**  

🚨 **Fraudulent transactions cost billions every year.** This project builds an **AI-powered fraud detection system** that identifies fraudulent transactions in real-time using **Machine Learning (XGBoost, Scikit-Learn)** and is deployed with **FastAPI & Streamlit**.  

### ✅ **Key Features:**  
✔ **Real-Time Fraud Prediction** – Enter transaction data & get fraud probability instantly.  
✔ **Machine Learning Model** – Uses **XGBoost**, trained on an **imbalanced dataset**.  
✔ **FastAPI Backend** – Hosted on **Google Cloud Run** for live predictions.  
✔ **Streamlit Web UI** – User-friendly interface deployed on **Streamlit Cloud**.  

---

## 🏗 **Tech Stack Used**  

| Technology | Usage |
|------------|------------------|
| **Python** | Programming Language |
| **XGBoost, Scikit-Learn** | Machine Learning Model |
| **FastAPI, Uvicorn** | Backend API |
| **Streamlit** | Frontend Web App |
| **Google Cloud Run** | API Deployment |
| **Streamlit Cloud** | Web UI Deployment |
| **Pandas, NumPy** | Data Processing |
| **Matplotlib, Seaborn** | Data Visualization |

---

## 📂 **Project Structure**  

```
fraud-detection-ml/
│── data/                    # Raw and processed datasets (ignored in Git)
│── models/                  # Trained ML models (ignored in Git)
│── reports/                 # Reports, confusion matrices, AUC curves
│── scripts/                 # Helper scripts for training & deployment
│── fraud_detection.ipynb     # Jupyter Notebook for model training
│── app.py                    # FastAPI backend (Deployed on Google Cloud Run)
│── streamlit_app.py          # Streamlit frontend (Deployed on Streamlit Cloud)
│── Dockerfile                # Configuration for FastAPI deployment
│── requirements.txt          # Dependencies for FastAPI & Streamlit
│── .gitignore                # Excludes large files from GitHub
│── .gcloudignore             # Excludes unnecessary files for Google Cloud
└── README.md                 # Project documentation (this file)




🛠 How to Run the Project Locally
✅ 1. Clone the Repository

git clone https://github.com/himanshu-dandle/fraud-detection-ml.git
cd fraud-detection-ml
✅ 2. Install Dependencies
pip install -r requirements.txt
✅ 3. Run FastAPI Backend (Local Server)

uvicorn app:app --host 0.0.0.0 --port 8000 --reload
🔹 API will be available at http://localhost:8000/
🔹 Test it using Postman or cURL.

✅ 4. Run Streamlit Web UI (Local App)

streamlit run streamlit_app.py
🔹 This will open the web app at http://localhost:8501/
🔹 Users can input transaction data & check fraud probability!

🚀 How to Deploy (For Advanced Users)
✅ Deploy FastAPI Backend on Google Cloud Run

gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/fraud-api
gcloud run deploy fraud-api --image gcr.io/YOUR_PROJECT_ID/fraud-api --platform managed --region us-central1 --allow-unauthenticated
🔹 This will host the FastAPI backend online for public use.

✅ Deploy Streamlit Web App on Streamlit Cloud
1️⃣ Upload the project to GitHub
2️⃣ Go to Streamlit Cloud
3️⃣ Select your GitHub Repo
4️⃣ Set the Main File Path → streamlit_app.py
5️⃣ Click Deploy 🚀

🔹 After a few minutes, your public Streamlit App will be live!

🔌 API Usage (Example Request & Response)
✅ POST Request Example
📌 Send JSON data to FastAPI for fraud detection:

json


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
✅ Response Example
json


{
    "prediction": 0,
    "fraud_probability": 0.02
}
🔹 prediction: 0 → Safe Transaction
🔹 prediction: 1 → Fraud Detected! 🚨

🎯 Future Improvements
✅ Enhance Model Performance – Try LSTM, Random Forest, or Neural Networks
✅ Add More Features – Include location & device ID for fraud detection
✅ Improve UI – Add graphs & probability distributions in Streamlit

🤝 Contributors
👨‍💻 Himanshu Dandle
📌 GitHub: himanshu-dandle
📌 LinkedIn: Himanshu Dandle

🔹 If you like this project, give it a ⭐ on GitHub! 🚀

