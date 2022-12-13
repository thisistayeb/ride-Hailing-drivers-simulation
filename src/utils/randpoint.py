"""Module providing a function generates uniform random geo-point inside a polygon."""
import random
from shapely import geometry


def gen_rand_point_square(polygon: list[list[float]]) -> tuple[float, float]:
    """generate a circumscribed quadrilateral of *any shape* and generate a random point inside it."""
    all_points_x = []
    all_points_y = []
    for item in polygon:
        all_points_x.append(item[0])
    for item in polygon:
        all_points_y.append(item[1])
    min_x = min(all_points_x)
    max_x = max(all_points_x)
    min_y = min(all_points_y)
    max_y = max(all_points_y)
    rand_x = random.uniform(min_x, max_x)
    rand_y = random.uniform(min_y, max_y)
    rand_point = (rand_x, rand_y)
    return rand_point


def _check_point_in_shape(shape: list[list[float]], point: tuple[float, float]) -> bool:
    """check if `point` is inside the `shape`"""
    point = geometry.Point(point)
    return point.within(geometry.Polygon(shape))


def gen_rand_point_shape(shape: list[list[float]]) -> tuple[float, float]:
    """generate a uniformly random point inside any shape.

    Args:
        shape: a list of all points of the shape.

    Returns:
        A random point inside the `shape`.

    """
    point = gen_rand_point_square(shape)
    if _check_point_in_shape(shape, point):
        return point
    return gen_rand_point_shape(shape)
