import time
from dataclasses import replace

import pytest

from ayorai.safety.asae import ASAEVerifier, Capability, derive_provenance_hash


@pytest.fixture
def verifier():
    return ASAEVerifier(b"a" * 32)


def capability(**overrides):
    values = {
        "issuer": "shield-policy",
        "subject": "agent-research",
        "name": "document.write",
        "resource_scope": "document://safe",
        "max_impact": "write",
        "expires_at": int(time.time()) + 300,
        "session_epoch": "epoch-1",
    }
    values.update(overrides)
    return Capability(**values)


def issue(verifier, **capability_overrides):
    return verifier.issue(
        capability(**capability_overrides),
        operation="write",
        bounded_arguments={"mode": "staged"},
        provenance_hash=derive_provenance_hash("trusted test document"),
        policy_version="policy-1",
    )


def test_valid_envelope_is_accepted_once(verifier):
    envelope = issue(verifier)
    assert verifier.verify(
        envelope,
        expected_subject="agent-research",
        required_impact="write",
        resource="document://safe/report",
        session_epoch="epoch-1",
        policy_version="policy-1",
    )
    assert not verifier.verify(
        envelope,
        expected_subject="agent-research",
        required_impact="write",
        resource="document://safe/report",
        session_epoch="epoch-1",
        policy_version="policy-1",
    )


def test_tampered_arguments_fail_signature(verifier):
    envelope = issue(verifier)
    tampered = replace(envelope, bounded_arguments={"mode": "unsafe"})
    assert not verifier.verify(
        tampered,
        expected_subject="agent-research",
        required_impact="write",
        resource="document://safe/report",
        session_epoch="epoch-1",
        policy_version="policy-1",
    )


def test_wrong_subject_scope_epoch_or_policy_fails(verifier):
    envelope = issue(verifier)
    assert not verifier.verify(
        envelope,
        expected_subject="agent-other",
        required_impact="write",
        resource="document://safe/report",
        session_epoch="epoch-1",
        policy_version="policy-1",
    )

    envelope = issue(verifier)
    assert not verifier.verify(
        envelope,
        expected_subject="agent-research",
        required_impact="write",
        resource="document://other/report",
        session_epoch="epoch-1",
        policy_version="policy-1",
    )

    envelope = issue(verifier)
    assert not verifier.verify(
        envelope,
        expected_subject="agent-research",
        required_impact="write",
        resource="document://safe/report",
        session_epoch="epoch-2",
        policy_version="policy-1",
    )

    envelope = issue(verifier)
    assert not verifier.verify(
        envelope,
        expected_subject="agent-research",
        required_impact="write",
        resource="document://safe/report",
        session_epoch="epoch-1",
        policy_version="policy-2",
    )


def test_expired_capability_is_rejected():
    clock = lambda: 1000
    verifier = ASAEVerifier(b"b" * 32, clock=clock)
    envelope = verifier.issue(
        capability(expires_at=1005),
        operation="write",
        bounded_arguments={},
        provenance_hash="h",
        policy_version="p",
    )
    assert verifier.verify(
        envelope,
        expected_subject="agent-research",
        required_impact="write",
        resource="document://safe/report",
        session_epoch="epoch-1",
        policy_version="p",
        now=1005,
    ) is False


def test_high_impact_requires_high_capability(verifier):
    envelope = issue(verifier, max_impact="write")
    assert not verifier.verify(
        envelope,
        expected_subject="agent-research",
        required_impact="high",
        resource="document://safe/report",
        session_epoch="epoch-1",
        policy_version="policy-1",
    )
