import os
import pytest


@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    """Set dummy environment variables for all tests to prevent Pydantic validation errors."""
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    monkeypatch.setenv("DATABASE_NAME", "test_db")
    monkeypatch.setenv("HOST", "localhost")
    monkeypatch.setenv("PASSWORD", "fake-password")
    monkeypatch.setenv("PORT", "5432")
    monkeypatch.setenv("USERNAME", "fake-user")
    monkeypatch.setenv("TABLE_NAME", "test_table")
    monkeypatch.setenv("EMBED_DIM", "1536")
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("MODEL", "gpt-4o")
    monkeypatch.setenv("OPENAI_API_KEY", "fake-openai-key")
    monkeypatch.setenv("LLM_URL", "http://localhost:8000")
    monkeypatch.setenv("API_KEY", "fake-api-key")
