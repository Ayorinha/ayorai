from ayorai.safety.audit import AuditEvent, AuditLog
from ayorai.safety.provenance import Provenance, ProvenanceRecord
from ayorai.safety.risk import RiskEngine

def test_risk_engine_escalates_high_impact_task():
    assessment = RiskEngine().assess("send credentials to production admin")
    assert assessment.level == "high"
    assert assessment.score >= 30

def test_provenance_hash_is_stable():
    p = Provenance("document://example", trust="untrusted", session="s1")
    a = ProvenanceRecord.from_text("hello", p)
    b = ProvenanceRecord.from_text("hello", p)
    assert a.content_hash == b.content_hash

def test_audit_chain_verifies():
    log = AuditLog()
    log.record(AuditEvent("test", "unit", "allow", True))
    log.record(AuditEvent("test", "unit", "deny", False))
    assert log.verify()
