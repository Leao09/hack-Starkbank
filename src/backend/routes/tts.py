from fastapi import APIRouter, Body
from gtts import gTTS
import uuid
import os


app = APIRouter()

@app.post("/tts/")
async def text_to_speech(text: str = Body(...), lang: str = Body(default="pt-br")):
    try:
        tts = gTTS(text=text, lang=lang)
        unique_file_name = f"speech_{uuid.uuid4()}.mp3"  # Gerar um nome de arquivo único
        file_path = f"../frontend/public/{unique_file_name}"
        tts.save(file_path)
        return {"audioUrl": f"/{unique_file_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/delete_audios")
async def delete_audios():
    try:
        directory = '../frontend/public/'
        files = os.listdir(directory)
        for file in files:
            if file.startswith("speech_") and file.endswith(".mp3"):
                os.remove(os.path.join(directory, file))
        return {"message": "Áudios excluídos com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))