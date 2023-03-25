# from geographiclib.geodesic import Geodesic
# 
# point1 = (37.7749, -122.4194)  # San Francisco, CA
# point2 = (40.7128, -74.0060)   # New York, NY
# point3 = (41.8781, -87.6298)   # Chicago, IL
# 
# geod = Geodesic.WGS84
# 
# # Calculate the geodesic line between point1 and point2
# line = geod.InverseLine(point1[0], point1[1], point2[0], point2[1])
# 
# # Calculate the projection of point3 onto the line
# projection = line.ArcPosition(0, point3[0], point3[1], Geodesic.DISTANCE | Geodesic.LONG_UNROLL)
# 
# # Calculate the cross-track distance
# cross_track_distance = projection['s12']
# 
# print(f"Shortest distance to the great circle: {cross_track_distance / 1000:.2f} km")
# 
# 
from geographiclib.geodesic import Geodesic

point1 = (37.7749, -122.4194)  # San Francisco, CA
point2 = (40.7128, -74.0060)   # New York, NY
point3 = (41.8781, -87.6298)   # Chicago, IL

geod = Geodesic.WGS84

# Calculate the geodesic line between point1 and point2
line = geod.InverseLine(point1[0], point1[1], point2[0], point2[1])

# Calculate the projection of point3 onto the line
projection = line.Position(line.ClosestPoint(point3[0], point3[1])['s12'])

# Calculate the distance between the original point3 and its projection on the line
cross_track_distance = geod.Inverse(point3[0], point3[1], projection['lat2'], projection['lon2'])['s12']

print(f"Shortest distance to the great circle: {cross_track_distance / 1000:.2f} km")
