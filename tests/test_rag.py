import pytest

from ayorai.rag.retriever import DocumentChunk, InMemoryRetriever


def test_retriever_returns_relevant_chunk():
    retriever = InMemoryRetriever(
        [
            DocumentChunk("Python data engineering", "doc-a"),
            DocumentChunk("Cooking recipes", "doc-b"),
        ]
    )
    results = retriever.search("Python engineering")
    assert results[0].source == "doc-a"


def test_retriever_respects_zero_limit():
    retriever = InMemoryRetriever([DocumentChunk("Python", "doc-a")])
    assert retriever.search("Python", limit=0) == []


def test_retriever_rejects_negative_limit():
    retriever = InMemoryRetriever([DocumentChunk("Python", "doc-a")])
    with pytest.raises(ValueError, match="non-negative"):
        retriever.search("Python", limit=-1)


def test_retriever_returns_empty_for_blank_query():
    retriever = InMemoryRetriever([DocumentChunk("Python", "doc-a")])
    assert retriever.search("   ") == []


def test_retriever_keeps_deterministic_order_for_ties():
    retriever = InMemoryRetriever(
        [
            DocumentChunk("Python engineering", "doc-a"),
            DocumentChunk("Python engineering", "doc-b"),
        ]
    )
    assert [item.source for item in retriever.search("Python")] == ["doc-a", "doc-b"]
