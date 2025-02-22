AI-Powered HR Chatbot with Slack Integration

🔗 Live Demo: 👉 HR Chatbot on Slack
💻 GitHub Repository: 👉 genai_chatbot

📌 Project Overview
🚀 An AI-powered HR chatbot that automates HR queries using GPT-4, Slack API, and Azure Cognitive Services. It provides instant answers to employee queries related to HR policies, reducing response time and improving efficiency.

✅ Key Features:
✔ Real-Time HR Assistance – Answers HR-related queries in Slack.
✔ GPT-4 Powered AI – Uses OpenAI for intelligent responses.
✔ Azure Cognitive Services – Extracts relevant info from HR documents.
✔ FastAPI Backend – Deployed on Render for scalability.
✔ Slack API Integration – Bot listens to @mentions and responds instantly.

🏗 Tech Stack Used
Technology	Usage
Python	Programming Language
FastAPI, Uvicorn	Backend API
OpenAI GPT-4	AI-Powered Responses
Slack API, Slack SDK	Slack Integration
Azure Cognitive Services	HR Policy Document Search
Render	API Deployment
📂 Project Structure
bash
Copy
Edit
gen_ai_chatbot/
│── hr_documents/            # HR policy documents (text & PDFs)
│── .env                     # API keys & environment variables (DO NOT COMMIT)
│── chatbot_api.py           # FastAPI backend
│── chatbot_ui.py            # Streamlit frontend (if required)
│── azure_text_analysis.py   # Azure Cognitive Services integration
│── read_documents.py        # HR document retrieval logic
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
🛠 How to Run the Project Locally
✅ 1. Clone the Repository

sh
Copy
Edit
git clone https://github.com/himanshu-dandle/genai_chatbot.git
cd genai_chatbot
✅ 2. Create a Virtual Environment

sh
Copy
Edit
python -m venv genai_hr_chatbot_env
source genai_hr_chatbot_env/bin/activate  # Mac/Linux
genai_hr_chatbot_env\Scripts\activate    # Windows
✅ 3. Install Dependencies

sh
Copy
Edit
pip install -r requirements.txt
✅ 4. Set Up Environment Variables

Create a .env file in the root directory and add the following:

ini
Copy
Edit
OPENAI_API_KEY="your-openai-api-key"
AZURE_TEXT_ANALYTICS_KEY="your-azure-key"
AZURE_TEXT_ANALYTICS_ENDPOINT="your-azure-endpoint"
SLACK_BOT_TOKEN="xoxb-your-slack-bot-token"
✅ 5. Run FastAPI Backend

sh
Copy
Edit
uvicorn chatbot_api:app --host 0.0.0.0 --port 8000 --reload
📍 The API will be available at:
🔹 http://127.0.0.1:8000
🔹 Swagger Docs: http://127.0.0.1:8000/docs

✅ 6. Run the Slack Bot Locally

sh
Copy
Edit
python chatbot_api.py
🔗 Slack Bot Setup
✅ 1. Create a Slack App

Visit Slack API Apps.
Click "Create New App" → Choose "From Scratch".
Enter an App Name (e.g., HR Chatbot) and select your workspace.
✅ 2. Configure OAuth & Permissions

Go to "OAuth & Permissions" and add the following Bot Token Scopes:

Scope	Description
app_mentions:read	Detect when bot is mentioned
calls:write	Start & manage calls
channels:read	Read public channels
chat:write	Send messages in Slack
commands	Add shortcuts/slash commands
groups:read	Read private channels bot has access to
im:history	Read direct messages bot has access to
im:read	View basic DM info
im:write	Start DMs with users
✅ 3. Install the App in Your Slack Workspace

Click "Install to Workspace".
Click Allow to grant permissions.
Copy the Bot User OAuth Token (xoxb-...) and add it to .env.
✅ 4. Enable Event Subscriptions

Go to "Event Subscriptions" → Toggle Enable Events: ON.
Set Request URL to:
bash
Copy
Edit
https://genai-chatbot-3uqj.onrender.com/slack/events
Click Verify → Ensure Verified status.
Subscribe to Bot Events:
app_mention
message.im
✅ 5. Invite Bot to a Slack Channel

Open Slack.
Go to a channel (e.g., #general).
Type:
bash
Copy
Edit
/invite @HR Chatbot
Test it by typing:
kotlin
Copy
Edit
@HR Chatbot What is the sick leave policy?
☁️ Deploy on Render
✅ 1. Deploy the Web Service

Go to Render.

Click "New Web Service" → Connect GitHub repository.

Set environment variables in Render Dashboard:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-api-key
AZURE_TEXT_ANALYTICS_KEY=your-azure-key
AZURE_TEXT_ANALYTICS_ENDPOINT=your-azure-endpoint
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
Set Start Command:

sh
Copy
Edit
uvicorn chatbot_api:app --host 0.0.0.0 --port $PORT
Click Deploy.

📍 Once deployed, the API will be accessible at:
🔗 https://genai-chatbot-3uqj.onrender.com

🔌 API Usage (Testing the Bot in Slack)
✅ Send a Test Message via cURL

sh
Copy
Edit
curl -k -X POST "https://slack.com/api/chat.postMessage" ^
-H "Authorization: Bearer xoxb-your-slack-token" ^
-H "Content-Type: application/json" ^
-d "{ \"channel\": \"YOUR_CHANNEL_ID\", \"text\": \"Hello from my bot!\" }"
✅ Expected Output:

json
Copy
Edit
{ "ok": true, "channel": "C08DVTGCQSH", "message": { "text": "Hello from my bot!" } }
📊 Troubleshooting
❌ Bot Not Responding in Slack?
✔ Ensure the bot is invited to the channel.
✔ Verify event subscriptions are configured correctly.
✔ Restart the bot by redeploying on Render.

❌ Slack Bot Token Not Working?
✔ Reinstall the Slack App and generate a new token.
✔ Ensure correct OAuth scopes are assigned.

📜 License
MIT License - Free to use and modify.

