

from pydantic import BaseSettings, Field

from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
class Settings(BaseSettings):
    db_url: str = Field(...,env="DATABASE_URL")


settings = Settings()