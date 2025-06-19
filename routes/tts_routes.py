# routes/tts_routes.py
from fastapi import APIRouter, Depends, Form, Query
from controllers.tts_controller import TTSController

router = APIRouter(tags=["TTS"])
tts_controller = TTSController()

@router.post("/synthesize/")
async def synthesize_text(text: str = Form(...), language: str = Form(None)):
    """Convert text to speech and return audio file
    
    - **text**: The text to convert to speech
    - **language**: Optional language code (e.g., 'en', 'fr', 'es')
    """
    return await tts_controller.synthesize(text, language)

@router.get("/models/")
async def get_available_models():
    """Get list of all available TTS models"""
    return await tts_controller.get_models()

@router.get("/models/by-language/")
async def get_models_by_language():
    """Get TTS models grouped by language"""
    return await tts_controller.get_models_by_language()

@router.get("/languages/")
async def get_available_languages():
    """Get list of available languages for TTS"""
    return await tts_controller.get_languages()