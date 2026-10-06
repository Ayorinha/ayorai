from abc import ABC, abstractmethod
from typing import Any

from ayorai.shield.engine import ShieldEngine


class MemoryStore(ABC):
    @abstractmethod
    def put(self, key: str, value: Any, *, trusted: bool = False) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Any:
        raise NotImplementedError


class InMemoryStore(MemoryStore):
    def __init__(self, shield: ShieldEngine | None = None) -> None:
        self._data: dict[str, Any] = {}
        self._shield = shield

    def put(self, key: str, value: Any, *, trusted: bool = False) -> None:
        if self._shield is not None:
            decision = self._shield.inspect_memory_write(str(value), trusted=trusted)
            if not decision.allowed:
                raise PermissionError(decision.reason)
        self._data[key] = value

    def get(self, key: str) -> Any:
        return self._data.get(key)
