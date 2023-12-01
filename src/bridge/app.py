from flask import Flask, request
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
import socketio
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

load_dotenv()

SERVER_URL = "http://localhost:3000"

sio = socketio.Client()

sio.connect(SERVER_URL)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo ao Flask!'

def connect_gpt(data):

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
        query = f"Você deve funcionar como um assistente de almoxarifado. Toda vez for feita uma pergunta a respeito a disponibilidade ou quantidade de uma peça, deve ser respondido se está disponivel e onde essa peça está. A localização da peça SEMPRE deve aparecer nas responstas no formato [x, y] obrigatoriamente. Perguntas que não são a respeito do almoxarifado não devem ser respondidas. Pergunta: {data}"
        docs = knowledge_base.similarity_search(query)
        response = chain.run(input_documents=docs, question=query)

    sio.emit('enqueue', response)

    return response


@app.route('/enviar_dados', methods=['POST'])
def receber_dados():
    dados = request.json  

    resposta = connect_gpt(dados['dados'])

    return resposta



if __name__ == '__main__':
    app.run(debug=True)