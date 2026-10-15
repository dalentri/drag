import pathlib as pl

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import VectorStoreIndex

from app.database import storage_context

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

doc_path = pl.Path("data/raw_docs/")

files = list(doc_path.glob("*.pdf")) + list(doc_path.glob("*.md"))
print(f"{len(files)} file(s) detected.")

docs = SimpleDirectoryReader(input_files=files).load_data()
print(f"loaded {len(docs)} files.")

pipeline = IngestionPipeline(
    transformations=[SentenceSplitter(chunk_size=512, chunk_overlap=50)]
)

nodes = pipeline.run(documents=docs)

index = VectorStoreIndex(nodes=nodes, storage_context=storage_context)

print(f"Successfully ingested and stored {len(nodes)} nodes into the database.")
