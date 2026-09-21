from dataclasses import dataclass
from hashlib import sha256

@dataclass(frozen=True)
class Provenance:
    source: str
    trust: str = "untrusted"
    session: str = "default"

@dataclass(frozen=True)
class ProvenanceRecord:
    provenance: Provenance
    content_hash: str

    @classmethod
    def from_text(cls, text: str, provenance: Provenance) -> "ProvenanceRecord":
        digest = sha256(text.encode("utf-8")).hexdigest()
        return cls(provenance, digest)
