import pathlib as pl

from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter

doc_path = pl.Path("../../data/raw_docs/")

files = list(doc_path.glob("*.pdf")) + list(doc_path.glob("*.md"))
print(f"{len(files)} detected.")

docs = SimpleDirectoryReader(input_files=files).load_data()
print(f"loaded {len(docs)} files.")

pipeline = IngestionPipeline(
    transformations=[SentenceSplitter(chunk_size=512, chunk_overlap=50)]
)

nodes = pipeline.run(documents=docs)
