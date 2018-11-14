# -*- coding: utf-8 -*-
"""
read_cloud_optimized_geotiffs.py

Created on Wed Nov 14 15:07:46 2018

@author: Henrikki Tenkanen
"""
import rasterio
import matplotlib.pyplot as plt
import numpy as np
from rasterio.plot import show

# Specify the path for Landsat TIF on AWS
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'

# Get the profile
src = rasterio.open(url)

#with rasterio.open(url) as src:
#    print(src.profile)
    
# Get the list overviews
oviews = src.overviews(1)
oview = oviews[-1]

# Read a thumbnail using low resolution source
thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)  ) )

# plot 
show(thumbnail, cmap='terrain')

# Retrieve a "Window" (a subset) from full resolution raster
window = rasterio.windows.Window(1024, 1024, 1280, 2560)

# Retrieve a subset of the data
subset = src.read(1, window=window)

# Plot the subset
show(subset, cmap='terrain')

fp = 'http://86.50.168.160/syke/corine/2012/corine_2012_0_6800000.tif'

src2 = rasterio.open(fp)

oviews = src2.overviews(1)
oview = oviews[2]

# Read a thumbnail using low resolution source
thumbnail2 = src2.read(1, out_shape=(1, int(src2.height // oview), int(src2.width // oview)  ) )
show(thumbnail2)




