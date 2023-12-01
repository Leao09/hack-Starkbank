import streamlit as st
import requests

def enviar_dados_para_servidor(dados):
    url = "http://127.0.0.1:5000/enviar_dados"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=dados, headers=headers)
    return response

# Configuração da interface gráfica
st.title("Interface do almoxarife")

# Entrada de dados do usuário
dados_usuario = st.text_input("Digite os dados:", "Onde posso encontrar um rolamento?")

# Botão para enviar os dados
if st.button("Enviar pergunta"):
    dados_json = {"dados": dados_usuario}
    resposta = enviar_dados_para_servidor(dados_json)

    # Exibir resposta do servidor
    st.write("Resposta do Servidor:")
    st.write(resposta.text)
