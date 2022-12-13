"""Fetch distance (Km) and duration time (minutes) between two geo-points from Neshan API."""
import json
import os
from math import ceil

import requests

KEY = os.environ.get("NESHAN_KEY")


def distance(
    origin: tuple[float, float], dest: tuple[float, float], key=KEY
) -> tuple[int, float]:
    """request distance and duration time with due attention to real traffic

    Args:
        origin: a geo-point like [lat,lng] of origin
        dest: a geo-point like [lat,lng] of destination
        key: API KEY of Neshan

    Returns:
        Returns duration time in minutes and distance in Km
        When API doesn't respond correctly return both zero
    """
    req = f"https://api.neshan.org/v1/distance-matrix?type=car&origins={origin[0]},{origin[1]}&destinations={dest[0]},{dest[1]}"
    headers = {"Api-Key": key}
    respond = requests.get(req, headers=headers)
    resp = json.loads(respond.content)

    if resp["status"] == "Ok":
        data = resp["rows"][0]["elements"][0]
        duration_time = ceil(data["duration"]["value"] / 60)
        dist = data["distance"]["value"] / 1000
        return duration_time, dist
    return 0, 0
