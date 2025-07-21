from twilio.rest import Client
from app.config import settings
from app.templates import load_template
from app.services.candidate_service import (
    find_or_create_candidate,
    update_candidate_state,
    update_candidate_cv,
    is_cv_aligned
)

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to: str, body: str):
    """Sends a WhatsApp message via Twilio."""
    try:
        message = client.messages.create(
            body=body,
            from_=settings.TWILIO_WHATSAPP_NUMBER,
            to=to
        )
        print(f"Message sent to {to}: SID {message.sid}")
        return message.sid
    except Exception as e:
        print(f"Error sending message to {to}: {e}")
        return None

def handle_incoming_message(data):
    """Main handler for all incoming Twilio messages."""
    from_number = data.get("From")
    if from_number is None:
        print("Webhook received without a 'From' number. Ignoring.")
        return

    candidate = find_or_create_candidate(from_number)
    num_media = int(data.get("NumMedia", 0))

    if num_media > 0:
        # This is a media message (assume it's a CV for now)
        cv_url = data.get("MediaUrl0")
        if cv_url:
            update_candidate_cv(from_number, cv_url)
            
            if is_cv_aligned(cv_url):
                # CV is aligned, ask for voice note
                reply_body = "Congratulations on your profile being shortlisted! Please send a 30-40 second voice note introducing yourself to proceed."
                send_whatsapp_message(to=from_number, body=reply_body)
                update_candidate_state(from_number, "awaiting_voice_note")
            else:
                # CV not aligned
                reply_body = load_template("not_interested.txt")
                send_whatsapp_message(to=from_number, body=reply_body)
                update_candidate_state(from_number, "cv_rejected")
    
    elif candidate.get("state") == "new":
        # This is the first text message from a new candidate
        reply_body = load_template("initial_message.txt").format(candidate_name="Candidate")
        send_whatsapp_message(to=from_number, body=reply_body)
        update_candidate_state(from_number, "awaiting_files")
    
    else:
        # Handle other text messages from existing candidates
        # TODO: Add logic for other states (awaiting_location, etc.)
        print(f"Received text from existing candidate {from_number} in state '{candidate.get('state')}'. No action defined yet.") 