import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field("postgresql://postgres:0912@localhost:5432/projeto_naviguide")


settings = Settings()