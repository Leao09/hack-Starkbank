from fastapi import FastAPI, Request, Body, HTTPException
from pydantic import BaseModel
import socketio
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from fastapi.responses import FileResponse
from gtts import gTTS
from dotenv import load_dotenv
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
import re

load_dotenv()

SERVER_URL = "http://localhost:5000"
sio = socketio.Client()
sio.connect(SERVER_URL)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

class DataModel(BaseModel):
    dados: str

@app.get('/')
def home():
    return 'Bem-vindo ao FastAPI!'

def connect_gpt(data: str):

    reader = PdfReader('./data/inventario_simulado_amoxarifado.pdf')
    
    if reader is not None:
        raw_text = ''
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text
        
        text_splitter = CharacterTextSplitter(        
            separator = "\n",
            chunk_size = 1000,
            chunk_overlap  = 200,
            length_function = len,
        )
        chunks = text_splitter.split_text(raw_text)
      
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        
        chain = load_qa_chain(OpenAI(), chain_type="stuff")
        query = f"Você deve funcionar como um assistente de almoxarifado. Toda vez for feita uma pergunta a respeito a disponibilidade ou quantidade de uma peça, deve ser respondido se está disponivel e onde essa peça está. A localização da peça SEMPRE deve aparecer nas responstas no formato [x, y] obrigatoriamente. Perguntas que não são a respeito do almoxarifado não devem ser respondidas. (NÃO SE ESQUEÇA, A LOCALIZAÇÃO DA PEÇA DEVE SER ENVIADA NO FORMATO [x, y]). Pergunta: {data}"
        docs = knowledge_base.similarity_search(query)
        response = chain.run(input_documents=docs, question=query)
    
    pattern = re.compile(r'\[x:(?P<x>-?\d+), y:(?P<y>-?\d+)\]')
    match = pattern.search(response)

    if match:
        x = int(match.group("x"))/100
        y = int(match.group("y"))/100
        coordinates = [x, y]

    sio.emit('enqueue', str(coordinates))

    return response

@app.post('/enviar_dados')
def receber_dados(data: DataModel):
    resposta = connect_gpt(data.dados)
    return resposta

@app.post("/tts/")
async def text_to_speech(text: str = Body(...), lang: str = Body(default="pt-br")):
    try:
        tts = gTTS(text=text, lang=lang)
        file_path = "../frontend/public/speech.mp3"
        tts.save(file_path)
        return FileResponse(file_path, media_type='audio/mp3', filename=file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
