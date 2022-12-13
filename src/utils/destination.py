"""Module providing a uniform random geo-point as a destination over 2 km from the origin"""
from . import tehran
from geopy.distance import geodesic as GD


def generate_dest(origin: tuple[float, float]) -> tuple[float, float]:
    """Generate random destinations of the passenger."""
    dest = tehran.random_req_tehran()
    if GD(origin, dest).km > 2:
        return dest
    return generate_dest(origin)
