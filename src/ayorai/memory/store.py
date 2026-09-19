from abc import ABC, abstractmethod
from typing import Any


class MemoryStore(ABC):
    @abstractmethod
    def put(self, key: str, value: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Any:
        raise NotImplementedError

class InMemoryStore(MemoryStore):
    def __init__(self) -> None:
        self._data: dict[str, Any] = {}

    def put(self, key: str, value: Any) -> None:
        self._data[key] = value

    def get(self, key: str) -> Any:
        return self._data.get(key)
