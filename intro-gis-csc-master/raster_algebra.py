# -*- coding: utf-8 -*-
"""
raster_algebra.py

How to do raster calculations using rasterio and numpy.

Created on Wed Nov 14 12:58:10 2018

@author: Henrikki Tenkanen
"""
import rasterio
import numpy as np
from rasterio.plot import show
import os
import matplotlib.pyplot as plt

# Data directory
data_dir = "L5_data"
fp = os.path.join(data_dir, 'Helsinki_masked.tif')

# Open the data
raster = rasterio.open(fp)

# Read channels for red and NIR
red = raster.read(3)
nir = raster.read(4)

# Stats
red.mean()
nir.mean()

# Plot
show(nir, cmap='terrain')

# Convert to floats
red = red.astype('f4')
nir = nir.astype('f4')

# Ignore 'division by zero' exception
np.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI
ndvi = (nir - red) / (nir + red)

# Plot the ndvi with legend
plt.imshow(ndvi, cmap='terrain_r')
plt.colorbar()

# Time series
#change = year2018 - year2008 



