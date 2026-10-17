from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    database_name: str
    host: str
    password: str
    port: str
    username: str
    table_name: str
    embed_dim: int
    llm_provider: str
    model: str
    openai_api_key: str
    llm_url: str
    api_key: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
