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
        terms = set(query.lower().split())
        ranked = sorted(
            self.documents,
            key=lambda doc: len(terms.intersection(doc.content.lower().split())),
            reverse=True,
        )
        return ranked[:limit]
