# -*- coding: utf-8 -*-
"""
download_osm_data.py

Use OSMnx package to download OSM data using OverPass API.

Created on Tue Nov 13 11:17:30 2018

@author: Henrikki Tenkanen
"""

import osmnx as ox
import matplotlib.pyplot as plt

# Specify the name of the area of interest for us
place_name = "Kamppi, Helsinki, Finland"

# Retrieve the data from OSM
graph = ox.graph_from_address(place_name)

# Plot the streets
fig, ax = ox.plot_graph(graph)

# Convert the graph to GeoDataFrames
nodes, edges = ox.graph_to_gdfs(graph)

# Retrieve buildings from OSM
buildings = ox.buildings_from_address(place_name, distance=1000)

# Footprint of Kamppi
footprint = ox.gdf_from_place(place_name)
footprint.plot()

# Retrieve Points of Interest from OSM
restaurants = ox.pois_from_place(place_name, amenities=['restaurant', 'bar'])

# Plot all layers together
ax = footprint.plot(facecolor='black')
ax = edges.plot(ax=ax, linewidth=1, edgecolor='#BC8F8F')
ax = buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)
ax = restaurants.plot(ax=ax, color='green', alpha=0.7, markersize=10)


