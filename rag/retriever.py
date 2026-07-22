from rag.vector_store import AtlasVectorStore


class AtlasRetriever:

    def __init__(self, vector_store: AtlasVectorStore):
        self.vector_store = vector_store

    def retrieve(self, question: str, k: int = 5):

        return self.vector_store.similarity_search(
            query=question,
            k=k
        )
    