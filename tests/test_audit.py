from ayorai.safety.audit import AuditEvent, AuditLog

def test_audit_log_records_security_decision():
    log = AuditLog()
    log.record(AuditEvent("policy", "system", "evaluate", True))
    assert len(log.events()) == 1
    assert log.events()[0].allowed is True
