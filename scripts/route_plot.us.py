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

func_name = fh.get_name(__file__)

fn = 'cc-all.txt'

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
    region='us48')
    
stateL = ['OR','ID','MT','WY',
          'UT','CO','NM',
          'TX','LA','MS','AL',
          'TN','KY','NC','SC']

pL = list()

# rather than concat, save in a dict
D = dict()
outlineD = dict()

f1 = gh.get_geodataframe_for_state_roads
f2 = gh.get_geodataframe_for_stateL

for state in stateL:
    D[state] = f1(state)
    outlineD[state] = f2([state])
    
# ---------------------------------


def gdf_for_route_str(route_str):

    # a list of segment objs
    rL = fmt.parse_route_str(route_str)
    #print(route_str)
    
    names = list()
    pL = list()
    X = list()
    Y = list()
    
    for seg in rL:
        # allow multiple states 
        # to accomodate interstate search
        state = seg.stateL[0]
    
        target = seg.hwy
        P,Q = seg.P, seg.Q
        
        # no point for border crossings
        if P.name.startswith('('):
            pass
        else:
            X.append(P.lon)
            Y.append(P.lat)
            names.append(P.name)
        
        gdf = D[state]        
        # non-strict search
        
        target = seg.hwy
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
        
    if Q.name.startswith('('):
        pass
    else:
        X.append(rL[-1].Q.lon)
        Y.append(rL[-1].Q.lat)
        names.append(Q.name)
    
    return pd.concat(pL),X,Y,names

# second half 
def fix_cc_special(ax):
    x1,y1 = -87.475643,35.435985    # 
    x2,y2 = -86.789402,36.156301     # Nashville
    ax.plot((x1,x2),(y1,y2),color='red',zorder=1)
    
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
    
#ph.plot_points(ax,X,Y,SZ=20)

fix_cc_special(ax)

ph.save_and_show_file(fig,
    func_name,dpi=600,scrub=False)

# save the route to a shapefile
if saving:
    ofn = fn.split('.')[0] + '.shp.zip'
    path = fh.local_data_path + ofn
    fh.save_geodataframe_to_shapefile(pd.concat(pL),path)







