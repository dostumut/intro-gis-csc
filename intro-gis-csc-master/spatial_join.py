# -*- coding: utf-8 -*-
"""
spatial_join.py

How to conduct spatial join using geopandas.

Created on Tue Nov 13 14:46:41 2018

@author: Henrikki Tenkanen
"""
import geopandas as gpd

# Filepaths
pop_fp = "L4_data/Vaestotietoruudukko_2015.shp"
point_fp = "L4_data/addresses.shp"

# Read the data
pop = gpd.read_file(pop_fp)
points = gpd.read_file(point_fp)

# Ensure that the datasets are in same projection
points = points.to_crs(crs=pop.crs)

# Check that the CRS matches
assert pop.crs == points.crs, "The CRS of the layers do not match!"

# Make spatial join
join = gpd.sjoin(points, pop, how="inner", op='within')

# Visualize
join.plot(column='ASUKKAITA', cmap='Reds', markersize=join['ASUKKAITA']/1642*100, legend=True)





