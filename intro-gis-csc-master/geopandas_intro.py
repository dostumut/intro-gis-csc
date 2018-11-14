# -*- coding: utf-8 -*-
"""
geopandas_intro.py

Basic functionalities of Geopandas library.

Created on Mon Nov 12 13:16:26 2018

@author: Henrikki Tenkanen
"""
# Import geopandas
import geopandas as gpd
import pandas as pd

# Filepath
fp = "L2_data/DAMSELFISH_distributions.shp"

# Read the file with Geopandas
data = gpd.read_file(fp)

# Print the first rows of the data
data.tail(20)

# Print column names of the GeoDataFrame
cols = data.columns

# Plot the geometries
data.plot()

# Write the first 50 rows of our data into a new Shapefile
outfp = "L2_data/DAMSELFISH_selection.shp"
outfp2 = "L2_data/DAMSELFISH_selection.geojson"

# Select the first rows
selection = data.head(50)

# Save the selection
selection.to_file(outfp)

# Save as GeoJSON
selection.to_file(outfp2, driver='GeoJSON')

# Geometries in GeoDataFrame
# --------------------------

#data.columns
#sel3 = data[['geometry', 'BINOMIAL']]

# Unique species can be found from the data
#unique = data['BINOMIAL'].unique()
#criteria = 'Stegastes redemptus'

# Select rows based on criteria
#fish_a = data.loc[(data['ValueX']>10) & (data['ValueY']<100)]
#import psycopg2
#import geoalchemy2

# Initialize the connection with driver such psycopg2
#conn, cursor = psycopg2.connect()
#pgdata = gpd.read_postgis(sql="SELECT * FROM TABLEX FETCH FIRST 10 ROWS;", con=conn)

# ITERATING ROWS IN GEOPANDAS / PANDAS
# ------------------------------------
# Alternative 1: Iterate over GeoDataFrame
for index, row in selection.iterrows():
    # Calculate the area of each Polygon
    poly_area = row['geometry'].area
    print(poly_area)
    
# Alternative 2
data['area'] = data.apply(lambda row: row['geometry'].area, axis=1)

# Alternative 3
def calculate_area(row):
    return row['geometry'].area 
   
data['area2'] = data.apply(calculate_area, axis=1)

# Geometric attributes from GeoDataFrame
# --------------------------------------

# Calculate the area using geopandas directly
data['area3'] = data.area
data['centroid'] = data.centroid

# Set the geometry source for GeoDataFrame
geo = data.copy()
geo = geo.set_geometry('centroid')
geo.plot()

# Drop the 'geometry' column from gdf
geo = geo.drop('geometry', axis=1)

# Create a buffer from points
geo['buffer'] = geo.buffer(10)
geo = geo.set_geometry('buffer')

# Save points
geo.to_file('geom_centroids.shp')

# Calculate basic statistics
mean_area = geo['area'].mean()
min_area = geo['area'].min()
max_area = geo['area'].max()
std_area = geo['area'].std()
median_area = geo['area'].median()

# Calculate in (Geo)DataFrame
geo['areaX2'] = geo['area'] + geo['area2']







