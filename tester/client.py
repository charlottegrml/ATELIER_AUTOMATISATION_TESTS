import time
import requests

BASE_URL = "https://api.frankfurter.app"
TIMEOUT = 3  # secondes
MAX_RETRY = 1


def call_api(endpoint="/latest", params=None, expected_status=200):
    """
    Appelle l'API Frankfurter avec timeout, retry et mesure de latence.
    Retourne un dict : status, json, latency_ms, error
    """
    if params is None:
        params = {"from": "EUR"}

    url = BASE_URL + endpoint
    attempt = 0

    while attempt <= MAX_RETRY:
        try:
            start = time.time()
            response = requests.get(url, params=params, timeout=TIMEOUT)
            latency_ms = round((time.time() - start) * 1000)

            # Gestion rate limit 429 : on attend et on retente
            if response.status_code == 429 and attempt < MAX_RETRY:
                time.sleep(2)
                attempt += 1
                continue

            # Tentative de décodage JSON
            try:
                body = response.json()
            except Exception:
                body = {}

            return {
                "status": response.status_code,
                "json": body,
                "latency_ms": latency_ms,
                "error": None
            }

        except requests.exceptions.Timeout:
            if attempt < MAX_RETRY:
                attempt += 1
                continue
            return {
                "status": None,
                "json": {},
                "latency_ms": TIMEOUT * 1000,
                "error": "timeout"
            }

        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRY:
                attempt += 1
                continue
            return {
                "status": None,
                "json": {},
                "latency_ms": 0,
                "error": str(e)
            }

        attempt += 1

    return {
        "status": None,
        "json": {},
        "latency_ms": 0,
        "error": "max retries reached"
    }
