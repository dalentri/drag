from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///:memory:"
    database_name: str = "test_db"
    host: str = "localhost"
    password: str = "test_password"
    port: str = "5432"
    username: str = "test_user"
    table_name: str = "test_table"
    embed_dim: int = 1536
    llm_provider: str = "openai"
    model: str = "gpt-4o"
    openai_api_key: str = "test-openai-key"
    llm_url: str = "http://localhost:8000"
    api_key: str = "test-api-key"
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
