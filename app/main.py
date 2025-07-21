from fastapi import FastAPI
from app.routes.whatsapp_routes import router

app = FastAPI(
    title="WhatsApp Chatbot",
    version="0.1.0"
)

app.include_router(router) 