from tester.tests import *
import time

def run_tests():

    tests = [
        ("status", test_status),
        ("json", test_json),
        ("base field", test_base_field),
        ("rates field", test_rates_field),
        ("date field", test_date_field),
        ("rates type", test_rates_type)
    ]

    results = []

    start = time.time()

    for name, func in tests:

        try:
            ok = func()
            status = "PASS" if ok else "FAIL"

        except:
            status = "ERROR"

        results.append({
            "name": name,
            "status": status
        })

    duration = (time.time() - start) * 1000

    passed = len([r for r in results if r["status"] == "PASS"])
    failed = len(results) - passed

    return {
        "summary": {
            "passed": passed,
            "failed": failed,
            "latency_ms_avg": duration / len(results),
            "error_rate": failed / len(results)
        },
        "tests": results
    }
