import sys, os, subprocess, math

import update_path
import utils.ubox as bh

#from shapely import affinity
#from shapely.geometry import Point, LineString

L = [(1,0),(2,1),(1,1),(1,2),
     (0,1),(-1,2),(-1,1),(-2,1),
     (-1,0),
     (-2,-1,),(-1,-1),(-1,-2),
     (0,-1),(1,-2),(1,-1),(2,-1)]

for x,y in L:
    o = bh.geto(0,0,x,y)
    try:
        t = '%5.2f %5.2f %7.2f' % (x,y,o)
    except:
        t = '%5.2f %5.2f' % (x,y)
    print(t)
    
'''
> p3 test_geto.py 
 1.00  0.00    0.00
 2.00  1.00   26.57
 1.00  1.00   45.00
 1.00  2.00   63.43
 0.00  1.00   90.00
-1.00  2.00  116.57
-1.00  1.00  135.00
-2.00  1.00  153.43
-1.00  0.00  180.00
-2.00 -1.00 -153.43
-1.00 -1.00 -135.00
-1.00 -2.00 -116.57
 0.00 -1.00  -90.00
 1.00 -2.00  -63.43
 1.00 -1.00  -45.00
 2.00 -1.00  -26.57
> 
'''