# -*- coding: utf-8 -*-
"""
nearest_points.py

How to get the nearest point of another one.

Created on Tue Nov 13 15:11:25 2018

@author: Henrikki Tenkanen
"""
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import geopandas as gpd

def nearest(row, geom_union, df2, geom1_col='geometry', geom2_col='geometry', src_column=None):
    """Find the nearest point and return the corresponding value from specified column."""

    # Find the geometry that is closest
    nearest = df2[geom2_col] == nearest_points(row[geom1_col], geom_union)[1]

    # Get the corresponding value from df2 (matching is based on the geometry)
    value = df2[nearest][src_column].get_values()[0]

    return value
    
# Filepaths
fp1 = "L4_data/PKS_suuralue.kml"
fp2 = "L4_data/addresses.shp"

# Activate KML driver
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

# Read data
polys = gpd.read_file(fp1)
src_points = gpd.read_file(fp2)

# Unary union
unary_union = src_points.unary_union

# Calculate the centroid for the polygons
polys['centroid'] = polys.centroid

# Find the nearest PT station for each Polygon centroid
polys['nearest_id'] = polys.apply(nearest, geom_union=unary_union, 
     df1=polys, df2=src_points, 
     geom1_col='centroid', src_column='id', axis=1)






