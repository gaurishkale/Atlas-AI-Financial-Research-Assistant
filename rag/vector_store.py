from langchain_chroma import Chroma


class AtlasVectorStore:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model

        self.persist_directory = "./database"

        self.vector_db = Chroma(
            collection_name="atlas_reports",
            embedding_function=self.embedding_model,
            persist_directory=self.persist_directory
        )

    def is_empty(self):

        return self.vector_db._collection.count() == 0

    def add_documents(self, documents):

        if self.is_empty():

            print("\nCreating embeddings...\n")

            self.vector_db.add_documents(documents)

        else:

            print("\nUsing existing vector database.\n")

    def similarity_search(self, query, k=5):

        return self.vector_db.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=20
        )