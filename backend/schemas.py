from pydantic import BaseModel


class IngestRequest(BaseModel):
    pdf_path: str


class AskRequest(BaseModel):
    question: str