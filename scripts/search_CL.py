# want to modify this to somehow label the different results

import sys

import matplotlib.pyplot as plt
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh

try:
    state = sys.argv[1]
    targetL = sys.argv[2].split(',')
except:
    print('example usage:')
    print('python3 search_CL.py CO 40,50,160')
    sys.exit()
    
# --------------------------------
script_name = 'cl_search'
strict = len(sys.argv) > 3

gdf = gh.get_geodataframe_for_state_roads(state)
sub = sh.multi_road_search(gdf,targetL,strict=False)
L = list(set(list(sub['FULLNAME'])))
print('\n'.join(L))

SZ=(7,7)
fig,ax = plt.subplots(figsize=(SZ))

ph.plot_region(ax,stateL=[state])
ph.plot_gdf(ax,gdf,color='lightgray')
ph.plot_gdf(ax,sub,color='red')

ph.save_and_show_file(fig,script_name,scrub=True)
