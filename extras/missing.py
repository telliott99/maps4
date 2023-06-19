'''
investigate "missing" data for Hwy 550 in sw CO
it's missing b/c a short section *in the middle*
is called US Hwy 550 N!
'''

import sys,os,subprocess

import geopandas as gpd
import matplotlib.pyplot as plt

script_name = __file__.split('.')[0]

# get roads for FIPS 08 (Colorado)
fn = 'tl_2020_08_prisecroads.zip'
HOME = os.path.expanduser('~')
p = HOME + '/data/prisecroads/' + fn
gdf = gpd.read_file(p)

# crop roads to the southwest corner
gdf = gdf.cx[-109:-107,37:38.5]

def f(e,t,strict=True):
    if strict:
        return e == t
    else:
        return t in e

sel = [f(e,'550',strict=False) for e in gdf['FULLNAME']]
relaxed = gdf[sel]

sel = [f(e,'US Hwy 550') for e in gdf['FULLNAME']]
US550 = gdf[sel]

sel = [f(e,'US Hwy 550 N') for e in gdf['FULLNAME']]
US550N = gdf[sel]

L = list(set(list(gdf['FULLNAME'])))
for e in sorted(L):
    if '550' in e:
        print(e)

fig,axes = plt.subplots(1,3)
for ax in axes:
    gdf.plot(ax=ax,color='lightgray')

ax = axes[0]
relaxed.plot(ax=ax,color='red')
ax.text(-108.4,38.8,'relaxed search')

ax = axes[1]
ax.yaxis.set_tick_params(labelleft=False)
US550.plot(ax=ax,color='red')
ax.text(-108.4,38.8,'US Hwy 550')

ax = axes[2]
ax.yaxis.set_tick_params(labelleft=False)
US550N.plot(ax=ax,color='red')
ax.text(-108.4,38.8,'US Hwy 550 N')

ofn = script_name + '.png'
plt.savefig(ofn)
subprocess.run(['open','-a','Preview',ofn])

'''
> p3 missing.py
US Hwy 550
US Hwy 550 N
>
'''