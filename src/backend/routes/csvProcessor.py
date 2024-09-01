from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import databases
import ormar
from pydantic import BaseSettings, Field
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carregando variáveis de ambiente
load_dotenv()

# Configurações e conexão com o banco de dados
class Settings(BaseSettings):
    db_url: str = Field(..., env="DATABASE_URL")

settings = Settings()
database = databases.Database(settings.db_url)
metadata = MetaData()
engine = create_engine(settings.db_url)

# Definindo o modelo base do ormar
class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

# Criando o roteador da API
app = APIRouter()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        logger.info("Iniciando o processamento do arquivo CSV")
        
        # Lê o arquivo CSV
        df = pd.read_csv(file.file, low_memory=False)  # Evita o DtypeWarning
        logger.info(f"Arquivo CSV lido com sucesso. Colunas: {list(df.columns)}")
        if 'id' in df.columns:
            df = df.drop(columns=['id'])
            logger.info("Coluna 'id' removida")
        # Conecta ao banco de dados
        async with database.transaction():
            for column in df.columns:
                # Nome da tabela baseado no nome da coluna
                table_name = column.replace(" ", "_").replace("-", "_")[:63]  # Ajuste o nome para o PostgreSQL
                logger.info(f"Criando tabela: {table_name}")

                # Define a estrutura da tabela
                table = Table(
                    table_name, metadata,
                    Column('id', Integer, primary_key=True),
                    Column(column, String)
                )

                # Cria a tabela no banco de dados
                metadata.create_all(engine, tables=[table])
                logger.info(f"Tabela {table_name} criada com sucesso")

                # Insere os dados na tabela
                # Convertendo a coluna para string para evitar problemas de tipos
                data = df[[column]].astype(str)  # Garante que todos os dados sejam tratados como string
                data.to_sql(table_name, con=engine, if_exists='append', index=False)
                logger.info(f"Dados inseridos na tabela {table_name}")

        logger.info("Processamento do arquivo CSV concluído com sucesso")
        return {"filename": file.filename, "status": "success"}
    
    except SQLAlchemyError as e:
        logger.error(f"Erro ao inserir dados no banco de dados: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao inserir dados no banco: {str(e)}")
    
    except Exception as e:
        logger.error(f"Erro ao processar o arquivo CSV: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo CSV: {str(e)}")
