import gradio as gr
from services.tts_service import TTSService
import asyncio

# Create a single instance of the TTS service to avoid reloading the model
print("Loading TTS Service...")
tts_service = TTSService()
print("TTS Service Loaded.")

# Define the function that Gradio will call
def synthesize(text, language):
    print(f"Received request to synthesize: {text} in language: {language}")
    # Gradio runs in a sync context, but our service method is async
    # We need to run the async function in a new event loop
    try:
        # Get the existing event loop or create a new one if none exists
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # If no event loop is running, create a new one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    file_path = loop.run_until_complete(tts_service.generate_speech(text, language))
    print(f"Generated audio file at: {file_path}")
    return file_path

# Get the list of available languages for the dropdown
# This also needs to be run in an event loop
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

available_languages = loop.run_until_complete(tts_service.get_available_languages())
language_choices = [(lang['name'], lang['code']) for lang in available_languages]

# Create the Gradio interface
iface = gr.Interface(
    fn=synthesize,
    inputs=[
        gr.Textbox(lines=3, label="Text to Synthesize"),
        gr.Dropdown(choices=language_choices, label="Language", value="en")
    ],
    outputs=gr.Audio(type="filepath", label="Generated Speech"),
    title="Coqui Text-to-Speech",
    description="Enter some text, select a language, and click 'Submit' to generate speech.",
    allow_flagging="never"
)

# Launch the interface
if __name__ == "__main__":
    print("Launching Gradio Interface...")
    iface.launch()
