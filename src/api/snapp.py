"""Fetch Snapp's price for two geo-points."""
import json
import os
import requests


def get_snapp_price(origin: tuple[float, float], dest: tuple[float, float]) -> int:
    """Fetch the price of the trip by Snapp."""
    origin_lat = origin[0]
    origin_lng = origin[1]
    dest_lat = dest[0]
    dest_lng = dest[1]
    url = "https://app.snapp.taxi/api/api-base/v2/passenger/newprice/s/6/0"
    headers = headers = os.environ.get("SNAPP_HEADERS")
    null = None
    data = {
        "points": [
            {"lat": origin_lat, "lng": origin_lng},
            {"lat": dest_lat, "lng": dest_lng},
            null,
        ],
        "waiting": null,
        "round_trip": False,
        "voucher_code": null,
        "service_types": [1, 2],
        "hurry_price": null,
        "hurry_flag": null,
        "priceriderecom": False,
    }
    data = json.dumps(data)
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        dict_ = json.loads(resp.text)
        prices = dict_["data"]["prices"][0]
        if not (prices["is_discounted_price"]):
            raw_price = prices["final"]
        else:
            raw_price = prices["raw_fare"]

        raw_price_toman = raw_price // 10
        return raw_price_toman
    return 0
