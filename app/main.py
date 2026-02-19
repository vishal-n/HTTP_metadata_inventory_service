from fastapi import FastAPI
from app.api.metadata_routes import router

app = FastAPI()

app.include_router(router)
