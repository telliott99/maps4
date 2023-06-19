import sys,os,subprocess
import geopandas as gpd

import matplotlib as mpl
import matplotlib.pyplot as plt
# from shapely.geometry import Point

func_name = __file__.split('.')[0]

fn = 'gz_2010_us_040_00_5m'
HOME = os.path.expanduser('~')
path = HOME + '/data/' + fn
gdf = gpd.read_file(path)

# --------------------------------

sel = gdf['STATE'] == '02'
gdf = gdf[sel]

print(gdf.columns)
print(list(set(list(gdf['GEO_ID']))))

sys.exit()

mp = gdf['geometry'].iloc[0]  # len is 1
pL = mp.geoms
print(len(pL))  # 118 !


fig,ax = plt.subplots()

albers = gdf.to_crs(w'ESRI:102003')
albers.boundary.plot(ax=ax)

# --------------------------------
fn = func_name + '.png'
plt.savefig(fn,dpi=1200)
subprocess.run(['open','-a','Preview',fn])



    
