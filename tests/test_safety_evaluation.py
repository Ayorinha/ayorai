from ayorai.safety.evaluation import CASES, evaluate, metrics

def test_evaluation_suite_covers_adversarial_and_benign_cases():
    results = evaluate(CASES)
    summary = metrics(results)
    assert summary["total_cases"] == len(CASES)
    assert summary["malicious_cases"] > 0
    assert summary["benign_cases"] > 0
    assert summary["false_negatives"] >= 0
    assert summary["false_positives"] >= 0

def test_current_guard_blocks_known_patterns():
    by_id = {result.case_id: result for result in evaluate(CASES)}
    assert by_id["PI-01"].outcome == "BLOCK"
    assert by_id["PI-02"].outcome == "BLOCK"
    assert by_id["PI-05"].outcome == "BLOCK"
    assert by_id["PI-06"].outcome == "BLOCK"

def test_suite_exposes_gaps_instead_of_claiming_perfect_detection():
    results = evaluate(CASES)
    summary = metrics(results)
    failures = [result for result in results if result.outcome == "FAIL"]
    assert summary["false_negatives"] == len(failures)
    assert all(result.malicious for result in failures)
