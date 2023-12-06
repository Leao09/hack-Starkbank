from fastapi import FastAPI, HTTPException, Body, UploadFile, File
from fastapi.responses import FileResponse
from gtts import gTTS
from fastapi.middleware.cors import CORSMiddleware
from speech_recognition import UnknownValueError, RequestError
import speech_recognition as sr
from io import BytesIO
import os

app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.post("/tts/")
async def text_to_speech(text: str = Body(...), lang: str = Body(default="pt-br")):
    try:
        tts = gTTS(text=text, lang=lang)
        file_path = "speech.mp3"
        tts.save(file_path)
        return FileResponse(file_path, media_type='audio/mp3', filename=file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class SpeechToTextNode:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_audio_to_text(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio_data, language='pt-br')
            return text

speech_to_text_node = SpeechToTextNode()

@app.post("/audio-to-text/")
async def audio_to_text(audio: UploadFile = File(...)):
    try:
        temp_file = f"temp_{audio.filename}"
        with open(temp_file, 'wb') as buffer:
            buffer.write(await audio.read())
        text = speech_to_text_node.convert_audio_to_text(temp_file)
        os.remove(temp_file)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
