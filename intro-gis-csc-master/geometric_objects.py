# -*- coding: utf-8 -*-
"""
geometric_objects.py

Introduction to Shapely geometric objects and functionalities.

Requirements:
    - shapely
    
Notes:
    - This is just first taste of Python GIS

Created on Mon Nov 12 10:58:47 2018

@author: Henrikki Tenkanen
"""
# Import the geometric objects
from shapely.geometry import Point, LineString, Polygon

# Point
# -----

# Create Point objects
point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)

# Get the coordinates
point_coords = point1.coords

# Get xy coordinates
xy = point1.xy
print(xy)

# Get x and y coordinate
x = point1.x
y = point1.y

# Calculate the distance between point1 and point2
point_dist = point1.distance(point2)
print(point_dist)

# Create a buffer with distance of 20 units
point_buffer = point1.buffer(20)

# LineString
# ----------

# Create line based on Shapely Points
line = LineString( [point1, point2, point3 ] )

# Create line based on coordinate tuples
line2 = LineString( [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)] )

# Coordinates
lxy = line.xy

# Get x and y coordinates
x = line.xy[0]
y = line.xy[1]

# Get the lenght
l_length = line.length

# Get the centroid of the line
l_centroid = line.centroid

# Polygon
# -------
for x in range(5):
    # do something with x
    print(x)
    
    
# Create Polygon based on coordinate tuples
poly = Polygon([ (2.2, 4.2), (7.2, -25.1), (9.26, -2.456) ])

# Create Polygon based on Points
point_list = [point1, point2, point3]
poly2 = Polygon( [(p.x, p.y) for p in point_list ] )

# Get geometry type as string
poly_type = poly.geom_type

# Calculate the area
poly_area = poly.area

# Centroid
poly_centroid = poly.centroid

# Bounding box
poly_bbox = poly.bounds

# Create Bounding box geometry
from shapely.geometry import box

# Unpack the bounding box coordinates with asterix (*)
bbox = box(*poly_bbox)

# Get exterior
poly_exterior = poly.exterior

# Lenght of exterior
poly_ext_length = poly.exterior.length

# Polygon with hole(s)
# --------------------

# Exterior of the world in decimal degrees
world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

# Create a large hole leaving 10 decimal degree boundary
hole = [[ (-170, 80), (-170, -80), (170, -80), (170, 80) ]]
world_poly = Polygon(shell=world_exterior, holes=hole)
