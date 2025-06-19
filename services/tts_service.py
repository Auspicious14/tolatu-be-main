# services/tts_service.py
import os
import uuid
from TTS.api import TTS

class TTSService:
    def __init__(self):
        self.model_name = "tts_models/en/ljspeech/tacotron2-DDC"

        self.tts = TTS(self.model_name).to('device')

        self.output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def generate_speech(self, text: str) -> str:
        """Generate speech from text and return the file path"""

        file_name = f"{uuid.uuid4()}.wav"
        file_path = os.path.join(self.output_dir, file_name)
        
        self.tts.tts_to_file(text=text, file_path=file_path)
        
        return file_path
    
    async def list_models(self) -> list:
        """List available TTS models"""
        models = TTS.list_models()
        print(models)
        return models
        # return [model for model in models if "tts_models/en" in model]
    
    async def change_model(self, model_name: str) -> bool:
        """Change the TTS model"""
        try:
            self.tts = TTS(model_name)
            self.model_name = model_name
            return True
        except Exception as e:
            print(f"Error changing model: {e}")
            return False