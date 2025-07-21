
from app.db.mongo_connection import get_candidate_collection
from datetime import datetime

def find_or_create_candidate(phone_number: str):
    """
    Finds a candidate by phone number or creates a new one if not found.
    Initializes with 'new' state.
    """
    candidates_collection = get_candidate_collection()
    candidate = candidates_collection.find_one_and_update(
        {"phone": phone_number},
        {"$setOnInsert": {
            "phone": phone_number,
            "state": "new",
            "cv_url": None,
            "voice_note_url": None,
            "created_at": datetime.utcnow()
        }},
        upsert=True,
        return_document=True
    )
    return candidate

def update_candidate_state(phone_number: str, new_state: str):
    """Updates the conversation state for a candidate."""
    candidates_collection = get_candidate_collection()
    candidates_collection.update_one(
        {"phone": phone_number},
        {"$set": {"state": new_state, "updated_at": datetime.utcnow()}}
    )

def update_candidate_cv(phone_number: str, cv_url: str):
    """Updates the CV URL for a candidate."""
    candidates_collection = get_candidate_collection()
    candidates_collection.update_one(
        {"phone": phone_number},
        {"$set": {"cv_url": cv_url, "updated_at": datetime.utcnow()}}
    )

def is_cv_aligned(cv_url: str) -> bool:
    """
    Placeholder function to check if the CV is aligned with job requirements.
    For now, this will always return True.
    In a real application, this would involve parsing the CV and matching keywords.
    """
    print(f"Analyzing CV at {cv_url}...")
    # TODO: Implement actual CV analysis logic (e.g., using an NLP model or keyword matching)
    return True 