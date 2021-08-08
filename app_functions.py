from math import radians, cos, sin, asin, sqrt

EARTH_RADIUS = 6371

_radius = {
    "MI" : 3959.9, 
    "KM" : 6372.8, 
}

def haversine(lat1, lon1, lat2, lon2, is_rads, unit):
    """Returns distance between lat long coordinates in specified unit"""
    RADIUS = _radius[unit]

    if not is_rads:
        delta_lat = radians(lat2 - lat1)
        delta_lon = radians(lon2 - lon1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
    else:
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1
        lat1 = lat1
        lat2 = lat2

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon/2) ** 2
    c = 2 * asin(sqrt(a))

    return RADIUS * c