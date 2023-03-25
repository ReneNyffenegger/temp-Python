from geopy.distance import great_circle
from geopy.point import Point

point1 = (37.7749, -122.4194)  # San Francisco, CA
point2 = (40.7128, -74.0060)   # New York, NY
point3 = (41.8781, -87.6298)   # Chicago, IL

# Create a great circle defined by two points (San Francisco and New York)
great_circle_arc = great_circle(point1, point2)

# Calculate the shortest distance from the great circle to the given point (Chicago)
shortest_distance = great_circle_arc.cross_track_distance(Point(point3))

print(f"Shortest distance to the great circle: {shortest_distance:.2f} km")
