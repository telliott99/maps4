import sys,subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh

script_name = 'simple'

s = '''
Santa Monica, CA [-117.0652,34.0039]
I- 10
Jacksonville, FL [-81.693942,30.321433]
'''
seg = fmt.parse_segment_str(s)
target = seg.hwy

SZ=(7,7)
fig,ax = plt.subplots(figsize=(SZ)) 

# grab the data for the US
outline = gh.get_geodataframe_for_us48()

# default bounds are set wrong, not sure why
xlim = ([-126,-66])
ylim = ([24,50])
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# plot it
outline.boundary.plot(ax=ax,
    color='blue',linewidth=0.5)

# grab the interstates
gdf = gh.get_geodataframe_for_interstates()

# plot them all
gdf.plot(ax=ax,
    color='lightgray',linewidth=0.8)

# search for I-10
sub = sh.search(gdf,target,strict=True)
sub.plot(ax=ax,
    color='red',linewidth=1.5)

# ---------------------------------

script_name = __file__.split('.')[0]
fn = script_name + '.png'
path = fh.demo_img_path + fn
plt.savefig(path)

cmd = ['open','-a','Preview', path]
subprocess.run(cmd)
