# main.py
from fastapi import FastAPI, File, Form
from fastapi.responses import FileResponse
from TTS.api import TTS
import uuid
import os

app = FastAPI()

# Download a multi-speaker TTS model first
# e.g.: TTS --list_models
model_name = "tts_models/en/vctk/vits"

# Loading the TTS
tts = TTS(model_name)

@app.post("/synthesize/")
def synthesize(text: str = Form(...)):
    """Convert text to audio and return file path."""
    file_name = f"{uuid.uuid4()}.wav"
    file_path = os.path.join("/tmp", file_name)

    tts.tts_to_file(text=text, file_path=file_path, speaker="p225")

    return FileResponse(file_path, media_type='audio/wav', filename=file_name)
