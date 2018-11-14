# -*- coding: utf-8 -*-
"""
geocode_addresses.py

How to convert addresses to Points and vice versa.

Created on Tue Nov 13 10:19:43 2018

@author: Henrikki Tenkanen
"""
import geopandas as gpd
import pandas as pd
from geopandas.tools import geocode
import contextily as ctx


def add_basemap(ax, zoom, url='http://tile.stamen.com/terrain/tileZ/tileX/tileY.png', basemap=None, extent=None):
    """Adds basemap to figure"""    
    xmin, xmax, ymin, ymax = ax.axis()
    if basemap is None:
        basemap, extent = get_basemap(ax, zoom=zoom, url=url)
    ax.imshow(basemap, extent=extent, interpolation='bilinear')
    # restore original x/y limits
    ax.axis((xmin, xmax, ymin, ymax))
    return ax

def get_basemap(ax, zoom, url='http://tile.stamen.com/terrain/tileZ/tileX/tileY.png'):
    """Helper function to add a basemap for the plot"""
    xmin, xmax, ymin, ymax = ax.axis()
    basemap, extent = ctx.bounds2img(xmin, ymin, xmax, ymax, zoom=zoom, url=url)
    return basemap, extent
    
# Filepath
fp = "L3_data/addresses.txt"

# Read the data
data = pd.read_csv(fp, sep=';')

# Geocode the addresses from 'addr'
geo = geocode(data['addr'], provider='nominatim', user_agent='csc_user_ht')

# Merge geocoded locations back to the original DataFrame
geo = geo.join(data)

# Reproject to Web Mercator (epsg 3857)
geo = geo.to_crs(epsg=3857)

# Plot the data with background map
ax = geo.plot()

# Add basemap 
add_basemap(ax=ax, zoom=12)
