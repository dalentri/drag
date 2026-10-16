from app.models.schemas import Query
from app.services.rag import generate_answer
from fastapi import APIRouter

router = APIRouter()


@router.post("/api/v1/query")
def generate_response(query: Query):
    return generate_answer(query.prompt)
