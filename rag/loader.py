from pathlib import Path
from typing import Dict

from pypdf import PdfReader


class PDFLoader:
    """
    Loads a PDF and extracts its text + metadata.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def load(self) -> Dict:

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"{self.pdf_path} does not exist.")

        reader = PdfReader(self.pdf_path)

        pages = []

        for index, page in enumerate(reader.pages):

            text = page.extract_text()

            if text:

                pages.append(
                    {
                        "page": index + 1,
                        "content": text
                    }
                )

        return {
            "file_name": self.pdf_path.name,
            "total_pages": len(reader.pages),
            "pages": pages
        }