import sys,os,subprocess
import geopandas as gpd
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh

default_route_str = '''
Scottsdale,AZ  [-111.890094,33.493274]
State Rte 101
Deer Valley,AZ [-112.113341,33.671126]
I- 17
Camp Verde,AZ  [-111.884452,34.577377]
State Rte 260
Cottonwood,AZ  [-112.002727,34.721418]
State Rte 89A
Jerome,AZ      [-112.114832,34.747834]
State Rte 89A
Sedona,AZ      [-111.759061,34.871682]
'''

def test(s=None):

    func_name = fh.get_name(__file__)
    print(func_name)

    if not s:
        s = default_route_str
    crs = "EPSG:4269"
    
    # will contain a list of Segment objs
    route = fmt.parse_route_str(s.strip())
    gdf = gh.make_geodataframe_for_route(
        route,crs)
    
    ofn = 'test_save.shp.zip'
    path = fh.local_data_path + ofn
    fh.save_geodataframe_to_shapefile(gdf,path)
    
    # try reading what we just wrote
    df = gpd.read_file(path)
    print(df['City'])

if __name__ == "__main__":
    test()
