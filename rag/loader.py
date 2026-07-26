from pathlib import Path
from typing import Dict
import os

from pypdf import PdfReader


class PDFLoader:
    """
    Loads a PDF and extracts its text + metadata.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def load(self) -> Dict:

        print("\n" + "=" * 70)
        print("Current Working Directory :", os.getcwd())
        print("PDF Path Received         :", repr(str(self.pdf_path)))
        print("Absolute Path             :", self.pdf_path.resolve())
        print("File Exists               :", self.pdf_path.exists())
        print("=" * 70 + "\n")

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found!\n"
                f"Received Path : {self.pdf_path}\n"
                f"Absolute Path : {self.pdf_path.resolve()}"
            )

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

        print(f"Successfully loaded {len(reader.pages)} pages from '{self.pdf_path.name}'")

        return {
            "file_name": self.pdf_path.name,
            "total_pages": len(reader.pages),
            "pages": pages
        }