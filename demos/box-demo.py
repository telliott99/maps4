'''
make a box using Shapely.geometry
and then use affinity.rotate to rotate it 
'''

import sys, os, subprocess, math
import matplotlib.pyplot as plt

import update_path
import utils.ufile as fh

from shapely import affinity
from shapely.geometry import box

def make_box(dx,dy,w=1):
    d = math.sqrt(dx**2 + dy**2)
    #      minx,miny,maxx,maxy
    return box(0,-w/2,d,w/2)
    
b = make_box(2,1)
r = affinity.rotate(b,30,(0,0))

fig, ax = plt.subplots()

# note:  
# ax.plot(b.exterior.xy) doesn't work
x,y = b.exterior.xy
ax.plot(x,y)
x,y = r.exterior.xy
ax.plot(x,y)

ax.scatter(0,0,color='black',zorder=2)

# ---------------------------------

script_name = fh.get_name(__file__)
fn = script_name + '.png'
path = fh.demo_img_path + fn
plt.savefig(path)

cmd = ['open','-a','Preview', path]
subprocess.run(cmd)
