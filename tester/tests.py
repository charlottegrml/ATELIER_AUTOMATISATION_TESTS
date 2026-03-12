from tester.client import call_api


def test_status_200():
    """GET /latest retourne HTTP 200"""
    r = call_api("/latest", {"from": "EUR"})
    ok = r["status"] == 200
    return {
        "name": "GET /latest → HTTP 200",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": f"Status reçu : {r['status']}" if not ok else ""
    }


def test_content_type_json():
    """La réponse est bien un dict JSON"""
    r = call_api("/latest", {"from": "EUR"})
    ok = isinstance(r["json"], dict) and r["status"] == 200
    return {
        "name": "Content-Type JSON valide",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": "Corps non JSON" if not ok else ""
    }


def test_champ_base():
    """Le champ 'base' est présent dans la réponse"""
    r = call_api("/latest", {"from": "EUR"})
    ok = "base" in r.get("json", {})
    return {
        "name": "Champ 'base' présent",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": "" if ok else "Champ 'base' manquant"
    }


def test_champ_rates():
    """Le champ 'rates' est présent et est un dict"""
    r = call_api("/latest", {"from": "EUR"})
    body = r.get("json", {})
    ok = "rates" in body and isinstance(body.get("rates"), dict)
    return {
        "name": "Champ 'rates' présent et dict",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": "" if ok else f"rates = {body.get('rates')}"
    }


def test_champ_date():
    """Le champ 'date' est présent et est une string"""
    r = call_api("/latest", {"from": "EUR"})
    body = r.get("json", {})
    ok = "date" in body and isinstance(body.get("date"), str)
    return {
        "name": "Champ 'date' présent (string)",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": "" if ok else f"date = {body.get('date')}"
    }


def test_conversion_eur_usd():
    """GET /latest?from=EUR&to=USD retourne un taux USD"""
    r = call_api("/latest", {"from": "EUR", "to": "USD"})
    body = r.get("json", {})
    ok = r["status"] == 200 and "USD" in body.get("rates", {})
    return {
        "name": "Conversion EUR→USD présente",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": "" if ok else "Taux USD absent"
    }


# ─────────────────────────────────────────────
# B. Tests ROBUSTESSE / cas invalides
# ─────────────────────────────────────────────

def test_devise_invalide_404():
    """Devise inconnue → doit retourner 404"""
    r = call_api("/latest", {"from": "ZZZ"})
    ok = r["status"] == 404
    return {
        "name": "Devise invalide → HTTP 404",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": f"Status reçu : {r['status']}" if not ok else ""
    }


def test_endpoint_inconnu_404():
    """Endpoint inexistant → doit retourner 404"""
    r = call_api("/route_inexistante", {})
    ok = r["status"] == 404
    return {
        "name": "Endpoint inconnu → HTTP 404",
        "status": "PASS" if ok else "FAIL",
        "latency_ms": r["latency_ms"],
        "details": f"Status reçu : {r['status']}" if not ok else ""
    }
