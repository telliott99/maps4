import sys,os,subprocess
import geopandas as gpd
import matplotlib.pyplot as plt

def lower48(gdf):
    # filter for lower48
    def f(e):
        return not e in ['02','15','72']   
    sel = [f(e) for e in gdf['STATE']]
    return gdf[sel]

def get_data():
    fn = 'gz_2010_us_040_00_5m'
    HOME = os.path.expanduser('~')
    path = HOME + '/data/' + fn
    return gpd.read_file(path)

def plot(gdf):
    fig,ax = plt.subplots()
    gdf.boundary.plot()
    return ax

def save():
    script_name = __file__.split('.')[0]
    ofn = script_name + '.png'
    print(ofn)
    plt.savefig(ofn,dpi=300)
    subprocess.run(['open','-a','Preview',ofn])
    
if __name__ == "__main__":
    gdf = get_data()
    outline = lower48(gdf)
    plot(outline)