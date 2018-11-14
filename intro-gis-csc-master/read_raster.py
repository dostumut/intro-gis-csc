# -*- coding: utf-8 -*-
"""
read_raster.py

Reading raster files with rasterio.

Created on Wed Nov 14 09:13:22 2018

@author: Henrikki Tenkanen
"""
import rasterio
import os
import numpy as np

# Data 
data_dir = r"C:\HY-DATA\HENTENKA\KOODIT\Opetus\CSC_lesson_codes"
#data_dir = "/home/htenkanen/Lesson"
fp = os.path.join(data_dir, 'L5_data', 'Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif')

# Open the file
raster = rasterio.open(fp)

# Projection
print(raster.crs)

# Affine transform
raster.transform

# Dimensions of the raster
raster.width
raster.height

# Number of channels
raster.count

# Bounds of the file
raster.bounds

# Driver
raster.driver

# No Data value
raster.nodatavals

# All metadata at once
raster.meta

# Read the data values to Python
# ------------------------------

# Read the raster into Numpy array
band1 = raster.read(1)

# Access the data type
data_type = str(band1.dtype)

# Calculate basic statistics
# --------------------------

# Read all the bands
array = raster.read()

# Calculate channel statistics
stats = []

# Skip rows
skip = 4

for idx, band in enumerate(array):
    if idx < skip:
        continue
        
    band_stat = {
            'min': band.min(),
            'max': band.max(),
            'median': np.median(band),
            'mean': band.mean(),
            'std': band.std()
            }
    # Insert stats inside another dict
    channel_stat = {'channel %s' % (idx+1): band_stat}
    # Append to list
    stats.append(channel_stat)
    

# Make a change    
    
    
    
    
    







