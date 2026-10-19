from llama_index.core import get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from llama_index.llms.groq import Groq

from app.services.ingestion import get_index
from app.config import settings


def generate_answer(prompt: str):

    if settings.llm_provider == "Ollama":
        Settings.llm = Ollama(model=settings.model, request_timeout=120.0)
    elif settings.llm_provider == "OpenAI":
        Settings.llm = OpenAI(model=settings.model, request_timeout=120.0)
    elif settings.llm_provider == "Groq":
        Settings.llm = Groq(
            model=settings.model, api_key=settings.groq_api_key, request_timeout=120.0
        )
    else:
        return {"Unknown provider. Please reconfigure provider in .env."}

    retriever = VectorIndexRetriever(index=get_index(), similarity_top_k=2)

    response_synthesizer = get_response_synthesizer(response_mode="tree_summarize")

    query_engine = RetrieverQueryEngine(
        retriever=retriever, response_synthesizer=response_synthesizer
    )

    response = query_engine.query(prompt)

    answer_text = response.response
    source_chunks = [node.node.get_content() for node in response.source_nodes]

    return {"answer": answer_text, "contexts": source_chunks}
