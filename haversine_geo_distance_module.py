from haversine import haversine, Unit

def distance_between_points(coord1, coord2):
    """
    Calculate the distance between two points on the Earth's surface using the Haversine formula.
    
    Parameters:
        coord1 (tuple): Latitude and Longitude of the first point in degrees (lat, lon).
        coord2 (tuple): Latitude and Longitude of the second point in degrees (lat, lon).
    
    Returns:
        float: The distance between the two points in kilometers.
    """
    return haversine(coord1, coord2, unit=Unit.KILOMETERS)
