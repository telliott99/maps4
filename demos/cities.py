'''
provde a file name with cities
look up data for population, longitude and latitude
the two data sources have the same size, probably identical
'''

import sys, json
from operator import itemgetter as get
from utils.ustates import state_to_abbrev

# two files I got from the web:
fn1 = 'us-cities-top-1k.csv'
fn2 = 'cities.json'

path = '/Users/telliott/data/'

# we can read csv data ourselves or use pandas
import pandas as pd

def get_dict1():
    df = pd.read_csv(path+fn1)
    nrows = df.shape[0]
    pL = list()
    
    for i in range(nrows):
        e = df.iloc[i]
        city = e['City']
        state = e['State']
        abbrev = state_to_abbrev[state]
        pop = e['Population']
        lon = round(e['lon'],6)
        lat = round(e['lat'],6)
        pL.append((city+', '+abbrev,pop,lon,lat))
    
    # sort by pop
    pL = sorted(pL,key = get(1),reverse=True)
    # print(pL[-1])  # pop 36877
    
    D = dict()
    for loc,pop,lon,lat in pL:
        D[loc] = {'pop':pop,'lon':lon,'lat':lat}
    return D

# -----

def get_dict2():
    with open(path+fn2) as fh:
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
    pL = sorted(pL,key = get(1),reverse=True)
    D = dict()
    for loc,pop,lon,lat in pL:
        D[loc] = {'pop':pop,'lon':lon,'lat':lat}
    return D

def test():
    D1 = get_dict1()
    D2 = get_dict2()
    print(D1['Portland, OR'])
    print(D2['Portland, OR'])
    print(len(D1.keys()),len(D2.keys()))

#test()

def handle_file(fn):
    with open(fn) as fh:
        input = fh.read().strip().split('\n')
    pL = list()
    D = get_dict1()
    t = '%s [%3.6f,%3.6f]'
    for e in input:
        try:
            sD = D[e]
            lon,lat = sD['lon'],sD['lat']
            print(t % (e,lon,lat))
        except KeyError:
            print(e)
    
if __name__ == "__main__":
    fn = sys.argv[1]
    handle_file(fn)
