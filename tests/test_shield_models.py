from ayorai.shield.models import RiskLevel, ShieldDecision


def test_risk_level_values_are_stable():
    assert RiskLevel.LOW.value == "low"
    assert RiskLevel.MEDIUM.value == "medium"
    assert RiskLevel.HIGH.value == "high"
    assert RiskLevel.CRITICAL.value == "critical"


def test_shield_decision_as_dict_serializes_security_fields():
    decision = ShieldDecision(
        allowed=False,
        risk=RiskLevel.HIGH,
        reason_code="TEST",
        reason="test decision",
        controls=("input-boundary", "policy-enforcement"),
        metadata={"source": "unit-test"},
    )

    payload = decision.as_dict()

    assert payload == {
        "allowed": False,
        "risk": "high",
        "reason_code": "TEST",
        "reason": "test decision",
        "controls": ["input-boundary", "policy-enforcement"],
        "metadata": {"source": "unit-test"},
    }
