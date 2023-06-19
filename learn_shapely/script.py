import sys,os,subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

func_name = __file__.split('.')[0]

fn = 'gz_2010_us_040_00_5m'

HOME = os.path.expanduser('~')
path = HOME + '/data/' + fn
gdf = gpd.read_file(path)

sel = gdf['STATE'] == '15'
gdf = gdf[sel]
print(gdf.shape)  # (1,6)  # df w/a single row

# gdf['geometry'] is its "active" geometry
gm = gdf['geometry']
print(gm.shape)   # (1,)
print(type(gm))

sys.exit()

# gm can be subscripted
# mp is a MultiPolygon
mp =gm.iloc[0]

# geos is a shapely.GeometrySequence
geos = mp.geoms
print(len(geos))   # 9

# it can be subscripted
# p is a shapely.geometry.polygon.Polygon
poly = geos[0]

# exterior, interiors which are LinearRing
ext = poly.exterior
print(len(poly.interiors))  # 0

X,Y = ext.coords.xy
X = X.tolist()
print(len(X))      # 230

for p in geos:
    print('%3.5f' % p.area)
    print(p.area)

'''
0.89870
0.00001
0.01629
0.12611
0.05853
0.00995
0.16353
0.03155
0.13710
>
'''

