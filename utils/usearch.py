import sys
import pandas as pd
import utils.ufile as fh

'''
RTTYP values:
C County
I Interstate
M Common Name
O Other
S State recognized
U U.S.
'''

def filter_RTTYP(gdf,rttypL):
    def f(code):
        if code in rttypL:
            return True
        return False
    sel = [f(code) for code in gdf['RTTYP']]
    return gdf[sel]

def filter_out(e,L):
        if e in L:
            return False
        return True
        
# L should be FIPS codes for states
def filter_out_by_COL(gdf,L_in,COL,fips=True):
    if fips:
        L = [fh.fipsD[e] for e in L_in]
    sel = [filter_out(e,L) for e in gdf[COL]]
    return gdf[sel]
    
def lower48(gdf):
    L = ['HI','AK','PR']
    f = filter_out_by_COL
    return f(gdf,L,'STATE')

def is_close_enough(item,t):
    # we want 'Rte 40' and 'Hwy 40' but not '340'
    try:
        if item.endswith(' ' + t):
            return True
    except:
        pass
    return False
    
def match_list(item,targetL):
    return item in targetL
    
def search_for_outline(gdf,targetL):
    sel = [match_list(e,targetL) for e in gdf['STATE']]
    return gdf[sel]

def search(gdf,target,COL='FULLNAME',strict=True):
    matched = gdf[gdf[COL] == target]
    if strict:
        return matched
    
    f = is_close_enough
    sel = [f(item,target) for item in gdf[COL]]
    df = gdf[sel]
    return pd.concat([matched,df])

# one state, multiple roads
def multi_road_search(gdf,targetL,strict=True):
    dfL = list()
    for target in targetL:
        sub = search(gdf,target,strict=strict)
        dfL.append(sub)
    big_df = pd.concat(dfL)
    return big_df

def names(df,COL='FULLNAME'):
    L = list(df[COL])
    return sorted(list(set(L)))
    

    