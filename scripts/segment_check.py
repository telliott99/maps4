# part of QA for segment information
# generates a file for each segment

import sys, os, time, subprocess, time
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh

func_name = fh.get_name(__file__)
fn = func_name + '.png'

# for each segment of a route
# pull the highway data
# and draw the points and the box and the clip

fn = 'sw-adventure.txt'

try:
    arg = sys.argv[1]
    if arg.startswith('cc'):
        fn = 'cc-adventure.txt'
    elif arg.startswith('co'):
        fn = 'colorado-2014.txt'
      
except IndexError:
    print('usage:')
    print('python3 segment_check.py sw [i]')
    sys.exit()

try:
    i = int(sys.argv[2])
except IndexError:
    i = 0
    
fn = 'cc-rest.txt'

data = fh.read_file(fh.local_data_path + fn)

path = fh.DESK + 'tmp/'

# not split yet
data = data.strip().split('\n\n')
data = [e for e in data if not e.startswith('#')]

# data has a list of 'route_str'
# i allows us to skip the good ones

L = list()
for route_str in data[i:]:
    s = route_str.strip()
    L.extend(fmt.parse_route_str(s))
    
D = dict()
f = gh.get_geodataframe_for_state_roads
    
for seg in L:
    P,Q,stateL,hwy = seg.P,seg.Q,seg.stateL,seg.hwy
    print(seg)
    print()
    
    # start plot
    SZ=(7,7)
    fig,ax = plt.subplots(figsize=(SZ)) 
    
    # plot outline
    ph.plot_region(ax,
        stateL=stateL)

    # get road data
    for state in stateL:
        if not state in D:
            D[state] = f(state)
    gdf = D[state]
    
    ph.plot_gdf(ax,gdf)
    
    # find the highway
    sub = sh.search(gdf,seg.hwy,strict=False)
    if sub.empty:
        print('no sub: %s - %s' % (seg.P.name,seg.Q.name))
        print()
        continue
    else:
        ph.plot_gdf(ax,sub,color='gray')

    # clip it 
    poly = gpd.GeoDataFrame([1], 
            geometry=[seg.box],crs=gdf.crs)
           
    clp = sub.clip(poly)
    if clp.empty:
        print('no clp: %s - %s' % (seg.P.name,seg.Q.name))
        print()
        continue
    else:
        ph.plot_gdf(ax,clp,color='red')

    try:
        ph.plot_points(ax,(P.lon,Q.lon),(P.lat,Q.lat))    
        x, y = seg.box.exterior.xy
        ax.plot(x,y,color='blue')
    except:
        print('problem with plot_points')
        print()
        continue
    
    try:
        title = P.name + '-' + Q.name
        plt.title(title)
            
        fn = title + '.png'
        fn = str(int(time.time()*10))[-4:] + '_' +  fn
    except:
        print('problem with title')
        continue
    
    fig.tight_layout()
    try:        
        plt.savefig(path+fn,dpi=300)
        # this keeps the memory footprint under control
        plt.close()
        
    # you *cannot* have / in a file path!
    except:
        print('error w/save for:')
        print('-'.join((seg.P.name,seg.hwy,seg.Q.name)))
        print()
        plt.close()
    
    #time.sleep(2)
    




