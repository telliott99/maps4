'''
almost the simplest demo for plotting state outlines
uses a color map, "magma"
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

#-------------------------------
# US gdf includes Hawaii, Alaska, Puerto Rico
# too big to plot nicely

# could clip the region using .cx
# gdf = ph.gdf_clip(gdf)  # has the default values

# or, filter the gdf
def lower48(gdf):
    L = ['HI','AK','PR']
    f = sh.filter_out_by_COL
    return f(gdf,L,'STATE')

gdf = gh.get_geodataframe_for_us48()
gdf = lower48(gdf)

#-------------------------------

# we'll handle the plot here

fig, ax = plt.subplots(figsize=(10,10))
gdf.plot(cmap='magma')


# ---------------------------------

script_name = fh.get_name(__file__)
fn = script_name + '.png'
path = fh.demo_img_path + fn
plt.savefig(path)

cmd = ['open','-a','Preview', path]
subprocess.run(cmd)

