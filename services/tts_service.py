# services/tts_service.py
import os
import uuid
import re
from TTS.api import TTS

class TTSService:
    def __init__(self):
        self.model_name = "tts_models/en/vctk/vits"
        self.language = "en"

        self.tts = TTS(self.model_name)

        self.output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def generate_speech(self, text: str, language: str = None) -> str:
        """Generate speech from text and return the file path"""
        # If language is specified and different from current, change the model
        if language and language != self.language:
            # Get the first model for the requested language
            models_by_lang = await self.get_models_by_language()
            if language in models_by_lang and models_by_lang[language]:
                await self.change_model(models_by_lang[language][0])

        file_name = f"{uuid.uuid4()}.wav"
        file_path = os.path.join(self.output_dir, file_name)
        
        self.tts.tts_to_file(text=text, file_path=file_path, speaker="p225")
        
        return file_path
    
    async def list_models(self) -> list:
        """List all available TTS models"""
        return TTS.list_models()
    
    async def get_models_by_language(self) -> dict:
        """Group models by language"""
        models = await self.list_models()
        models_by_lang = {}
        
        for model in models:
            # Extract language code from model name
            # Format is typically: tts_models/LANG/dataset/model_type
            match = re.match(r'tts_models/([^/]+)/', model)
            if match:
                lang_code = match.group(1)
                if lang_code not in models_by_lang:
                    models_by_lang[lang_code] = []
                models_by_lang[lang_code].append(model)
        
        return models_by_lang
    
    async def get_available_languages(self) -> list:
        """Get list of available languages"""
        models_by_lang = await self.get_models_by_language()
        languages = list(models_by_lang.keys())
        
        # Map language codes to more readable names
        language_names = {
            'en': 'English',
            'fr': 'French',
            'de': 'German',
            'es': 'Spanish',
            'it': 'Italian',
            'nl': 'Dutch',
            'pt': 'Portuguese',
            'pl': 'Polish',
            'tr': 'Turkish',
            'ru': 'Russian',
            'ja': 'Japanese',
            'zh': 'Chinese',
            'multi': 'Multilingual'
        }
        
        # Return a list of dictionaries with code and name
        return [
            {"code": code, "name": language_names.get(code, code)}
            for code in languages
        ]
    
    async def change_model(self, model_name: str) -> bool:
        """Change the TTS model"""
        try:
            self.tts = TTS(model_name)
            self.model_name = model_name
            
            # Update the current language
            match = re.match(r'tts_models/([^/]+)/', model_name)
            if match:
                self.language = match.group(1)
                
            return True
        except Exception as e:
            print(f"Error changing model: {e}")
            return False