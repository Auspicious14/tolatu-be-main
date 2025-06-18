# routes/tts_routes.py
from fastapi import APIRouter, Depends, Form
from controllers.tts_controller import TTSController

router = APIRouter(tags=["TTS"])
tts_controller = TTSController()

@router.post("/synthesize/")
async def synthesize_text(text: str = Form(...)):
    """Convert text to speech and return audio file"""
    return await tts_controller.synthesize(text)

@router.get("/models/")
async def get_available_models():
    """Get list of available TTS models"""
    return await tts_controller.get_models()