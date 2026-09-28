import hashlib

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


def test_adaptive_rejects_low_confidence_candidate():
    defense = AdaptiveDefense()
    observation = ThreatObservation("feed", "weak-signal", "hash", 0.50)
    candidate = defense.observe(observation, rule_id="THREAT-003", rationale="Insufficient evidence")
    rejected = defense.validate(candidate)
    assert rejected.status == "rejected"
    assert defense.candidates() == (candidate,)
    assert defense.active_rules() == ()


def test_adaptive_rejects_unknown_candidate():
    defense = AdaptiveDefense()
    observation = ThreatObservation("feed", "unknown", "hash", 0.99)
    candidate = ThreatObservation("other", "signal", "hash2", 0.99)
    rule = defense.observe(observation, rule_id="THREAT-004", rationale="Observed")
    unknown = type(rule)("THREAT-X", candidate, "not observed")
    try:
        defense.validate(unknown)
    except ValueError as exc:
        assert str(exc) == "Unknown threat candidate"
    else:
        raise AssertionError("unknown candidate should fail")


def test_adaptive_promotion_rejects_unvalidated_candidate():
    defense = AdaptiveDefense()
    observation = ThreatObservation("feed", "weak-signal", "hash", 0.50)
    candidate = defense.observe(observation, rule_id="THREAT-005", rationale="Insufficient evidence")
    try:
        defense.promote(candidate)
    except ValueError as exc:
        assert str(exc) == "Only validated rules can be promoted"
    else:
        raise AssertionError("rejected candidate should not be promoted")
