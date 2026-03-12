import statistics
from datetime import datetime
from tester.tests import (
    test_status_200,
    test_content_type_json,
    test_champ_base,
    test_champ_rates,
    test_champ_date,
    test_conversion_eur_usd,
    test_devise_invalide_404,
    test_endpoint_inconnu_404,
)

ALL_TESTS = [
    test_status_200,
    test_content_type_json,
    test_champ_base,
    test_champ_rates,
    test_champ_date,
    test_conversion_eur_usd,
    test_devise_invalide_404,
    test_endpoint_inconnu_404,
]


def run_tests():
    """
    Exécute tous les tests et retourne un dict structuré
    avec les résultats + métriques QoS.
    """
    results = []
    for test_fn in ALL_TESTS:
        try:
            result = test_fn()
        except Exception as e:
            result = {
                "name": test_fn.__name__,
                "status": "FAIL",
                "latency_ms": 0,
                "details": f"Exception : {str(e)}"
            }
        results.append(result)

    # ── Calcul des métriques ──────────────────
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed
    total = len(results)
    error_rate = round(failed / total, 3) if total > 0 else 0

    latencies = [r["latency_ms"] for r in results if r.get("latency_ms")]
    latency_avg = round(statistics.mean(latencies)) if latencies else 0
    latency_p95 = round(
        sorted(latencies)[int(len(latencies) * 0.95) - 1]
    ) if len(latencies) >= 2 else (latencies[0] if latencies else 0)

    availability = round((passed / total) * 100, 1) if total > 0 else 0

    return {
        "api": "Frankfurter",
        "timestamp": datetime.now().isoformat(),
        "passed": passed,
        "failed": failed,
        "error_rate": error_rate,
        "latency_ms_avg": latency_avg,
        "latency_ms_p95": latency_p95,
        "availability": availability,
        "tests": results
    }
