from twilio.rest import Client
from app.db.mongo_connection import get_candidate_collection
from app.services.gpt_service import get_gpt_reply
from app.services.file_service import upload_file_to_firebase
from app.templates import load_template
import os
from app.config import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to: str, body: str):
    message = client.messages.create(
        body=body,
        from_=settings.TWILIO_WHATSAPP_NUMBER,
        to=to
    )
    return message.sid

def handle_incoming_message(data):
    from_number = data.get("From")
    body = data.get("Body")
    if not from_number or not body:
        print("Missing 'From' or 'Body' in incoming data:", data)
        return
    print(f"Received from {from_number}: {body}")
    send_whatsapp_message(from_number, load_template("initial_message.txt").format(candidate_name="Candidate")) 