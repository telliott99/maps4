import sys,os
import utils.ubox as bh

sep = '\n'
sep2 = sep * 2

'''
Standardize nomenclature:

Point (an obj)
  has name, lon, lat  latter two as floats

Segment (an obj)
  has start P, end Q, state and hwy

  We will always break at a state line
  since the data source changes '
  and the highway name may also

Route 
  one days drive.  A list of segments,
  with or without the actual points.

Trip
  a list of routes.
'''

class Point:
    # a border point will have state == None
    def __init__(self,loc,state,lon,lat):
        self.name = loc
        # we use abbrevs as usual
        self.state = state  # may be None
        
        self.lon = float(lon)  # if lon is already a float
        self.lat = float(lat)  # it's a no-op
        
    def __repr__(self):
        if self.state is None:
            name = self.name
        else:
            name = self.name + ',' + self.state
        rest = '%3.6f %3.6f' % (self.lon,self.lat)
        return self.name.ljust(30) + rest

# to allow long internet routes
# relax restriction to have only a single state
def get_stateL(P,Q):
    if P.state is None:
        return [Q.state]
    elif Q.state is None:
        return [P.state]
    if P.state == Q.state:
        return [P.state]
    else:
        return [P.state,Q.state]

class Segment:
    def __init__(self,P,Q,hwy):
        self.P = P
        self.Q = Q
        
        # for convenience we allow interstates
        # to be like I-10
        # but gdf actually have I- 10
        
        if hwy[:2] == 'I-':
            if not hwy[2] == ' ':
                hwy = hwy[:2] + ' ' + hwy[2:]
        self.hwy = hwy
        self.stateL = get_stateL(P,Q)
        
        o,rot = bh.make_box_for_points(
            self.P,self.Q)
        self.o = o
        self.box = rot
        
    def __repr__(self):
        s = sep.join([
            str(self.P),
            self.hwy,
            str(self.Q),
            ','.join(self.stateL)])  
        return s
              
'''
one day's drive is a "chunk" of a trip
represented as a list of Segment objs
'''
    
# --------------------------------

def get_lines(s,nl=sep):
    return s.strip().split(sep)

def join_lines(L,nl=sep):
    return sep.join(L)
    
# --------------------------------

def pprint(df,func_name):
    results = list(set(list(df['FULLNAME'])))
    print(func_name + ':')
    results = sorted(list(set(list(df['FULLNAME']))))
    print(join_lines(results))

# --------------------------------

# receive an individual location as string
def parse_point_str(point_str):
    '''
    return one Point object from
    string of name,[lon,lat]
    '''
    func_name = 'parse_point_str'
    name, rest = point_str.strip().split('[')
    name = name.strip()
    assert rest[-1] == ']'
    rest = rest[:-1]
    lon,lat = rest.strip().split(',')
    
    if ',' in name:
        sL = name.split(',')
        city = sL[0].strip()
        state = sL[1].strip()
        return Point(city,state,lon,lat)
        
    else:
        state = None
        return Point(name,state,lon,lat)
        
# --------------------------------

def parse_segment_str(seg_str,verbose=False):
    sL = seg_str.strip().split('\n')
    P_str,hwy_str,Q_str = sL
    
    if verbose:
        print(P_str)
        print(Q_str)
        print()
    
    P = parse_point_str(P_str)
    Q = parse_point_str(Q_str)
    
    hwy = hwy_str.strip()
    return Segment(P,Q,hwy)
     

def parse_route_str(route_str):
    ''' 
    parse a route_str:  
    a string with point-hwy-point-hwy ..
    return a Segment obj for each point-hwy-point triplet
    '''
    
    lines = get_lines(route_str)
    rL = list()
    
    for i in range(0,len(lines)-2,2):
        P_str,hwy_str,Q_str = lines[i:i+3]
        P = parse_point_str(P_str)
        Q = parse_point_str(Q_str)
        
        hwy = hwy_str.strip()
        seg = Segment(P,Q,hwy)
        rL.append(seg)
    return rL

# --------------------------------

'''
One file may have a single route
or a whole trip, a list of routes

A route is a list of segments
A segment is P->Q w/hwy and state
'''

def read_trip_from_file(fn = None):
    if not fn:
        fn = 'sw-adventure.txt'
        
    if os.getcwd().split('/')[-1] == 'scripts':
        path = '../data/' + fn
    else:
        path = 'data/' + fn
        
    with open(path) as fh:
        s = fh.read()
        
    data = s.strip().split(sep2)
    data = [e for e in data if not e.startswith('#')]
        
    # a Trip is a list of Routes
    # a Route is a alist of Segments
    # each Segment is like one hop, from P to Q
    
    trip = list()
    for route_str in data:
        route = parse_route_str(route_str)
        trip.append(route)
    return trip

def test_format_helper():
    trip = read_trip_from_file()
    pL = list()   
    
    # each trip is a list of routes
    # routes composed of Segment objs
    # i and j just help with printing
    for i,route in enumerate(trip):
        for j,seg in enumerate(route):
            pL.append(seg.P)
            pL.append(seg.hwy)
            if j == len(route) - 1:
                pL.append(seg.Q)
        if not i == len(trip) - 1:
            pL.append('-'*25)
    for line in pL:
        print(line)

if __name__ == "__main__":
    test_format_helper() 
        
    