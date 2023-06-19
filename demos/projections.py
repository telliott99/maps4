import sys,os,subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

script_name = __file__.split('.')[0]

fn = 'gz_2010_us_040_00_5m'

HOME = os.path.expanduser('~')
path = HOME + '/data/' + fn
gdf = gpd.read_file(path)

# filter for lower48

def f(e):
    return not e in ['02','15','72']
  
sel = [f(e) for e in gdf['STATE']]
outline = gdf[sel]

# print(outline.crs)   # EPSG:4269

# ----------------------------------

eckert = outline.to_crs('ESRI:54012')
# Albers contiguous USA
albers = outline.to_crs('ESRI:102003')

# ----------------------------------

fig,axes = plt.subplots(1,3)
outline.boundary.plot(ax=axes[0])
axes[0].set_title('NAD83')

albers.boundary.plot(ax=axes[1])
axes[1].set_title('Albers')

eckert.boundary.plot(ax=axes[2])
axes[2].set_title('eckert')

fig.tight_layout()

ofn = script_name + '.png'
plt.savefig(ofn,dpi=300)
subprocess.run(['open','-a','Preview',ofn])