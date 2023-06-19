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

func_name = 'route-plot'

fn = 'sw-adventure.txt'

try:
    arg = sys.argv[1]
    if arg.startswith('sw'):
        fn = 'sw-adventure.txt'
    elif arg.startswith('co'):
        fn = 'co-adventure.txt'
    elif arg.startswith('cc'):
        fn = 'cc-west.txt'
      
except IndexError:
    pass

# edit for save
saving = False

path = fh.local_data_path
data = fh.read_file(path+fn)

# not split yet
data = data.strip().split('\n\n')
data = [e for e in data if not e.startswith('#')]

# ---------------------------------

SZ=(7,7)
fig,ax = plt.subplots(figsize=(SZ)) 
          
ph.plot_region(ax,
    region='western_states')
    
stateL = ['AZ','UT','CO',
          'NM','OR','ID','WY']
pL = list()

# rather than concat, save in a dict
D = dict()
outlineD = dict()

# ---------------------------------

f1 = gh.get_geodataframe_for_state_roads
f2 = gh.get_geodataframe_for_stateL

def gdf_for_route_str(route_str):

    # a list of segment objs
    rL = fmt.parse_route_str(route_str)
    #print(route_str)
    
    names = list()
    pL = list()
    X = list()
    Y = list()
    
    for seg in rL:
        # allow multiple states for interstate search
        state = seg.stateL[0]
        
        if not state in D:        
            D[state] = f1(state)
            
        if not state in outlineD:
            outlineD[state] = f2([state])
    
        target = seg.hwy
        P,Q = seg.P, seg.Q
        
        # only plot if marked
        
        if P.name.startswith('-'):
            X.append(P.lon)
            Y.append(P.lat)
            # strip the mark
            names.append(P.name[1:])
        
        gdf = D[state]
        
        # apparently, some state roads
        # have extraneous data!
        # filter here
        # gdf = gdf.clip(outlineD[seg.state])
        
        # non-strict search
        target = seg.hwy.split()[-1]
        sub = sh.search(gdf,target,strict=False)

        poly = gpd.GeoDataFrame([1], 
            geometry=[seg.box],crs=gdf.crs)
        clp = sub.clip(poly)
        
        if clp.empty:
            print('problem with')
            print(seg)
            print()
            continue
            
        pL.append(clp)
        
    if Q.name.startswith('-'):
        X.append(rL[-1].Q.lon)
        Y.append(rL[-1].Q.lat)
        names.append(Q.name[1:])
    
    return pd.concat(pL),X,Y,names
    
def fix_cc_special(ax):
    x1,y1 = -110.837448,44.457214
    x2,y2 = x1+0.3, y1-0.1
    x3,y3 = -109.528467,40.455896  # Vernal, UT
    x4,y4 = -109.050836,40.273204  # (UT-CO)
    ax.plot((x1,x2),(y1,y2),color='red',zorder=1)
    ax.plot((x3,x4),(y3,y4),color='red',zorder=1)
    
# this would have to be a lot smarter to look good
# not implemented
def annotate_points(ax,X,Y):
    for i,(x,y) in enumerate(zip(X,Y)):
        label = "{:2d}".format(i+1)
        plt.annotate(label,         # text
                     (x,y),         # coordinates
                     textcoords="offset points",
                     xytext=(0,10), # offset distance
                     ha='center')   # horizontal alignment

# ---------------------------------

X = list()
Y = list()
pL = list()

for route_str in data:
    sub,xL,yL,names = gdf_for_route_str(route_str)   
    X.extend(xL)
    Y.extend(yL)
    ph.plot_gdf(ax,sub,color='red',linewidth=2)
    pL.append(sub)
    
ph.plot_points(ax,X,Y,SZ=20)
#annotate_points(ax,X,Y)

if fn.startswith('cc'):
    fix_cc_special(ax)

ph.save_and_show_file(fig,func_name,scrub=False)

# save the route to a shapefile
if saving:
    ofn = fn.split('.')[0] + '.shp.zip'
    path = fh.local_data_path + ofn
    fh.save_geodataframe_to_shapefile(pd.concat(pL),path)







