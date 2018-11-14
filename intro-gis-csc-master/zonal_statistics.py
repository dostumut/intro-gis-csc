# -*- coding: utf-8 -*-
"""
zonal_statistics.py

How to calculate zonal statistics using rasterio and rasterstats.

Created on Wed Nov 14 13:52:33 2018

@author: Henrikki Tenkanen
"""

import rasterio
from rasterio.plot import show
from rasterstats import zonal_stats
import osmnx as ox
import geopandas as gpd
import os
import matplotlib.pyplot as plt

# Filepath
data_dir = "L5_data"
dem_fp = os.path.join(data_dir, 'Helsinki_DEM_2x2m_mosaic.tif')

# Read the data
dem = rasterio.open(dem_fp)

# Fetch the Polygons for zonal statistics from OSM
kallio_q = "Kallio, Helsinki, Finland"
pihlajamaki_q = "Pihlajamäki, Malmi, Helsinki, Finland"

# Retrieve the geometries from OSM
kallio = ox.gdf_from_place(kallio_q)
pihlajamaki = ox.gdf_from_place(pihlajamaki_q)

# Test that crs matches
#assert kallio.crs == dem.crs, "CRS do not match between layers!"
#assert pihlajamaki.crs == dem.crs, "CRS do not match between layers!"

# Reproject the Polygon to same projection as raster
kallio = kallio.to_crs(crs="+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")
pihlajamaki = pihlajamaki.to_crs(crs="+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")

# Plot the areas on top of the raster
ax = kallio.plot(facecolor='None', edgecolor='red', linewidth=2)
ax = pihlajamaki.plot(ax=ax, facecolor='None', edgecolor='blue', linewidth=2)

# Plot the raster below
show((dem, 1), ax=ax)
#show((dem, 1))
#

# Use zonal statistics to assess which are is higher
# --------------------------------------------------

# Read the data
array = dem.read(1)

# Get the affine
affine = dem.transform

# Calculate zonal statistics
zs_kallio = zonal_stats(kallio, array, 
                        affine=affine, 
                        stats=['min', 'max', 
                               'mean', 'median', 
                               'majority'])

zs_pihla = zonal_stats(pihlajamaki, array, 
                        affine=affine, 
                        stats=['min', 'max', 
                               'mean', 'median', 
                               'majority'])

# Which one is higher
if zs_kallio[0]['max'] > zs_pihla[0]['max']:
    print("Kallio is higher!")
else:
    print("Pihlajamäki is higher!")

# Dictionary
zs_results = {}

for channel in range(1,5):
    zs_results[channel] = zonal_stats(polygon, channel_data_array, stats=['min', 'max'])

















