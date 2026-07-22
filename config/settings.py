from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Gemini
    GOOGLE_API_KEY: str

    LLM_PROVIDER: str = "gemini"
    LLM_MODEL: str = "gemini-2.5-flash"

    EMBEDDING_PROVIDER: str = "gemini"
    EMBEDDING_MODEL: str = "models/gemini-embedding-2"

    # RAG
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    # ChromaDB
    COLLECTION_NAME: str = "atlas_reports"
    DATABASE_DIR: str = "./database"

    class Config:
        env_file = ".env"


settings = Settings()