from flask import Flask, request
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os
from dotenv import load_dotenv
import socketio

load_dotenv()

SERVER_URL = "http://localhost:3000"

sio = socketio.Client()

sio.connect(SERVER_URL)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo ao Flask!'

def connect_gpt(data):
    chat_model = ChatOpenAI()

    messages = [
        SystemMessage(content=os.getenv('COMPORTAMENTO')),
        HumanMessage(content=data),
    ]
        
    response = chat_model(messages)

    sio.emit('enqueue', response.content)

    return response.content


@app.route('/enviar_dados', methods=['POST'])
def receber_dados():
    dados = request.json  

    resposta = connect_gpt(dados['dados'])

    return resposta



if __name__ == '__main__':
    app.run(debug=True)