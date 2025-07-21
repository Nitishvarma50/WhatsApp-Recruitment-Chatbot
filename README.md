# WhatsApp Recruitment Chatbot

A modular backend chatbot built with **FastAPI** that automates candidate engagement and screening over WhatsApp using the Twilio API, OpenAI GPT, MongoDB Atlas, and Firebase Storage.

## Features
- Receives and replies to WhatsApp messages via Twilio
- Sends structured, template-based messages to candidates
- Integrates with OpenAI GPT for dynamic replies
- Stores candidate data and status in MongoDB Atlas
- Handles CV and voice note uploads to Firebase Storage
- Scheduler for follow-up reminders

---

## Project Structure
```
Whatsapp_Chatbot/
├── app/
│   ├── main.py                   # FastAPI app entrypoint
│   ├── routes/                   # Webhook route for Twilio
│   ├── services/                 # WhatsApp, GPT, file, etc. services
│   ├── scheduler/                # Follow-up reminders
│   ├── db/                       # MongoDB connection
│   └── templates/                # Message templates
├── requirements.txt              # Python dependencies
├── .gitignore                    # Excludes secrets, env, venv, etc.
├── README.md                     # This file
```

---

## Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/Nitishvarma50/WhatsApp-Recruitment-Chatbot.git
cd WhatsApp-Recruitment-Chatbot
```

### 2. Set Up Python Environment
```sh
python -m venv chatenv
# On Windows:
chatenv\Scripts\activate
# On Mac/Linux:
source chatenv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with your credentials:
```
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+your_twilio_number
OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=your_mongodb_connection_uri
DATABASE_NAME=chatbotdb
FIREBASE_CREDENTIALS_PATH=path_to_your_firebase_credentials.json
```

### 5. Run the Server Locally
```sh
uvicorn app.main:app --reload
```
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API docs.

### 6. Test the Webhook Locally
Use curl or Postman to POST form data to `/webhook/twilio`:
```sh
curl -X POST http://127.0.0.1:8000/webhook/twilio -F 'From=whatsapp:+1234567890' -F 'Body=Hello'
```

---

## Deployment (Render Example)
1. Push your code to GitHub (no secrets in code).
2. Create a new Web Service on [Render](https://render.com/).
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
5. Add your environment variables in the Render dashboard.
6. Deploy and use the public URL as your Twilio webhook.

---

## Security
- **Never commit secrets** (API keys, tokens, .env, Firebase JSON) to git.
- Use `.gitignore` to exclude sensitive files.
- Set secrets in your deployment platform’s dashboard.

---

## License
MIT 