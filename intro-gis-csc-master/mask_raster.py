# -*- coding: utf-8 -*-
"""
mask_raster.py

How to use Rasterio to mask (clip) raster files.

Created on Wed Nov 14 11:07:34 2018

@author: Henrikki Tenkanen
"""
import rasterio
from rasterio.plot import show
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
import pycrs
import os
from raster_tools import get_features

# Data dir
data_dir = "L5_data"

# Input
fp = os.path.join(data_dir, 'p188r018_7t20020529_z34__LV-FIN.tif')

# Output raster
out_tif = os.path.join(data_dir, 'Helsinki_masked.tif')

# Read the data
raster = rasterio.open(fp)

# Visualize NIR
show((raster, 4), cmap='terrain')

# WGS84 coordinates
minx, miny = 24.60, 60.00
maxx, maxy = 25.22, 60.35
bbox = box(minx, miny, maxx, maxy)

# Create a GeoDataFrame
crs_code = pycrs.parser.from_epsg_code(4326).to_proj4()
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=crs_code)

# Project the GeoDataFrame to the same projection as the raster
geo = geo.to_crs(crs=raster.crs)

# Convert GeoDataFrame to geometric features dict
coords = get_features(geo)

# Clip the raster based on Polygon
out_img, out_transform = mask(dataset=raster, shapes=coords, crop=True)

# Copy the metadata
out_meta = raster.meta.copy()

# Parse Proj4 information to store with the raster
epsg_code = int(raster.crs.data['init'].replace('epsg:', ''))
epsg_proj4 = pycrs.parser.from_epsg_code(epsg_code).to_proj4()

# Update metadata with new dimensions, crs etc.
out_meta.update(
        {"height": out_img.shape[1],
         "width": out_img.shape[2],
         "transform": out_transform,
         "crs": epsg_proj4
         }
        )


# Save the clipped raster to disk
with rasterio.open(out_tif, 'w', **out_meta) as dest:
    dest.write(out_img)

# Open and plot
clipped = rasterio.open(out_tif)
show((clipped, 5), cmap='terrain')






