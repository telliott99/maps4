'''
Phoenix, AZ [-112.074037,33.448377]
I-10
Tucson, AZ [-110.926479,32.221743]
'''

import sys, math, subprocess
from shapely import affinity
from shapely.geometry import box

# --------------------------------

# make it *wide*
def make_box(x1,y1,x2,y2,w=None):
    dx,dy = x2-x1,y2-y1
    d = math.sqrt(dx**2 + dy**2)
    if w is None:
        w = d
              # minx,miny,maxx,maxy
    return box(x1,y1-w/2,x1+d,y1+w/2)

# --------------------------------

def geto(x1,y1,x2,y2):
    dx,dy = x2-x1,y2-y1
    
    if dx == 0 and dy == 0:
        fh.sorry('error in geto:  P == Q x=' + str(round(x1,2)))
        
    elif dx == 0 and dy > 0:
        return 90
        
    elif dx == 0 and dy < 0:
        return -90
    
    elif dy == 0 and dx > 0:
        return 0
            
    elif dy == 0 and dx < 0:
        return 180

    # from old math_helper.py
    m = dy/dx
    
    d = math.degrees(math.atan(m))
    
    # tricky
    # see test output at bottom
    
    #Q1  
    if dx > 0 and dy > 0:
        return d
      
    if dx < 0:
        #Q2
        if dy > 0:
            return d + 180
    
        #Q3  
        if dy < 0:
            return d - 180

    #Q4  
    if dx > 0 and dy < 0:
        return d

def make_box_for_points(P,Q):
    #print('make_box_for_points')
    x1,y1 = P.lon,P.lat
    x2,y2 = Q.lon,Q.lat
    box = make_box(x1,y1,x2,y2)
    
    o = geto(x1,y1,x2,y2)
        
    # arg2 is angle in degrees ccw from pos x-axis
    rot = affinity.rotate(box,o,(x1,y1))
    return o,rot


'''
standard trig version
going ccw from positive x-axis
negative for quadrants Q3 and Q4

> p3 tests/test_geto.py
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
