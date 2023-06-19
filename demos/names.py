import sys
import subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh

script_name = fh.get_name(__file__)

try:
    state = sys.argv[1]
    targetL = sys.argv[2].split(',')
except IndexError:
    print('usage:')
    print('python3 names.py <state> <highway_list>')
    print('python3 names.py AZ 89A,180')
    sys.exit()

gdf = gh.get_geodataframe_for_state_roads(state)
sub = sh.multi_road_search(gdf,targetL,strict=False)

fig, ax = plt.subplots(figsize=(10,10))

ph.plot_region(ax,stateL=['UT'])
ph.plot_gdf(ax,sub,color='red')

ph.save_and_show_file(fig,script_name,scrub=True)

L = list(set(list(sub['FULLNAME'])))
for e in L:
    print(e)
