from rag.pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    total_chunks = pipeline.ingest(
        "data/reports/tcs_annual_report.pdf"
    )

    print(f"\nChunks Created : {total_chunks}\n")

    results = pipeline.search(
        "What is the company's revenue?"
    )

    for index, result in enumerate(results):

        print("=" * 60)

        print(f"Result {index+1}")

        print(f"Page : {result.metadata['page']}")

        print()

        print(result.page_content[:500])


if __name__ == "__main__":
    main()