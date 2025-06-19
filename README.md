# Text-to-Speech API with Coqui TTS

This is a FastAPI backend that uses Coqui TTS to convert text to speech in multiple languages.

## Features

- Convert text to speech using Coqui TTS
- Support for multiple languages
- RESTful API with FastAPI

## API Endpoints

### Text to Speech

```
POST /api/synthesize/
```

**Parameters:**

- `text` (required): The text to convert to speech
- `language` (optional): Language code (e.g., 'en', 'fr', 'es')

**Response:**

- Audio file (WAV format)

### Available Languages

```
GET /api/languages/
```

**Response:**

```json
{
  "languages": [
    {"code": "en", "name": "English"},
    {"code": "fr", "name": "French"},
    ...
  ]
}
```

### Available Models

```
GET /api/models/
```

**Response:**

```json
{
  "models": ["tts_models/en/ljspeech/tacotron2-DDC", ...]
}
```

### Models by Language

```
GET /api/models/by-language/
```

**Response:**

```json
{
  "models_by_language": {
    "en": ["tts_models/en/ljspeech/tacotron2-DDC", ...],
    "fr": [...],
    ...
  }
}
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   python app.py
   ```

## Usage Example

```python
import requests

# Convert text to speech in English (default)
response = requests.post(
    "http://localhost:8000/api/synthesize/",
    data={"text": "Hello, world!"}
)

# Save the audio file
with open("output.wav", "wb") as f:
    f.write(response.content)

# Convert text to speech in French
response = requests.post(
    "http://localhost:8000/api/synthesize/",
    data={"text": "Bonjour le monde!", "language": "fr"}
)

# Save the audio file
with open("output_fr.wav", "wb") as f:
    f.write(response.content)
```
