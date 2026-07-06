from langchain_chroma import Chroma


class AtlasVectorStore:

    def __init__(self, embedding_model):

        self.vector_db = Chroma(
            collection_name="atlas_reports",
            embedding_function=embedding_model,
            persist_directory="./database"
        )

    def add_documents(self, documents):

        self.vector_db.add_documents(documents)

    def similarity_search(self, query, k=5):

        return self.vector_db.similarity_search(query, k=k)