'''
preliminary analysis of roads by RTTYP
files are per-state
for usage see below
'''

import sys,os,subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

import update_path
import utils.ustates as us

try:
    state = sys.argv[1]
except IndexError:
    print('usage:')
    print('python3 analyze-roads.py <state>')

try:
    fips = us.abbrev_to_fips[state]
except:
    print('sorry, there is a problem with %s' % state)
    sys.exit()

def get_data():
    fn = 'tl_2020_%s_prisecroads.zip' % fips
    HOME = os.path.expanduser('~')
    path = HOME + '/data/prisecroads/' + fn
    return gpd.read_file(path)

def analyze(gdf):
    print(gdf.shape)
    #print(gdf.columns)
    D = dict()
    for k in 'UCOSIM':
        sel = gdf['RTTYP'] == k
        sub = gdf[sel]
        D[k] = sub.shape[0]
    return D

gdf = get_data()
D = analyze(gdf)
for k in D:
    print(k, D[k])

'''
for i in range(gdf.shape[0]):
    row = gdf.iloc[i]
    if row['RTTYP'] == 'M':
        print(row['FULLNAME'])
'''
    
'''
FIPS 04 is Arizona
C County
I Interstate
M Common Name
O Other
S State recognized
U U.S.

> p3 analyze-roads.py AZ
(1320, 5)
U 168
C 20
O 11
S 431
I 71
M 619
>
'''