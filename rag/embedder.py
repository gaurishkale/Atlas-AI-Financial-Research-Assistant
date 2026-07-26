from langchain_huggingface import HuggingFaceEmbeddings

from config.settings import settings


class AtlasEmbedding:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    def get_model(self):

        return self.embedding