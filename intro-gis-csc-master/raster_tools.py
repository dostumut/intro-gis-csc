# -*- coding: utf-8 -*-
"""
raster_tools.py

Useful functions related to raster processing.

Created on Wed Nov 14 10:25:29 2018

@author: Henrikki Tenkanen
"""

import numpy as np
import json

def normalize(array):
    """Normalizes numpy arrays into scale 0.0 - 1.0"""
    array_min, array_max = array.min(), array.max()
    return ((array  - array_min) / (array_max - array_min))

def get_features(gdf):
    """Converts GeoDataFrame into a format how 
       rasterio mask function wants to have the geometric
       features.
    """
    features = [json.loads(gdf.to_json())['features'][0]['geometry']]
    return features
    








