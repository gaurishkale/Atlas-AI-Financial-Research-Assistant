import time

from google.api_core.exceptions import ResourceExhausted
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

        if not self.is_empty():
            print("\nUsing existing vector database.\n")
            return

        print("\nCreating embeddings...\n")

        BATCH_SIZE = 25

        total = len(documents)

        for start in range(0, total, BATCH_SIZE):

            end = min(start + BATCH_SIZE, total)

            batch = documents[start:end]

            print(
                f"Embedding batch {start//BATCH_SIZE + 1} "
                f"({start + 1}-{end} / {total})"
            )

            success = False

            while not success:

                try:
                    self.vector_db.add_documents(batch)
                    success = True

                except ResourceExhausted:

                    print("Rate limit reached. Waiting 60 seconds...")

                    time.sleep(60)

                except Exception as e:
                    print(e)
                    raise

            time.sleep(2)

        print("\nAll embeddings created successfully.\n")

    def similarity_search(self, query, k=5):

        return self.vector_db.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=20
        )