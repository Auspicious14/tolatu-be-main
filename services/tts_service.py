# services/tts_service.py
import os
import uuid
from TTS.api import TTS

class TTSService:
    def __init__(self):
        # Default model
        self.model_name = "tts_models/en/ljspeech/tacotron2-DDC"
        # Initialize TTS
        self.tts = TTS(self.model_name)
        # Create output directory if it doesn't exist
        self.output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def generate_speech(self, text: str) -> str:
        """Generate speech from text and return the file path"""
        # Generate unique filename
        file_name = f"{uuid.uuid4()}.wav"
        file_path = os.path.join(self.output_dir, file_name)
        
        # Generate speech
        self.tts.tts_to_file(text=text, file_path=file_path)
        
        return file_path
    
    async def list_models(self) -> list:
        """List available TTS models"""
        # This would typically call TTS.list_models() but we'll return a simplified list
        # In a real implementation, you might want to filter or format the models list
        return [
            "tts_models/en/ljspeech/tacotron2-DDC",
            "tts_models/en/ljspeech/glow-tts",
            "tts_models/en/ljspeech/speedy-speech",
            "tts_models/en/vctk/vits"
        ]
    
    async def change_model(self, model_name: str) -> bool:
        """Change the TTS model"""
        try:
            self.tts = TTS(model_name)
            self.model_name = model_name
            return True
        except Exception as e:
            print(f"Error changing model: {e}")
            return False