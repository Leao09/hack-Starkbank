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
import re

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
        print(f"Total tokens used so far: {cb.total_tokens}")
        print(f"Estimated total cost so far: {cb.total_cost}")

    end_time = time.time()  # End timing
    print(f"Time taken for processing the response: {end_time - start_time} seconds")

    return response

@cl.on_chat_start
async def on_chat_start():
    files = None
    # Wait for the user to upload a PDF file
    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a PDF file to begin!", accept=["application/pdf"]
        ).send()

    pdf_file = files[0]
    chunks = await preprocess_pdf(pdf_file.content)
    store_name = pdf_file.name.split('.')[0]
    cl.user_session.set("chunks", chunks)
    cl.user_session.set("store_name", store_name)

    await cl.Message(content=f"`{pdf_file.name}` uploaded. You can now ask questions about your PDF.").send()

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

        formatted_query = query_formatting(query)
        print(formatted_query)

        response = await generate_response(query, VectorStore)
        response_message = cl.Message(content=response[1])
        await response_message.send()
    else:
        prompt_message = cl.Message(content="Please upload a PDF to start.")
        await prompt_message.send()

##Para a integração com o robô:
async def query_formatting(query):
    regex = r'.*?(ponto|prateleira|estante|local|peça|lugar|posi[çc][aã]o|[áa]rea|arm[áa]rio)?\s?([123])'
    match = re.search(regex, query, re.IGNORECASE)
    if match:
        ponto = match.group(2)
        formatted = f"Ponto {ponto}"
        return formatted
    else:
        return "Error"

if __name__ == '__main__':
    cl.run()
