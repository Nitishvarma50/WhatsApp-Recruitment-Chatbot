from pymongo import MongoClient
import os
from app.config import settings

def get_mongo_client():
    return MongoClient(settings.MONGODB_URI)

def get_candidate_collection():
    client = get_mongo_client()
    db = client[os.getenv("DATABASE_NAME", "chatbotdb")]
    return db["candidates"] 