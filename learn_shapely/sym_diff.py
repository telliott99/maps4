'''
periodic reminder:  do not re-use names!
this script had bee named shapely.py
broke geopandas for other scripts in same folder
'''


import sys,subprocess
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import box, Polygon

func_name = __file__.split('.')[0]

# minx,miny,maxx,maxy
b1 = box(1,1,4,4)
p1 = gpd.GeoSeries(Polygon(b1))
b2 = box(2,2,5,5)
p2 = gpd.GeoSeries(Polygon(b2))

# intersection, union
# difference, symmetrical difference

fig,axes = plt.subplots(3,2)

p1.plot(ax=axes[0][0],color='blue')
p2.plot(ax=axes[0][1],color='orange')

u = p1.union(p2)
u.plot(ax=axes[1][0],color='cyan')

i = p1.intersection(p2)
i.plot(ax=axes[1][1],color='cyan')

d =  p1.difference(p2)
d.plot(ax=axes[2][0],color='cyan')

sd = p1.symmetric_difference(p2)
sd.plot(ax=axes[2][1],color='cyan')

lim = [0,6]

for ax in axes[0]:
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect('equal')

for ax in axes[1]:
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect('equal')

for ax in axes[2]:
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect('equal')

fig.tight_layout()
fn = func_name + '.png'
plt.savefig(fn)
subprocess.run(['open','-a','Preview',fn])