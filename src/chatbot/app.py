import os
import openai
import pickle
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
import chainlit as cl
import time

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Function to preprocess uploaded PDF
async def preprocess_pdf(pdf_content):
    with open("temp.pdf", "wb") as f:
        f.write(pdf_content)
    pdf_reader = PdfReader("temp.pdf")
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ''

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)
    return chunks

# Function to generate response based on the query
async def generate_response(query, VectorStore):
    start_time = time.time()  # Start timing

    docs = VectorStore.similarity_search(query=query, k=3)

    llm = ChatOpenAI(model_name='gpt-3.5-turbo')
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=query)
        # Print the callback information
        print(f"Número total de tokens utilizados: {cb.total_tokens}")
        print(f"Custo estimado: {cb.total_cost}")

    end_time = time.time()  # End timing
    print(f"Tempo total para processar a resposta: {end_time - start_time} seconds")

    return response

@cl.on_chat_start
async def on_chat_start():
    files = None
    # Wait for the user to upload a PDF file
    while files is None:
        files = await cl.AskFileMessage(
            content="Por favor, faça o upload do seu PDF!", accept=["application/pdf"]
        ).send()

    pdf_file = files[0]
    chunks = await preprocess_pdf(pdf_file.content)
    store_name = pdf_file.name.split('.')[0]
    cl.user_session.set("chunks", chunks)
    cl.user_session.set("store_name", store_name)

    await cl.Message(content=f"`{pdf_file.name}` carregado com sucesso. Agora você pode fazer perguntas!").send()

@cl.on_message
async def main(message):
    query = message.content
    chunks = cl.user_session.get("chunks")
    store_name = cl.user_session.get("store_name")

    if chunks and store_name:
        # Load or create VectorStore
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        response = await generate_response(query, VectorStore)
        response_message = cl.Message(content=response)
        await response_message.send()
    else:
        prompt_message = cl.Message(content="Por favor, faça o upload do seu PDF!")
        await prompt_message.send()

if __name__ == '__main__':
    cl.run()
