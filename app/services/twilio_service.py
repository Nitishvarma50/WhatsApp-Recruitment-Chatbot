from twilio.rest import Client
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
    # Placeholder: parse message, call OpenAI, respond, etc.
    from_number = data.get("From")
    body = data.get("Body")
    # TODO: Call OpenAI GPT handler, store to Mongo, etc.
    print(f"Received from {from_number}: {body}")
    # Example: send auto-reply
    send_whatsapp_message(from_number, "Thanks for your message! (Bot reply)") 