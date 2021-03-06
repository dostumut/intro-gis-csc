# -*- coding: utf-8 -*-
"""
read_wfs.py

Created on Tue Nov 13 09:29:02 2018

@author: Henrikki Tenkanen
"""

import geopandas as gpd
import requests
import geojson
import pycrs

# URL for WFS backend
url = "http://geo.stat.fi/geoserver/vaestoruutu/wfs"

# Get capabilities
capabilities_params = dict(service='WFS', request='GetCapabilities')

# Request
capabilities = requests.get(url, params=capabilities_params)
print(capabilities.content)

# Specify the parameters for fetching the data
params = dict(service='WFS', version='2.0.0', request='GetFeature',
          typeName='vaestoruutu:vaki2017_5km', outputFormat='json')

# Fetch the data from WFS
r = requests.get(url, params=params)

# Create a GeoDataFrame from the response
data = gpd.GeoDataFrame.from_features(geojson.loads(r.content))

# Define CRS
#data.crs = {'init': 'epsg:3067'}
data.crs = pycrs.parser.from_epsg_code(3067).to_proj4()

# Set geometry
data = data.set_geometry('geometry')

# Remove column with lists
data = data.drop('bbox', axis=1)

# Save to disk
outfp = "L2_data/Population_grid_5km.gpkg"
data.to_file(outfp, driver='GPKG')









