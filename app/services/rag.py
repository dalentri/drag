from llama_index.core import get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine

from app.services.ingestion import index


def generate_answer(prompt: str):
    retriever = VectorIndexRetriever(index=index, similarity_top_k=2)

    response_synthesizer = get_response_synthesizer(response_mode="tree_summarize")

    query_engine = RetrieverQueryEngine(
        retriever=retriever, response_synthesizer=response_synthesizer
    )

    response = query_engine.query(prompt)

    answer_text = response.response
    source_chunks = [node.node.get_content() for node in response.source_nodes]

    return {"answer": answer_text, "contexts": source_chunks}
