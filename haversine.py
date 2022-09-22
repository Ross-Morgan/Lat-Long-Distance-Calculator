from enum import Enum
from math import radians, cos, sin, asin, sqrt
from typing import Union


class Radius(Enum):
    KM = 6372.8
    MI = 3959.9
    NM = 3440.0647948164


def haversine(lat1: float, lon1: float, lat2: float, lon2: float, unit: Union[str, Radius], is_rads: bool = False):
    """Returns distance between lat long coordinates in specified unit"""
    RADIUS = Radius[unit]

    if not is_rads:
        delta_lat = radians(lat2 - lat1)
        delta_lon = radians(lon2 - lon1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
    else:
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon/2) ** 2
    c = 2 * asin(sqrt(a))

    return RADIUS * c
