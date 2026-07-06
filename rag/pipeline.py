from rag.loader import PDFLoader
from rag.chunker import TextChunker
from rag.embedder import AtlasEmbedding
from rag.vector_store import AtlasVectorStore


class RAGPipeline:

    def __init__(self):

        self.loader = None
        self.chunker = TextChunker()

        self.embedding = AtlasEmbedding()

        self.vector_store = AtlasVectorStore(
            self.embedding.get_model()
        )

    def ingest(self, pdf_path: str):

        self.loader = PDFLoader(pdf_path)

        document = self.loader.load()

        chunks = self.chunker.split(
            document["pages"]
        )

        self.vector_store.add_documents(chunks)

        return len(chunks)

    def search(self, query: str, k: int = 5):

        return self.vector_store.similarity_search(
            query,
            k
        )