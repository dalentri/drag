from fastapi import FastAPI
from app.models.schemas import Query
from app.services.rag import generate_answer

app = FastAPI()


@app.post("/api/v1/query")
def generate_response(query: Query):
    return generate_answer(query.prompt)
