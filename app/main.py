from rag.pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    pipeline.ingest(
        "data/reports/tcs_annual_report.pdf"
    )

    answer, docs = pipeline.ask(
        "What are the company's revenue recognition policies?"
    )

    print("\n")
    print("=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(answer)

    print("\nSources")

    for doc in docs:

        print(f"Page {doc.metadata['page']}")


if __name__ == "__main__":
    main()