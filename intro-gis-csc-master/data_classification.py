# -*- coding: utf-8 -*-
"""
data_classification.py

Classify data values based on common classifiers.

Created on Tue Nov 13 13:08:13 2018

@author: Henrikki Tenkanen
"""
import geopandas as gpd
import pysal as ps

# Filepath
fp = "L3_data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"

# Read the data
data = gpd.read_file(fp)

# Exclude -1 values (NoData)
data = data.loc[data['pt_r_tt']>=0]

# Plot data based on Fisher Jenks with 9 classes
data.plot(column='pt_r_tt', scheme='Fisher_Jenks', 
          k=10, cmap='RdYlBu', 
          linewidth=0, legend=True)

# Define the number of classes
k = 12

# Initialize the natural breaks classifier
classifier = ps.Natural_Breaks.make(k)

# Classify the travel time values
classifications = data[['pt_r_tt']].apply(classifier)

# Rename the column 'nb_pt_r_tt'
classifications = classifications.rename(columns={'pt_r_tt': 'nb_pt_r_tt'})

# Conduct table join based on index
data = data.join(classifications)

# Create a map based on new classes
ax = data.plot(column='nb_pt_r_tt', linewidth=0, legend=True)

# Create a custom classifier
class_bins = [10, 20, 30, 40, 50, 60]

# Custom classifier
classifier = ps.User_Defined.make(class_bins)

# Classify the travel time values
custom_classifications = data[['pt_r_tt']].apply(classifier)

# Rename the column 'nb_pt_r_tt'
custom_classifications = custom_classifications.rename(columns={'pt_r_tt': 'c_pt_r_tt'})

# Conduct table join based on index
data = data.join(custom_classifications)

# Create a map based on new classes
ax = data.plot(column='c_pt_r_tt', linewidth=0, legend=True)


