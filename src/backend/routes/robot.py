from pydantic import BaseModel
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()

app = APIRouter()

# Função auxiliar para comunicar com API do ChatGPT
async def connect_gpt(data: str):
    # Texto estático de exemplo, substitua pelo conteúdo desejado
    raw_text = """
    Você está analisando os dados financeiros da TechSolutions Inc., uma empresa de tecnologia. A empresa está utilizando uma abordagem de mapeamento e redução para processar e extrair insights valiosos dos dados contábeis. O objetivo é entender melhor as receitas e despesas para otimizar operações e melhorar a lucratividade.
Primeiro, os dados brutos, incluindo receitas, despesas, salários e outras transações, são mapeados e categorizados por tipo, data e unidade de negócio. Em seguida, esses dados são agregados e reduzidos para identificar padrões e tendências. A análise deve se concentrar em três áreas principais:
Análise de Receita: Determine o total de receitas por unidade de negócio e por mês, identificando qualquer variação sazonal e padrões de crescimento ou declínio.
Análise de Despesas: Calcule o total de despesas por categoria e unidade de negócio, e compare com as receitas para calcular margens de lucro e identificar áreas de potencial economia.
Comparação de Despesas e Receitas: Avalie o custo de aquisição de clientes e o retorno sobre o investimento em marketing para identificar a eficácia das estratégias de marketing.
Utilize esses dados para gerar insights sobre:
Quais produtos ou serviços estão gerando mais receita e quais períodos apresentam maiores variações.
Áreas onde os custos podem ser reduzidos sem comprometer a qualidade.
Desempenho de diferentes unidades de negócio e oportunidades para melhorar a eficiência operacional.
Forneça recomendações específicas baseadas nesses insights para ajudar a TechSolutions Inc. a tomar decisões informadas e a alcançar suas metas de lucratividade.
    """

    # Divide o texto em chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(raw_text)

    # Criação dos embeddings e base de conhecimento
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # Carrega o modelo de QA
    chain = load_qa_chain(OpenAI(), chain_type="map_reduce")
    query = f"Você é um analista financeiro senior especializado em gerar relatório financeiros para e-comerce: {data}"
    docs = knowledge_base.similarity_search(query)
    response = chain.run(input_documents=docs, question=query)
    return response


# Estrutura de dados esperada pela rota de solicitação do chatbot
class DataModel(BaseModel):
    dados: str

# Rota de solicitação a partir do chatbot
@app.post('/enviar_dados')
async def receber_dados(data: DataModel):
    resposta = await connect_gpt(data.dados)
    return resposta
