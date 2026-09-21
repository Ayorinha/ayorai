from dataclasses import dataclass, field
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any

@dataclass(frozen=True)
class AuditEvent:
    event_type: str
    actor: str
    action: str
    allowed: bool
    metadata: dict[str, Any] = field(default_factory=dict)
    timestamp: str = ""
    previous_hash: str = ""
    event_hash: str = ""

    def __post_init__(self) -> None:
        if not self.timestamp:
            object.__setattr__(self, "timestamp", datetime.now(timezone.utc).isoformat())
        if not self.event_hash:
            payload = "|".join([
                self.event_type, self.actor, self.action, str(self.allowed),
                self.timestamp, self.previous_hash, repr(sorted(self.metadata.items()))
            ])
            object.__setattr__(self, "event_hash", sha256(payload.encode("utf-8")).hexdigest())

class AuditLog:
    """In-memory tamper-evident event chain for research and tests."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def record(self, event: AuditEvent) -> None:
        previous = self._events[-1].event_hash if self._events else ""
        if event.previous_hash != previous:
            event = AuditEvent(
                event.event_type, event.actor, event.action, event.allowed,
                event.metadata, event.timestamp, previous
            )
        self._events.append(event)

    def events(self) -> tuple[AuditEvent, ...]:
        return tuple(self._events)

    def verify(self) -> bool:
        previous = ""
        for event in self._events:
            if event.previous_hash != previous:
                return False
            previous = event.event_hash
        return True
