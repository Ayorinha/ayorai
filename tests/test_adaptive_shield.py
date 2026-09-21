import hashlib

import pytest

from ayorai.shield.action_guard import AssetSensitivity, HighImpactActionGuard, ProtectedAction
from ayorai.shield.adaptive import AdaptiveDefense, ThreatObservation
from ayorai.shield.models import RiskLevel


def test_adaptive_learning_quarantines_untrusted_observations():
    defense = AdaptiveDefense()
    observation = ThreatObservation("feed", "new-tool-poisoning", "abc123", 0.80)
    candidate = defense.observe(observation, rule_id="THREAT-001", rationale="Observed in external feed")
    assert candidate.status == "quarantined"
    assert defense.active_rules() == ()


def test_adaptive_learning_requires_validation_before_promotion():
    defense = AdaptiveDefense()
    observation = ThreatObservation("feed", "known-pattern", hashlib.sha256(b"x").hexdigest(), 0.99)
    candidate = defense.observe(observation, rule_id="THREAT-002", rationale="Corroborated observation")
    active = defense.promote(candidate)
    assert active.status == "active"
    assert defense.active_rules()[0].rule_id == "THREAT-002"


def test_sensitive_action_requires_human_approval():
    guard = HighImpactActionGuard()
    action = ProtectedAction("transfer", "financial-record", AssetSensitivity.RESTRICTED, RiskLevel.HIGH)
    decision = guard.evaluate(action)
    assert decision.allowed is False
    assert decision.reason_code == "HIGH_IMPACT_APPROVAL_REQUIRED"


def test_approved_sensitive_action_is_allowed():
    guard = HighImpactActionGuard()
    action = ProtectedAction("transfer", "financial-record", AssetSensitivity.RESTRICTED, RiskLevel.HIGH)
    decision = guard.evaluate(action, human_approval=True)
    assert decision.allowed is True
