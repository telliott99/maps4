import sys,os
import geopandas as gpd

import matplotlib as mpl
import matplotlib.pyplot as plt
from shapely.geometry import Point

func_name = __file__.split('.')[0]

fn = 'gz_2010_us_040_00_5m'
HOME = os.path.expanduser('~')
path = HOME + '/data/' + fn
gdf = gpd.read_file(path)
# --------------------------------

sel = gdf['STATE'] == '15'
gdf = gdf[sel]
exp = gdf.explode(index_parts=True)
# --------------------------------
print(exp['geometry'].type.head())

fig,ax = plt.subplots()
exp.plot(ax=ax,cmap='tab20')

# listed by order in the MultiPolygon
L = ["Hawaii", "",     # go silent for Ford Island
     "Ni'ihau","Kauai",
     "Molokai","Kaho'olawe",
     "Maui","Lanai","O'ahu"]
     
def g(name,t):
    match name:
        case "O'ahu":
            return t[0],t[1]+0.4
        case "Kauai":
            return t[0],t[1]-0.4
        case "Ni'ihau":
            return t[0],t[1]-0.4
        case "Molokai":
            return t[0]+0.2,t[1]+0.2
        case "Maui":
            return t[0]+0.6,t[1]
        case "Ford Island":
            return t[0]-0.3,t[1]-0.4
        case "Lanai":
            return t[0]-0.4,t[1]-0.1
        case "Hawaii":
            return t[0]-0.9,t[1]
        case "Kaho'olawe":
            return t[0]-0.65, t[1]-0.1
    return t

def f(row):
    # weirdly the row.name here is not an int
    # but a tuple like (11,0), (11,1) ..
    print(row.name)
    i = row.name[1]
    
    xy = g(L[i],
        list(row.geometry.centroid.coords[0]))
    name = L[i]
    
    if name == 'Hawaii':
        name = "Hawai'i"
    ax.annotate(
        text=name,
        xy=xy,
        ha='center')
    
exp.apply(f,axis=1)
fn = func_name + '.png'
plt.savefig(fn,dpi=1200)

#-----------------------

D = {"Hawaii":[-155.519783,19.625055], 
     "Kaho'olawe":[-156.607857,20.550829],
     "Kauai":[-159.567160,22.017814],
     "Lanai":[-156.930387,20.834303],
     "Maui":[-156.279557,20.758340],
     "Molokai":[-156.986996,21.134644],
     "Ni'ihau":[-160.148047,21.904692],
     "O'ahu":[-157.968125,21.488976],
     "Ford Island":[-157.959627,21.363596]}
     
print('-'*30)

def h(row):
    i = row.name[1]
    poly = row['geometry']
    for k in D:
        if poly.contains(Point(D[k])):
            print(i,k)

exp.apply(h,axis=1)


    
