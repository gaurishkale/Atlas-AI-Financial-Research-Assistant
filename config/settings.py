from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Gemini
    GOOGLE_API_KEY: str

    LLM_PROVIDER: str = "gemini"
    LLM_MODEL: str = "gemini-3.6-flash"

    EMBEDDING_PROVIDER: str = "huggingface"
    EMBEDDING_MODEL: str = "BAAI/bge-base-en-v1.5"

    # RAG
    CHUNK_SIZE: int = 2500
    CHUNK_OVERLAP: int = 200                    

    # ChromaDB
    COLLECTION_NAME: str = "atlas_reports"
    DATABASE_DIR: str = "./database"

    class Config:
        env_file = ".env"


settings = Settings()

print("LLM Model:", settings.LLM_MODEL)
print("Embedding Model:", settings.EMBEDDING_MODEL)