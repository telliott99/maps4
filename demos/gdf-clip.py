'''
exercises the clip method of GeoDataFrame
https://geopandas.org/en/stable/gallery/plot_clip.html
'''

import sys
import subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh

from shapely.geometry import box

script_name = 'gdf-clip'

gdf = gh.get_geodataframe_for_us48()

fig, ax = plt.subplots(
    figsize=(7,7))
gdf.boundary.plot(
    ax=ax,
    color='lightgray')

poly = box(-115,33,-105,40)
poly_gdf = gpd.GeoDataFrame(
    [1], 
    geometry=[poly], 
    crs=gdf.crs)
    
sub = gdf.clip(poly)
sub.boundary.plot(
    ax=ax,
    color='black')

poly_gdf.boundary.plot(
    ax=ax,
    color='red')

# ---------------------------------

func_name = fh.get_name(__file__)
fn = script_name + '.png'
path = fh.demo_img_path + fn
plt.savefig(path,dpi=300)

cmd = ['open','-a','Preview', path]
subprocess.run(cmd)




