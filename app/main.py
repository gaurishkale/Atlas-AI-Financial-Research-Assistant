from rag.loader import PDFLoader


def main():

    loader = PDFLoader("data/reports/tcs_annual_report.pdf")

    document = loader.load()

    print("=" * 60)
    print("AtlasIQ")
    print("=" * 60)

    print(f"File : {document['file_name']}")
    print(f"Pages: {document['total_pages']}")

    print()

    print(document["pages"][0]["content"][:2000])


if __name__ == "__main__":
    main()