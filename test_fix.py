# Test script to verify the plotting fix
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Create sample data similar to the notebook
print("Creating test data...")

# Sample GeoDataFrame with colors
from shapely.geometry import Point
data = {
    'comarca': ['A', 'B', 'C'],
    'color_rgb': [[0.5, 0.5, 0.5], [0.3, 0.7, 0.2], [0.8, 0.1, 0.4]],
    'geometry': [Point(0, 0), Point(1, 1), Point(2, 2)]
}
gdf = gpd.GeoDataFrame(data, crs='EPSG:4326')

# Test the plotting approach
fig, ax = plt.subplots(figsize=(10, 10))

# Method 1: Original (problematic)
try:
    gdf.plot(ax=ax, color=gdf['color_rgb'].tolist(), edgecolor='black')
    print("✓ Original method works!")
except Exception as e:
    print(f"✗ Original method failed: {e}")

# Method 2: Individual plotting (our fix)
fig, ax = plt.subplots(figsize=(10, 10))
try:
    for idx, row in gdf.iterrows():
        gdf[gdf.index == idx].plot(ax=ax, color=[row['color_rgb']], edgecolor='black', linewidth=0.5)
    print("✓ Individual plotting method works!")
except Exception as e:
    print(f"✗ Individual plotting method failed: {e}")

print("\nTest completed.")
