import sys
import subprocess
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh


# sL = ['AZ','NM','UT','CO']

outline = gh.get_geodataframe_for_stateL(['AZ'])
roads = gh.get_geodataframe_for_state_roads('AZ')
interstates = gh.get_geodataframe_for_interstates()

targetL = ['State Rte 101',
           'State Rte 260',
           'State Rte 89A',
           'N State Rte 89A',
           'US Hwy 180',
           'State Rte 64',
           #'US Hwy 64',
           'US Hwy 89A',
           'N US Hwy 89']

# note:  part of State Rte 64 is missing
# (east from Grand Canyon Village

gdf = sh.multi_road_search(
    roads,
    targetL,
    strict=False)

i17 = sh.search(interstates,'I- 17')
gdf = pd.concat((gdf,i17))

fig, ax = plt.subplots(
    figsize=(7,7))

roads.plot(ax=ax,
    color='lightgray',zorder=0)

gdf.plot(
    ax=ax,
    color='red',zorder=1)

gdf.boundary.plot(
    ax=ax,
    color='black',markersize=10,zorder=2)

outline.boundary.plot(
    ax = ax,
    color='blue',zorder=3)

script_name = __file__.split('.')[0]
path = fh.demo_img_path + 'regional_roads.png'
plt.savefig(path, dpi=300)
ph.show_image(path)
