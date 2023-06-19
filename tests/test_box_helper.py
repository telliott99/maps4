import sys, math, subprocess
import matplotlib.pyplot as plt

import update_path
import utils.ufmt as fmt
import utils.ufile as fh 
import utils.box as bh

def test():
    func_name = fh.get_name(__file__)
    print(func_name)

    P = fmt.Point(
        'Phoenix','AZ',-112.074037,33.448377)
    Q = fmt.Point(
        'Tucson','AZ',-110.926479,32.221743)
    hwy = 'I-10'
    
    # seg = fmt.Segment(P,Q,hwy)
    o,rot = bh.make_box_for_points(P,Q)
    
    fig, ax = plt.subplots()
    x, y = rot.exterior.xy
    ax.plot(x,y)
    ax.set_aspect('equal')
    
    ax.scatter(P.lon,P.lat,color='red',zorder=1)
    ax.scatter(Q.lon,Q.lat,color='black',zorder=1)
    
    fn = 'box_helper.png'
    path = fh.test_img_path + fn
    plt.savefig(path)
    
    cmd = ['open','-a','Preview', path]
    subprocess.run(cmd)
    

    
if __name__ == "__main__":
    test()