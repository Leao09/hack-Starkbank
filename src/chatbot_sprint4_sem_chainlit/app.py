from fastapi import FastAPI, HTTPException, Body, UploadFile, File
from fastapi.responses import FileResponse
from gtts import gTTS
from fastapi.middleware.cors import CORSMiddleware
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
