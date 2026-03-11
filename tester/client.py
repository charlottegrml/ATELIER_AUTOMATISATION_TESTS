import requests
import time

URL = "https://api.frankfurter.app/latest?from=EUR"

def call_api():

    retries = 1

    for i in range(retries + 1):

        try:
            start = time.time()

            r = requests.get(URL, timeout=3)

            latency = (time.time() - start) * 1000

            return {
                "status": r.status_code,
                "latency": latency,
                "json": r.json()
            }

        except requests.exceptions.Timeout:

            if i < retries:
                continue

            return {
                "status": "timeout",
                "latency": None,
                "json": None
            }
