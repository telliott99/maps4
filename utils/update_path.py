import sys

def get_parent(p):
    sep = '/'
    return sep.join(p.split(sep)[:-1])

script_path = sys.path[0]
parent = get_parent(script_path)
sys.path.insert(0,parent)
sys.path.insert(1,parent+'/utils')
