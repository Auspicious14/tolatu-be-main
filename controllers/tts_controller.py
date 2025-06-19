# controllers/tts_controller.py
from fastapi.responses import FileResponse
from services.tts_service import TTSService

class TTSController:
    def __init__(self):
        self.tts_service = TTSService()
    
    async def synthesize(self, text: str, language: str = None):
        """Controller method to handle text-to-speech synthesis"""
        file_path = await self.tts_service.generate_speech(text, language)
        return FileResponse(
            path=file_path,
            media_type='audio/wav',
            filename=file_path.split('/')[-1] if '/' in file_path else file_path.split('\\')[-1]
        )
    
    async def get_models(self):
        """Controller method to get available TTS models"""
        return {"models": await self.tts_service.list_models()}
    
    async def get_models_by_language(self):
        """Controller method to get models grouped by language"""
        return {"models_by_language": await self.tts_service.get_models_by_language()}
    
    async def get_languages(self):
        """Controller method to get available languages"""
        return {"languages": await self.tts_service.get_available_languages()}