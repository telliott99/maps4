'''
like box-demo1.py but using utils/box_helper.py
make a box using Shapely.geometry
and then use affinity.rotate to rotate it 
'''

import sys, os, subprocess, math
import matplotlib.pyplot as plt

import update_path
import utils.ufile as fh

from shapely import affinity
from shapely.geometry import box

import utils.ubox as bh

'''
Phoenix [-112.074037,33.448377]
(AZ) I- 10
Tucson [-110.926479,32.221743]
'''

t = '''
(WY-UT) [-109.430980,41.000000]
US Hwy 191
Vernal, UT [-109.528467,40.455896]
'''

u = '''
Vernal, UT [-109.528467,40.455896]
US Hwy 40
(UT-CO) [-109.050836,40.273204]
'''

def do_plots(b,r,X,Y):
    fig, ax = plt.subplots()
    x, y = b.exterior.xy
    ax.plot(x,y)
    x, y = r.exterior.xy
    ax.plot(x,y)
    ax.scatter(X,Y)
    ax.set_aspect('equal')

x1,y1 = -109.528467,40.455896
x2,y2 = -109.050836,40.273204
b = bh.make_box(x1,y1,x2,y2)
o = bh.geto(x1,y1,x2,y2)
        
# rotate around P
r = affinity.rotate(b,o,(x1,y1))

X,Y = (x1,x2),(y1,y2)
do_plots(b,r,X,Y)

# ---------------------------------

script_name = fh.get_name(__file__)
fn = script_name + '.png'
path = fh.demo_img_path + fn
plt.savefig(path)

cmd = ['open','-a','Preview', path]
subprocess.run(cmd)
