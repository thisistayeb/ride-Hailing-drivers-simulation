"""Test all function works properly"""
import unittest
from src.utils import destination, origin, randpoint
from geopy.distance import geodesic as GD
from shapely import geometry
import random


def random_loc() -> tuple[int, int]:
    """Generate randol locatio in Earth"""
    lat = random.uniform(-90.0000000, 90.0000000)
    lng = random.uniform(-180.0000000, 180.0000000)
    loc = (lat, lng)
    return loc


class TestUtils(unittest.TestCase):
    """Test utils of the script"""

    def test_near_req(self):
        """Test that request for (35.14, 18.29) will be less than 1KM."""
        loc = (35.14, 18.29)
        new_loc = origin.near_req(loc)

        dist = GD(loc, new_loc).km
        result = dist <= 1
        self.assertTrue(result)

    def test_near_req_random(self):
        """Test that request for a random loc will be less than 1KM."""
        loc = random_loc()
        new_loc = origin.near_req(loc)

        dist = GD(loc, new_loc).km
        result = dist <= 1
        self.assertTrue(result)

    def test_generate_dest(self):
        """Test that distination of passanger in 35.14, 18.29 is more than 2km"""
        loc = (35.14, 18.29)
        new_loc = destination.generate_dest(loc)
        dist = GD(loc, new_loc).km
        result = dist >= 2
        self.assertTrue(result)

    def test_generate_des_random(self):
        """Test that distination of random passanger is more than 2km"""
        loc = random_loc()
        new_loc = destination.generate_dest(loc)
        dist = GD(loc, new_loc).km
        result = dist >= 2
        self.assertTrue(result)

    def test_random_point_in_shape(self):
        """Test if a random point in square of specefic square is inside that.
        specefic square: [[0,0],[0,1],[1,0],[1,1]]
        """
        shape = [[0, 0], [0, 1], [1, 0], [1, 1]]
        point = randpoint.gen_rand_point_shape(shape)

        polygon = geometry.Polygon(shape)
        point = geometry.Point(point)
        result = point.within(polygon)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
