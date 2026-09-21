"""Experimental ASAE authorization channel for AYORAI Shield.

ASAE separates model intent from execution authority. This module is a
research implementation using standard-library HMAC-SHA256 primitives.
It is not a production credential system.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict, replace
from hashlib import sha256
import hmac
import json
import secrets
import time
from typing import Any, Callable


IMPACT_ORDER = {"read": 0, "write": 1, "external": 2, "high": 3}


@dataclass(frozen=True)
class Capability:
    issuer: str
    subject: str
    name: str
    resource_scope: str
    max_impact: str
    expires_at: int
    session_epoch: str
    parent_id: str = ""


@dataclass(frozen=True)
class AuthorizationEnvelope:
    protocol_version: str
    capability: Capability
    operation: str
    bounded_arguments: dict[str, Any]
    provenance_hash: str
    policy_version: str
    nonce: str
    transaction_id: str
    issued_at: int
    signature: str


class ASAEVerifier:
    """Verifies short-lived, scoped authorization envelopes.

    The model is never treated as an authority. A caller must possess the
    verifier-side secret and a valid capability to create an accepted envelope.
    """

    protocol_version = "0.1"

    def __init__(self, secret: bytes, *, clock: Callable[[], float] | None = None) -> None:
        if len(secret) < 32:
            raise ValueError("ASAE research keys must contain at least 32 bytes.")
        self._secret = secret
        self._clock = clock or time.time
        self._consumed_nonces: set[str] = set()

    @staticmethod
    def new_nonce() -> str:
        return secrets.token_urlsafe(24)

    @staticmethod
    def new_transaction_id() -> str:
        return secrets.token_urlsafe(18)

    def _payload(self, envelope: AuthorizationEnvelope) -> bytes:
        data = asdict(envelope)
        data.pop("signature", None)
        return json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def sign(self, envelope: AuthorizationEnvelope) -> str:
        return hmac.new(self._secret, self._payload(envelope), sha256).hexdigest()

    def issue(
        self,
        capability: Capability,
        *,
        operation: str,
        bounded_arguments: dict[str, Any],
        provenance_hash: str,
        policy_version: str,
        transaction_id: str | None = None,
    ) -> AuthorizationEnvelope:
        now = int(self._clock())
        if capability.expires_at <= now:
            raise ValueError("Cannot issue an expired capability.")
        envelope = AuthorizationEnvelope(
            protocol_version=self.protocol_version,
            capability=capability,
            operation=operation,
            bounded_arguments=dict(bounded_arguments),
            provenance_hash=provenance_hash,
            policy_version=policy_version,
            nonce=self.new_nonce(),
            transaction_id=transaction_id or self.new_transaction_id(),
            issued_at=now,
            signature="",
        )
        return replace(envelope, signature=self.sign(envelope))

    def verify(
        self,
        envelope: AuthorizationEnvelope,
        *,
        expected_subject: str,
        required_impact: str,
        resource: str,
        session_epoch: str,
        policy_version: str,
        now: int | None = None,
    ) -> bool:
        current = int(self._clock()) if now is None else now
        capability = envelope.capability

        if envelope.protocol_version != self.protocol_version:
            return False
        if not hmac.compare_digest(envelope.signature, self.sign(envelope)):
            return False
        if capability.subject != expected_subject:
            return False
        if capability.session_epoch != session_epoch:
            return False
        if capability.expires_at <= current:
            return False
        if envelope.policy_version != policy_version:
            return False
        if envelope.nonce in self._consumed_nonces:
            return False
        if IMPACT_ORDER.get(capability.max_impact, 99) < IMPACT_ORDER.get(required_impact, 99):
            return False
        if resource != capability.resource_scope and not resource.startswith(capability.resource_scope.rstrip("/") + "/"):
            return False

        self._consumed_nonces.add(envelope.nonce)
        return True

    def verify_signature_only(self, envelope: AuthorizationEnvelope) -> bool:
        """Validate authenticity without consuming the one-time authorization."""
        return hmac.compare_digest(envelope.signature, self.sign(envelope))


def derive_provenance_hash(content: str) -> str:
    """Create the content commitment used by the experimental protocol."""
    return sha256(content.encode("utf-8")).hexdigest()
