from fastapi import FastAPI
from backend.routes import router

app = FastAPI(
    title="AtlasIQ API",
    version="1.0.0"
)

app.include_router(router)