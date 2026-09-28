from ayorai.safety.risk import RiskEngine


def test_risk_engine_normalizes_whitespace_and_stays_low():
    assessment = RiskEngine().assess("  summarize\nthis document  ")
    assert assessment.level == "low"
    assert assessment.score == 0
    assert assessment.reasons == ()


def test_risk_engine_returns_medium_for_one_high_impact_term():
    assessment = RiskEngine().assess("send this report")
    assert assessment.level == "medium"
    assert assessment.score == 10
    assert assessment.reasons == ("high-impact:send",)


def test_risk_engine_returns_high_for_three_terms():
    assessment = RiskEngine().assess("delete and transfer then execute")
    assert assessment.level == "high"
    assert assessment.score == 30
    assert assessment.reasons == (
        "high-impact:delete",
        "high-impact:transfer",
        "high-impact:execute",
    )


def test_risk_engine_caps_score_at_100():
    text = " ".join(RiskEngine.HIGH_IMPACT_TERMS)
    assessment = RiskEngine().assess(text)
    assert assessment.level == "high"
    assert assessment.score == 100
    assert len(assessment.reasons) == len(RiskEngine.HIGH_IMPACT_TERMS)
