'''
Having run route_plot.py multiple times
and saved the data as a shapefile
here we load that file
and plot what we have in pretty colors
'''


import sys,os,subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh
    
def load_and_plot_route(ax,fn,color='red'):
    path = fh.local_data_path + fn + '.shp.zip'
    gdf = gpd.read_file(path)
        
    ph.plot_region(ax,region='western_states')
    ph.plot_gdf(ax,gdf,color=color)
    
    path = fh.local_data_path + fn + '.txt'
    data = fh.read_file(path)
    L = data.strip().split('\n')
    
    X = list()
    Y = list()
    for line in L:
        if not '[' in line:
            continue
        p = fmt.parse_point_str(line.strip())
        X.append(p.lon)
        Y.append(p.lat)
    
    ph.plot_points(ax,X,Y,SZ=20)

size=(7,7)
fig,ax = plt.subplots(figsize=(size))
  
colors=['red','blue','orange']
trips = ['cc','sw','co']
for trip,color in zip(trips,colors):
    fn = trip + '-adventure'
    load_and_plot_route(ax,fn,color=color)
    
ph.save_and_show_file(fig,'big_save',scrub=False)
