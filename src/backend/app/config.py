import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field("postgresql://postgres:postgres@database-naviguide.cbpcvwneun7e.us-east-1.rds.amazonaws.com:5432")


settings = Settings()