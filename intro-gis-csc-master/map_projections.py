# -*- coding: utf-8 -*-
"""
map_projections.py

Introduction to Map projections. 


Created on Mon Nov 12 15:24:37 2018

@author: Henrikki Tenkanen
"""
import geopandas as gpd
import matplotlib.pyplot as plt

# Filepath
fp = "L2_data/Europe_borders.shp"

# Read the data
data = gpd.read_file(fp)

# Check the coordinate reference system
print(data.crs)

# Reproject the GeoDataFrame to EPSG 3035
geo = data.copy()
geo = geo.to_crs(epsg=3035)

# Plot and see the difference
# ---------------------------

# Create subplots 
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,8))

# Plot WGS84 to ax1
data.plot(ax=ax1, facecolor='gray')
geo.plot(ax=ax2, facecolor='blue')

# Set titles
ax1.set_title("WGS84", fontsize=24)
ax2.set_title("ETRS Lambert Azimuthal Equal Area", fontsize=24)

# Save the figure on disk
plt.savefig("projections.png", dpi=300)

# Save reprojected data to disk
outfp = "L2_data/Europe_borders_epsg3035.shp"

# Fix the CRS
import pycrs
proj4 = pycrs.parser.from_epsg_code(3035).to_proj4()
geo.crs = proj4
geo.to_file(outfp)






