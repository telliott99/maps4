'''
example from GeoPandas docs
https://geopandas.org/en/stable/docs/user_guide/data_structures.html
'''

import sys
import subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

# install with pip
import geodatasets

script_name = __file__.split('.')[0]

fn = 'geoda.malaria'
p = geodatasets.get_path(fn)
gdf = gpd.read_file(p)
#gdf.plot()

# this gdf has more than one geometry
print(gdf.geometry.name)
# geometry

# print(gdf.geometry.geom_type)
'''
0            Polygon
1            Polygon
..
1066    MultiPolygon
1067    MultiPolygon
Length: 1068, dtype: object
>
'''

# rename 'geometry' to 'borders'
gdf = gdf.rename_geometry('borders')

print(gdf.crs)
# EPSG:4326  # WGS84

gdf = gdf.to_crs('EPSG:5070')  # Albers
gdf['centroids'] = gdf.centroid
gdf = gdf.set_geometry('centroids')

gdf.plot()

ofn = script_name + '.png'
plt.savefig(ofn)
subprocess.run(['open','-a','Preview',ofn])
