import sys, os, subprocess
import geopandas as gpd
import matplotlib.pyplot as plt
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh


# get multiple roads for a single state
def test(
    state='CO',target_str='24,40,50'):
    
    func_name = fh.get_name(__file__)
    print(func_name)
    
    SZ=(7,7)
    fig,ax = plt.subplots(figsize=(SZ))

    targetL = target_str.split(',')
    roads = gh.get_geodataframe_for_state_roads(state)
    
    # gdf contains the concatenated results, a single df
    gdf = sh.multi_road_search(
        roads,targetL,strict=False)
    
    ph.plot_region(ax,stateL=[state])
    ph.plot_gdf(ax,gdf,color='red')
    
    fmt.pprint(gdf,func_name)
    ph.save_and_show_file(fig,func_name,scrub=True)
                        
def test_all():
    test_search()
    test_multi_road_search()
    
if __name__ == "__main__":
    test()
