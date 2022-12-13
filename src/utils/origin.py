"""This module generates the passenger's origin."""
import math
import random


def near_req(loc: tuple[int, int]) -> tuple[int, int]:
    """Generate random geo-points with at most 1 km distance."""
    lat = loc[0]
    lng = loc[1]
    theta = 2 * math.pi * math.sqrt(random.random())
    radius_in_deg = 1 / 40000 * 360
    r = math.sqrt(random.random()) * radius_in_deg
    new_lat = lat + (r * math.cos(math.radians(theta)))
    new_lng = lng + (r * math.sin(math.radians(theta)))
    new_loc = (new_lat, new_lng)
    return new_loc
