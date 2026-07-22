from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config.settings import settings


class AtlasEmbedding:
    def __init__(self):
        self.embedding = GoogleGenerativeAIEmbeddings(
            model=settings.EMBEDDING_MODEL,
            google_api_key=settings.GOOGLE_API_KEY,
        )

    def get_model(self):
        return self.embedding