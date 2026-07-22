from rag.pipeline import RAGPipeline


pipeline = RAGPipeline()


class AtlasService:

    @staticmethod
    def ingest(pdf_path: str):

        total_chunks = pipeline.ingest(pdf_path)

        return {
            "chunks": total_chunks
        }

    @staticmethod
    def ask(question: str):

        answer, docs = pipeline.ask(question)

        return {
            "answer": answer,
            "sources": list(
                {
                    doc.metadata["page"]
                    for doc in docs
                }
            )
        }