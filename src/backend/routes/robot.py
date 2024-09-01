from pydantic import BaseModel
import pandas as pd
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

    df = pd.read_csv('../data/invoice.csv', low_memory=False)

    raw_text = df.astype(str).agg(' '.join, axis=1).str.cat(sep=' ')
    
    # Divide o texto em chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(raw_text)

    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    chain = load_qa_chain(OpenAI(), chain_type="finance")
    query = f"Você é um analista financeiro senior especializado em gerar relatório financeiros para e-comerce: {data}"
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


