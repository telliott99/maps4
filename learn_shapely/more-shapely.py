import sys,subprocess
import matplotlib.pyplot as plt
import geopandas as gpd

from shapely.geometry import Point
from shapely.geometry import LineString, Polygon

script_name = __file__.split('.')[0]

#-----------------------

p = Point([0,0])
q = Point([3,1.5])
ls = LineString([p,q])
poly = Polygon([[1,-1],[1,1],[-1,1],[-1,-1],[1,-1]])
gs = gpd.GeoSeries([p,q,ls,poly])

# we need to save ax for subsequence calls to plt
ax = gs.boundary.plot()

ax.plot((p.x,q.x),(p.y,q.y))

print(poly.contains(ls))    # False
print(poly.crosses(ls))     # True
r = poly.intersection(ls)

X,Y = r.xy
X,Y = list(X), list(Y)
ax.scatter(X,Y,color='red',zorder=2)
ax.plot(X,Y,color='red')

#-----------------------

fn = script_name + '.png'
plt.savefig(fn)
subprocess.run(['open','-a','Preview',fn])