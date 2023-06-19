import sys, os, subprocess, time

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import utils.ugeo as gh
import utils.ufile as fh

# default
crs="EPSG:4269"

def get_default_path(fn):
    return fh.img_path + fn

# generate unique timestamps 
# with millisecond resolution
def get_timestamp():
    t = time.time()
    whole = str(int(t))
    rest = str(t).split('.')[1]
    return '-' + whole[-4:] + '.' + rest[2:]
    
def show_image(path,scrub=False):
    v = False
    if v:
        print('show_image')
        print(path)
        print()

    cmd = ['open','-a','Preview', path]
    subprocess.run(cmd)
   
    if scrub:
        time.sleep(2)
        cmd = ['rm', path]
        subprocess.run(cmd)

def save_and_show_file(
        fig,
        script_name,
        dpi=300,
        scrub=False):
        
    t = fh.get_timestamp()
    fn = script_name + t + '.png'
    
    if script_name.startswith('test'):
        path = fh.test_img_path + fn
    elif script_name == 'search_CL':
        path = fh.test_img_path + fn
    else:
        path = fh.demo_img_path + fn

    #fig.tight_layout()
    v = False
    if v:
        print('save_fig')
        print(path)
        print()
    plt.savefig(path,dpi=dpi)
    
    # show the image file and then delete it
    show_image(path,scrub=scrub)

# --------------------------------
    
def plot_region(
    ax,
    region='western_states',
    stateL=None):
        
    # get the data for the outline:
    # region could be one of 'western_states' etc
    
    # these must be valid names of shapefiles in data-shp/
    # otherwise, the abbreviated names of states in a list

    if not (region or stateL):
        outline_gdf = gh.get_geodataframe_for_us48()
    if region == 'us48':
        outline_gdf = gh.get_geodataframe_for_us48()
    elif stateL:
        outline_gdf = gh.get_geodataframe_for_stateL(
            stateL)
    else:  # region
        outline_gdf = gh.get_geodataframe_for_region(
            region)

    # outlines always in the first layer 
    # zorder=0
    outline_gdf.boundary.plot(
        ax=ax,
        color='blue', 
        linewidth=0.75,
        zorder=3)

# we want this to be flexible
# hence we accept simple lists
# X = x-values and Y = y-values plus optional labels   

def plot_points(ax,X,Y,
    labels=None,
    color='black',
    SZ=40):
    
    plt.scatter(X,Y,
        color=color,
        s=SZ,
        zorder=2)
   
def plot_gdf(
    ax,
    gdf,
    color='lightgray',
    linewidth=None):    
    
    if linewidth is None:
        linewidth = 1
    gdf.plot(
        ax=ax,
        color=color,
        linewidth=linewidth,
        zorder=1)

