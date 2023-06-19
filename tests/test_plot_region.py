import sys,os,subprocess

import geopandas as gpd
import matplotlib.pyplot as plt
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh
       
def test(
    region='western_states',
    stateL=None):
    
    func_name = fh.get_name(__file__)
    print(func_name)

    if not region and stateL is None:
        fh.sorry(func_name + ' needs arguments')
    
    SZ=(7,7)
    fig,ax = plt.subplots(figsize=(SZ)) 

    #gdf = gh.make_empty_geodataframe()
    ph.plot_region(ax=ax,
        region=region,
        stateL=stateL)
       
    ph.save_and_show_file(
        fig,func_name,scrub=True)

if __name__ == "__main__":
    test()