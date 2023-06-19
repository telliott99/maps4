import sys
import geopandas as gpd
import pandas as pd

import utils.ufile as fh
import utils.ufmt as fmt

# the current working directory is
# determined by the path to whoever imports us
# it could be project
# but it could also be project/scripts

# --------------------------------

# this df will not contain highway data
# just city names, lon and lat
# it's a toy, used to test saving shapefiles

# A route is a list of segments
# Each segment has P,Q,state,hwy

def make_geodataframe_for_route(route,crs):
    names = list()
    X = list()
    Y = list()
    
    # successive segments, each Q is the next P
    # except the last
    
    for seg in route:
        names.append(seg.P.name)
        X.append(seg.P.lon)
        Y.append(seg.P.lat)
    
    last_seg = route[-1]
    names.append(last_seg.Q.name)
    X.append(last_seg.Q.lon)
    Y.append(last_seg.Q.lat)

    D = { 'City': names,
          'Longitude': X,
          'Latitude': Y }
          
    df = pd.DataFrame(D)   
     
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(
            df.Longitude, df.Latitude), 
        crs=crs)
    return gdf
    
# --------------------------------

def get_geodataframe_for_region(region):
    fn = fh.get_geodata_filepath_for_region(region)
    return gpd.read_file(fn)
    return get_geodataframe_for_us()

# we *will* handle outline data for multiple states
def get_geodataframe_for_stateL(stateL):
    gdf = get_geodataframe_for_us48()
    D = fh.fipsD
    stateL = [D[e] for e in stateL]
    def filter(s):
        return s in stateL
    sel = [filter(s) for s in list(gdf['STATE'])]
    return gdf[sel]
    
def get_geodataframe_for_us48():
    fn = fh.us_states_data_path
    return gpd.read_file(fn)

def get_geodataframe_for_us48():
    fn = fh.us_states_data_path
    gdf = gpd.read_file(fn)
    def filter(e):
        return not (e in ['02','15','72'])
    sel = [filter(e) for e in list(gdf['STATE'])]
    df = gdf[sel]
    return df

# caller should handle multiple states and then concat
def get_geodataframe_for_state_roads(state):
    fn = fh.get_geodata_filepath_for_road_data(state)
    gdf = gpd.read_file(fn)
    return gdf

def get_geodataframe_for_interstates():
    path = fh.priroads_data_path
    return gpd.read_file(path)

# --------------------------------

# empty GeoDataFrame

def make_empty_geodataframe():
    df = gpd.GeoDataFrame(columns=[
        'id', 'distance', 'feature'], 
        geometry='feature')
    return df
    
# --------------------------------

# clip "dissolves geometry" 
# old, we use a different function now

'''
def clip(df,limits):
    xmin,xmax,ymin,ymax = limits
    return df.cx[xmin:xmax, ymin:ymax]
'''

def names(df,COL='FULLNAME'):
    return sorted(list(set(list(df[COL]))))
