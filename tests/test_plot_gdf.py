import sys,os,subprocess

import geopandas as gpd
import matplotlib.pyplot as plt
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh
       
def test():
    func_name = fh.get_name(__file__)
    print(func_name)


    gdf = gh.get_geodataframe_for_state_roads('AZ')
    target = 'I- 10'
    sub = sh.search(gdf,target,strict=True)
    
    SZ=(7,7)
    fig,ax = plt.subplots(figsize=(SZ)) 

    # we need some outline
    # set up by hand here
    ph.plot_region(ax,
        region=None,
        stateL=['AZ'])
    
    ph.plot_gdf(ax,sub)
    
    ph.plot_points(ax,[-112.937020,-110.980169],
                   [  33.497503,  32.221358])

    ph.save_and_show_file(fig,func_name,scrub=True)

if __name__ == "__main__":
    test()