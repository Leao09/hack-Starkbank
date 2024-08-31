from db import database, User
from pydantic import BaseModel
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from fastapi.responses import FileResponse
from gtts import gTTS
from dotenv import load_dotenv

from fastapi import APIRouter


load_dotenv()

app = APIRouter()

# Função auxiliar para comunicar com API do ChatGPT
async def connect_gpt(data: str):

    reader = PdfReader('./data/inventario_simulado.pdf')

    if reader is not None:
        raw_text = ''
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        chunks = text_splitter.split_text(raw_text)

        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        chain = load_qa_chain(OpenAI(), chain_type="stuff")
        query = f"Você deve funcionar como um assistente de almoxarifado. Toda vez for feita uma pergunta a respeito a disponibilidade, descrição ou quantidade de uma peça, deve ser respondido sem a localização. Me diga a localização da peça SOMENTE quando solicitarmos essa informação, e diga que está indo, no formato [x, y] obrigatoriamente. Perguntas que não são a respeito do almoxarifado não devem ser respondidas. Pergunta: {data}"
        docs = knowledge_base.similarity_search(query)
        response = chain.run(input_documents=docs, question=query)



    return response


# Estrutura de dados esperada pela rota de solitação do chatbot
class DataModel(BaseModel):
    dados: str

# Rota de solicitação a partir do chatbot
@app.post('/enviar_dados')
async def receber_dados(data: DataModel):
    resposta = await connect_gpt(data.dados)
    return resposta


