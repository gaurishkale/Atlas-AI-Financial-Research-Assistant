from rag.loader import PDFLoader
from rag.chunker import TextChunker
from rag.embedder import AtlasEmbedding
from rag.vector_store import AtlasVectorStore
from rag.retriever import AtlasRetriever

from llm.chat import AtlasLLM
from prompts.rag_prompt import RAG_PROMPT


class RAGPipeline:

    def __init__(self):

        self.loader = None

        self.chunker = TextChunker()

        self.embedding = AtlasEmbedding()

        self.vector_store = AtlasVectorStore(
            self.embedding.get_model()
        )

        self.retriever = AtlasRetriever(
            self.vector_store
        )

        self.chat = AtlasLLM()

    def ingest(self, pdf_path: str):

        self.loader = PDFLoader(pdf_path)

        document = self.loader.load()

        chunks = self.chunker.split(
            document["pages"]
        )

        self.vector_store.add_documents(chunks)

        return len(chunks)

    def search(self, query: str, k: int = 5):

        return self.retriever.retrieve(
            question=query,
            k=k
        )

    def ask(self, question: str):

        docs = self.search(question)

        context = "\n\n".join(
            [
                f"Page {doc.metadata['page']}:\n{doc.page_content}"
                for doc in docs
            ]
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        answer = self.chat.ask(prompt)

        return answer, docs