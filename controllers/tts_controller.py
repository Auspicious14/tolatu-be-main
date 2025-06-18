# controllers/tts_controller.py
from fastapi.responses import FileResponse
from services.tts_service import TTSService

class TTSController:
    def __init__(self):
        self.tts_service = TTSService()
    
    async def synthesize(self, text: str):
        """Controller method to handle text-to-speech synthesis"""
        file_path = await self.tts_service.generate_speech(text)
        return FileResponse(
            path=file_path,
            media_type='audio/wav',
            filename=file_path.split('/')[-1]
        )
    
    async def get_models(self):
        """Controller method to get available TTS models"""
        return {"models": await self.tts_service.list_models()}