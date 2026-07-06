from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split(self, pages):

        chunks = []

        for page in pages:

            page_chunks = self.splitter.split_text(
                page["content"]
            )

            for chunk in page_chunks:

                chunks.append(
                    Document(
                        page_content=chunk,
                        metadata={
                            "page": page["page"]
                        }
                    )
                )

        return chunks