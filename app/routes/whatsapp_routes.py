from fastapi import APIRouter, Request, BackgroundTasks, status
from fastapi.responses import JSONResponse
from app.services.message_service import handle_incoming_message

router = APIRouter()
 
@router.post("/webhook/twilio", status_code=status.HTTP_200_OK)
async def twilio_webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.form()
    background_tasks.add_task(handle_incoming_message, data)
    return JSONResponse(content={"status": "received"}) 