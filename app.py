# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.tts_routes import router as tts_router

app = FastAPI(title="TTS API", description="Text-to-Speech API using Coqui TTS")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(tts_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8020, reload=True)