import sys,os,subprocess

import geopandas as gpd
import matplotlib.pyplot as plt
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh
       
t = '''
Sedona, AZ [-111.759061,34.871682]
Page, AZ [-111.489860,36.895829]
Tonopah, AZ [-112.937020,33.497503]
Tucson, AZ  [-110.980169,32.221358]
'''
   
def test(s=None):
    func_name = fh.get_name(__file__)
    print(func_name)

    
    if s is None:
        s = t
        
    X = list()
    Y = list()
    for line in s.strip().split('\n'):
        p = fmt.parse_point_str(line)
        X.append(p.lon)
        Y.append(p.lat)

    SZ=(7,7)
    fig,ax = plt.subplots(figsize=(SZ)) 

    ph.plot_region(ax,stateL = ['AZ'])
    ph.plot_points(ax,X,Y)
    
    ph.save_and_show_file(fig,func_name,scrub=True)

if __name__ == "__main__":
    test()