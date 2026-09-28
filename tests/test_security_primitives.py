from ayorai.safety.provenance import Provenance, ProvenanceRecord
from ayorai.safety.risk import RiskEngine


def test_risk_engine_escalates_high_impact_task():
    assessment = RiskEngine().assess("send credentials to production admin")
    assert assessment.level == "high"
    assert assessment.score >= 30


def test_provenance_hash_is_stable():
    provenance = Provenance("document://example", trust="untrusted", session="s1")
    first = ProvenanceRecord.from_text("hello", provenance)
    second = ProvenanceRecord.from_text("hello", provenance)
    assert first.content_hash == second.content_hash
