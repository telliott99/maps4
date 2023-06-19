import geopandas as gpd
import fiona.errors as err

try:
    fn1 = 'gz_2010_us_040_00_5m.zip'
    gdf = gpd.read_file(fn1)
except err.DriverError:
    print("that didn't work")
    fn2 = 'gz_2010_us_040_00_5m'
    gdf = gpd.read_file(fn2)
    print("but that did")

# gpd should be able to read ZIP files
fn3 = 'cc-adventure.shp.zip'
gdf = gpd.read_file(fn3)
print("and so did that")

# docs say if "dataset is in a folder in the ZIP"
# put ! + filename
# but no

# this doesn't work either
path = 'zip://' + fn1
gdf = gpd.read_file(path)

# nope
fh = open(fn1)
gdf = gpd.read_file(fh)

'''
that didn't work
but that did
and so did that
Traceback ... fiona.errors.DriverError
'''