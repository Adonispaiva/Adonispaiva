"""Configurações centrais da aplicação."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuração carregada via variáveis de ambiente."""

    app_name: str = Field(default="rag_inovexa", alias="APP_NAME")
    app_env: str = Field(default="development", alias="APP_ENV")
    app_debug: bool = Field(default=True, alias="APP_DEBUG")
    api_prefix: str = Field(default="/v1", alias="API_PREFIX")
    database_url: str = Field(
        default="sqlite+pysqlite:///./rag_inovexa.db", alias="DATABASE_URL"
    )
    vector_backend: str = Field(default="pgvector", alias="VECTOR_BACKEND")
    lexical_backend: str = Field(default="bm25", alias="LEXICAL_BACKEND")
    default_embedding_model: str = Field(
        default="text-embedding-3-large", alias="DEFAULT_EMBEDDING_MODEL"
    )
    default_rerank_strategy: str = Field(
        default="hybrid-weighted", alias="DEFAULT_RERANK_STRATEGY"
    )
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False, extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
