import os
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.core.indices import vector_store
from llama_index.vector_stores.postgres import PGVectorStore
import psycopg2
from app.config import settings

connection_string = settings.database_url

_storage_context = None


def get_storage_context():
    global _storage_context

    if _storage_context is None:
        vector_store = PGVectorStore.from_params(
            database=settings.database_name,
            host=settings.host,
            password=settings.password,
            port=settings.port,
            user=settings.username,
            table_name=settings.table_name,
            embed_dim=settings.embed_dim,
        )

        _storage_context = StorageContext.from_defaults(vector_store=vector_store)

    return _storage_context
