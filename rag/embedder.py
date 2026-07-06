from langchain_ollama import OllamaEmbeddings


class AtlasEmbedding:

    def __init__(self):

        self.embedding_model = OllamaEmbeddings(
            model="nomic-embed-text"
        )

    def get_model(self):
        return self.embedding_model