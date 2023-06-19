import sys,os,subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

import update_path

import utils.ufile as fh

script_name = fh.get_name(__file__)

data_path = fh.data_path

# simple way to only include the continental 48
def clip(df):
    xmin,ymin,xmax,ymax = -124.9,25.02,-66.74,49.1
    return df.cx[xmin:xmax, ymin:ymax]

# --------------------------------

fn = 'gz_2010_us_040_00_5m'
outline = gpd.read_file(data_path + fn)
outline = clip(outline)

fn = 'tl_2019_us_primaryroads'  # interstates
roads = gpd.read_file(data_path + fn)
roads = clip(roads)

# --------------------------------

# a bit more sophisticated
# we don't want ring roads like I- 405 

def filter(e):
    return len(e) <= 5   #I- 55 but not I- 495
    
sel = [filter(e) for e in roads['FULLNAME']]
roads = roads[sel]

# --------------------------------

fig, ax = plt.subplots(figsize=(7,7))

# I've made this mistake a lot
# if plot is called with no axes provided
# matplotlib just ignores the previous one

outline.boundary.plot(ax=ax,color='blue',linewidth=1)
roads.plot(ax=ax,color='red')

ofn = fh.demo_img_path + script_name+'.png'
plt.savefig(ofn, dpi=300)

subprocess.run(['open','-a','Preview',ofn])