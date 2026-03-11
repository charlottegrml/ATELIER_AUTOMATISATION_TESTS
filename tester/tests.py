from tester.client import call_api

def test_status():

    r = call_api()

    return r["status"] == 200


def test_json():

    r = call_api()

    return isinstance(r["json"], dict)


def test_base_field():

    r = call_api()

    return "base" in r["json"]


def test_rates_field():

    r = call_api()

    return "rates" in r["json"]


def test_date_field():

    r = call_api()

    return "date" in r["json"]


def test_rates_type():

    r = call_api()

    return isinstance(r["json"]["rates"], dict)
