import sys,os,subprocess,time
from operator import itemgetter
import json

from utils.ustates import state_to_abbrev

'''
# the current working directory could be project
# but it could also be project/scripts

# having headaches with relative paths so
# since we run *either*
# on Dropbox or on Desktop
'''

HOME = os.path.expanduser('~')
DBOX = HOME + '/Library/CloudStorage/Dropbox/'
DESK = HOME + '/Desktop/'

# this (does) break if the project is renamed!
# alternatively, we could use __file__

# could try something from this
'''
print(__file__)
print(os.path.relpath(DBOX, __file__))
sys.exit()
'''

if 'Dropbox' in sys.path[0]:
    PROJ_ROOT = DBOX + 'maps/'
else:
    PROJ_ROOT = DESK + 'maps/'

data_path =         HOME +'/' + 'data/'
prisecroads_path =  data_path + 'prisecroads/'

local_data_path =   PROJ_ROOT + 'data/'
demo_img_path =     PROJ_ROOT + 'figs-demos/'
test_img_path =     PROJ_ROOT + 'figs-tests/'

def get_name(p):
    n = os.path.split(p)[-1]
    return n.split('.')[0]

def sorry(msg):
    print(msg)
    sys.exit()

# generate unique timestamps 
# with millisecond resolution

def get_timestamp():
    t = time.time() * 100
    whole = str(int(t))
    return '-' + whole[-6:]

# do not assume that caller wants it split
def read_file(path):
    with open(path) as fh:
        data = fh.read()
    return data

# ---------------------------------

def get_fips_dict():
    D = dict()
    path = data_path + 'fips.txt'
    data = read_file(path)
    data = data.strip().split('\n')
    for item in data:
        abbrev,fips = item.strip().split()
        D[abbrev] = fips
    return D
    
def get_rev_dict(D):
    rD = dict()
    for k in D:
        rD[D[k]] = k
    return rD

# we're using the json version from data/cities.json
def get_city_loc_dict():
    with open(data_path+'cities.json') as fh:
        data = json.load(fh)
    pL = list()
    
    for e in data:
        city = e['city']
        state = e['state']
        abbrev = state_to_abbrev[state]
        pop = int(e['population'])
        lon = round(e['longitude'],6)
        lat = round(e['latitude'],6)
        pL.append((city+', '+abbrev,pop,lon,lat))
        
    pL = sorted(pL,key = itemgetter(1),reverse=True)
    D = dict()
    for loc,pop,lon,lat in pL:
        D[loc] = {'pop':pop,'lon':lon,'lat':lat}
    return D
 
fipsD = get_fips_dict()
rev_fipsD = get_rev_dict(fipsD)

stateL = sorted(list(fipsD.keys()))

cityD = get_city_loc_dict()

# ---------------------------------

fn = 'gz_2010_us_040_00_5m'
us_states_data_path = data_path + fn

fn = 'tl_2019_us_primaryroads'
priroads_data_path = data_path + fn


'''
# includes all 50 states + PR
def get_geodata_filepath_for_us():
    fn = 'gz_2010_us_040_00_5m'
    return data_path + fn
'''

# already validated

def get_geodata_filepath_for_region(region):
    if region == 'us':
        return us_states_data_path
        
    fp = (data_path + '%s.shp.zip') % region
    if not os.path.isfile(fp):
        sorry('file not found: ' + fp)
    return fp

def get_geodata_filepath_for_road_data(state):
    template = 'tl_2020_%s_prisecroads.zip'
    fipsD = get_fips_dict()
    fn = template % fipsD[state]
    return prisecroads_path + fn

'''
def get_geodata_filepath_for_interstates():
    fn = 'tl_2019_us_primaryroads'
    return data_path + fn
'''

def get_route_info(name):
    if name == 'sw':
        fn = 'sw-adventure.txt'        
    elif name == 'cc':
        fn = 'cc-adventure.txt'
    return read_file(local_data_path + fn)
        
def save_geodataframe_to_shapefile(gdf,path):
    gdf.to_file(
        filename = path,
        driver='ESRI Shapefile')
    


