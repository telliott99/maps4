import matplotlib.pyplot as plt
import template as tpl

import update_path
import utils.ustates as us

gdf = tpl.get_data()
outline = tpl.lower48(gdf)
# -----

D = us.state_to_fips
capD = dict()

fn = '../data/us-state-capitals.csv'
with open(fn) as fh:
    data = fh.read().strip().split('\n')
    # skip the column names
    for line in data[1:]:
        state,capital,lat,lon = line.strip().split(',')
        fips = us.state_to_fips[state]
        capD[fips] = {
             'name':capital,
             'lon':float(lon),
             'lat':float(lat)}

X = list()
Y = list()
  
def f(row):
    fips = row['STATE']
    try:
        sD = capD[fips]
        X.append(sD['lon'])
        Y.append(sD['lat'])
    except KeyError:
        return

outline.apply(f,axis=1)

# -----

fig,ax = plt.subplots()
ax = outline.boundary.plot(
    ax=ax,color='blue',linewidth=0.7)
    
ax.scatter(X,Y,
    color='red',s=10,zorder=2)

tpl.save()
