import sys,os,subprocess

import geopandas as gpd
import matplotlib.pyplot as plt
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh

s = '''
Phoenix, AZ [-112.074037,33.448377]
I- 10
Tucson, AZ   [-110.926479,32.221743]
'''

t = '''
Vernal, UT [-109.528467,40.455896]
US Hwy 40
(UT-CO) [-109.050836,40.273204]
'''

def test():
    func_name = fh.get_name(__file__)
    print(func_name)

    seg = fmt.parse_segment_str(s)
        
    SZ=(7,7)
    fig,ax = plt.subplots(figsize=(SZ)) 

    ph.plot_region(ax,
        region=None,
        stateL=seg.stateL)
    
    # for now, we will ignore the case with 2 states
    gdf = gh.get_geodataframe_for_state_roads(
              seg.stateL[0])
    target = seg.hwy
    sub = sh.search(gdf,target,strict=True)
    ph.plot_gdf(ax,sub)
    
    poly = gpd.GeoDataFrame([1], 
        geometry=[seg.box], 
        crs=gdf.crs)
        
    ph.plot_gdf(ax,sub.clip(poly),color='red')
    
    P = seg.P
    Q = seg.Q

    ph.plot_points(ax,[P.lon,Q.lon],[P.lat,Q.lat])

    ph.save_and_show_file(fig,func_name,scrub=True)

if __name__ == "__main__":
    test()
    