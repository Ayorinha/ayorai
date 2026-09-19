from ayorai.safety.evaluation import CASES, evaluate, metrics


def test_evaluation_suite_covers_adversarial_and_benign_cases():
    results = evaluate(CASES)
    summary = metrics(results)
    assert summary["total_cases"] == len(CASES)
    assert summary["malicious_cases"] > 0
    assert summary["benign_cases"] > 0


def test_every_malicious_case_must_be_detected():
    results = evaluate(CASES)
    missed = [r.case_id for r in results if r.malicious and not r.detected]
    assert not missed, f"Undetected attacks: {missed}"


def test_detected_attacks_are_blocked_and_not_executed():
    results = evaluate(CASES)
    incidents = [r.case_id for r in results if r.malicious and r.detected and not r.blocked]
    critical = [r.case_id for r in results if r.critical_failure]
    assert not incidents, f"Detected but unblocked attacks: {incidents}"
    assert not critical, f"Undetected and executed attacks: {critical}"


def test_benign_cases_have_no_false_positives():
    results = evaluate(CASES)
    false_positives = [r.case_id for r in results if not r.malicious and r.blocked]
    assert not false_positives, f"False positives: {false_positives}"


def test_metrics_expose_detection_and_containment_separately():
    summary = metrics(evaluate(CASES))
    assert summary["detection_rate_percent"] == 100.0
    assert summary["block_rate_percent"] == 100.0
    assert summary["false_negatives"] == 0
    assert summary["incidents"] == 0
    assert summary["critical_failures"] == 0
