from ayorai.rag.retriever import DocumentChunk, InMemoryRetriever


def test_retriever_returns_relevant_chunk():
    retriever = InMemoryRetriever([
        DocumentChunk("Python data engineering", "doc-a"),
        DocumentChunk("Cooking recipes", "doc-b"),
    ])
    results = retriever.search("Python engineering")
    assert results[0].source == "doc-a"
