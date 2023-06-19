'''
plot a simple route Los Angeles - Portland
'''

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

# ---------------------------------

s = '''
Los Angeles, CA [-118.243685,34.052234]
I- 5
Portland, OR [-122.676482,45.523062]
'''

# a Segment has P,Q,hwy,stateL
seg = fmt.parse_segment_str(s)
# ---------------------------------

# init the plot
SZ=(7,7)
fig,ax = plt.subplots(figsize=(SZ)) 

# ---------------------------------
              
stateL = ['CA','AZ','NM',
          'NV','UT','CO',
          'WA','OR','ID','WY','MT']
          
outline_gdf = gh.get_geodataframe_for_stateL(
    stateL)
    
ph.plot_gdf(ax,
    outline_gdf.boundary,
    color='lightgray')

# ---------------------------------

# actually, freeways or restricted entrance
gdf = gh.get_geodataframe_for_interstates()

# get interstates only
gdf = sh.filter_RTTYP(gdf,'I')

# remove all interstates not in outline
# magic!
sub = gpd.overlay(gdf, outline_gdf, how='intersection')

ph.plot_gdf(ax,
    sub,color='gray',linewidth=1.5)
    
# ---------------------------------

# search for I- 5, given above
route = sh.search(sub,seg.hwy)

# seg.box is oriented along P->Q
poly = gpd.GeoDataFrame([1], 
            geometry=[seg.box],crs=gdf.crs)
clp = route.clip(poly)

ph.plot_gdf(ax,
    clp,color='red',linewidth=3)
    

X = [seg.P.lon, seg.Q.lon]
Y = [seg.P.lat, seg.Q.lat]
ph.plot_points(ax,X,Y,color='blue',SZ=100)

# ---------------------------------

script_name = fh.get_name(__file__)
fn = script_name + '.png'
path = fh.demo_img_path + fn
plt.savefig(path)

cmd = ['open','-a','Preview', path]
subprocess.run(cmd)
