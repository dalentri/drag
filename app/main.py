from app.routers.query import router as query_router
from fastapi import FastAPI
from app.config import settings
import os

os.environ["OPENAI_API_KEY"] = settings.openai_api_key


app = FastAPI()
app.include_router(query_router)
