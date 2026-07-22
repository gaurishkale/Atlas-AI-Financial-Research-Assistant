from fastapi import APIRouter

from backend.schemas import (
    AskRequest,
    IngestRequest
)

from backend.services import AtlasService


router = APIRouter()


@router.get("/")
def home():

    return {
        "message": "Welcome to AtlasIQ 🚀"
    }


@router.post("/ingest")
def ingest(request: IngestRequest):

    return AtlasService.ingest(
        request.pdf_path
    )


@router.post("/ask")
def ask(request: AskRequest):

    return AtlasService.ask(
        request.question
    )