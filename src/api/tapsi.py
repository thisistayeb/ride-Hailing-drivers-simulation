"""Fetch Tapsi's price for two geo-points."""
import requests, json, os


def get_tapsi_price(origin: tuple[float, float], dest: tuple[float, float]) -> int:
    """Fetch the price of the trip by Tapsi."""
    origin_lat = origin[0]
    origin_lng = origin[1]
    dest_lat = dest[0]
    dest_lng = dest[1]
    url = "https://api.tapsi.cab/api/v2.4/ride/preview"
    headers = os.environ.get("TAPSI_HEADERS")
    data = {
        "origin": {"latitude": origin_lat, "longitude": origin_lng},
        "destinations": [{"latitude": dest_lat, "longitude": dest_lng}],
        "hasReturn": False,
        "waitingTime": 0,
        "gateway": "CAB",
        "initiatedVia": "WEB",
    }
    data = json.dumps(data)
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        dict_ = json.loads(resp.text)
        normal_tapsi = dict_["data"]["categories"][0]["services"][0]
        price_tapsi = int(normal_tapsi["prices"][0]["passengerShare"]) + int(
            normal_tapsi["prices"][0]["discount"]
        )
        return price_tapsi
    return 0
