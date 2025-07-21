# WhatsApp Chatbot

A modular FastAPI backend for WhatsApp chatbot using Twilio, OpenAI GPT-4, MongoDB Atlas, and Firebase Storage.

## Setup

1. Create and activate virtual environment:
    ```
    python -m venv chatenv
    chatenv\Scripts\activate
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Copy `.env.example` to `.env` and fill in your credentials.

4. Run the server:
    ```
    uvicorn app.main:app --reload
    ```

## Folder Structure

See the codebase for details. 