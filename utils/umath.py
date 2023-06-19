import sys
from math import cos, radians, atan, degrees

# formatting does not belong here
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def geto(dx,dy):
    if dx == 0 and dy == 0:
        return 0   # correct solution?
    
    if dx == 0:
        if dy > 0:
            return 0
        else:
            return 180
    if dy == 0:
        if dx > 0:
            return 90
        else:
            return 270
        
    m = dy/dx    
    # sign of m doesn't care *which* of dx,dy is negative
        
    # Q1
    if dx > 0 and dy > 0:
        at = degrees(atan(m))
        return  90 - at

    # Q2, make the slope positive
    # this makes it a mirror image of Q1
    if dx < 0 and dy > 0:
        m *= -1
        at = degrees(atan(m))
        return 270 + at
        
    # Q3
    if dx < 0 and dy < 0:
        at = degrees(atan(m))
        return 270 - at
        
    # Q4, slope is negative, but we work with pos number
    if dx > 0 and dy < 0:
        m *= -1
        at = degrees(atan(m))
        return  90 + at

# P,Q are points
# result is the orientation of the vector P->Q 
# in compass degrees
def get_limits(P,Q):
    xmax = P.x
    xmin = Q.x
    if xmin > xmax:
        xmin,xmax = xmax,xmin

    ymax = P.y
    ymin = Q.y
    if ymin > ymax:
        ymin,ymax = ymax,ymin
    
    dx = P.x - Q.x
    dy = P.y - Q.y
    o = geto(dx,dy)
    
    if o >= 0 and o <= 45: 
        which = 'ylim'
    elif o >= 315 and o <= 360: 
        which = 'ylim'
    elif o >= 135 and o <= 225: 
        which = 'ylim'
    else:
        which = 'xlim'
    
    pad = 1
    if which == 'xlim':     
        return (xmin,ymin-pad,xmax,ymax+pad)
    return (xmin-pad,ymin,xmax+pad,ymax)
    
