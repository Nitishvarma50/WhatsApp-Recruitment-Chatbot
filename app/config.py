import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MONGODB_URI = os.getenv("MONGODB_URI")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "chatbotdb")
    FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")


settings = Settings() 
print("TWILIO_ACCOUNT_SID:", Settings.TWILIO_ACCOUNT_SID)
print("TWILIO_AUTH_TOKEN:", Settings.TWILIO_AUTH_TOKEN)