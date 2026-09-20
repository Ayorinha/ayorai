from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentChunk:
    content: str
    source: str


class Retriever(ABC):
    @abstractmethod
    def search(self, query: str, limit: int = 5) -> list[DocumentChunk]:
        raise NotImplementedError


class InMemoryRetriever(Retriever):
    def __init__(self, documents: list[DocumentChunk] | None = None) -> None:
        self.documents = documents or []

    def search(self, query: str, limit: int = 5) -> list[DocumentChunk]:
        if limit < 0:
            raise ValueError("limit must be non-negative")
        if not query.strip() or limit == 0:
            return []

        terms = set(query.lower().split())
        ranked = sorted(
            self.documents,
            key=lambda doc: len(terms.intersection(doc.content.lower().split())),
            reverse=True,
        )
        return ranked[:limit]
