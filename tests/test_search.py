import matplotlib.pyplot as plt
import update_path

import utils.ugeo as gh
import utils.uplot as ph
import utils.usearch as sh
import utils.ufmt as fmt
import utils.ufile as fh


def test(state='CO',target='I- 25'):
    
    func_name = fh.get_name(__file__)
    print(func_name)

    ofn = func_name + '.png'
    # test results are saved to figs, not figs-save 
    path = fh.test_img_path + ofn
    
    gdf = gh.get_geodataframe_for_state_roads(state)    
    sub = sh.search(gdf,target,strict=False)
    
    stateL = ['AZ','UT','NM','CO']
    
    SZ=(7,7)
    fig,ax = plt.subplots(figsize=(SZ))
    
    ph.plot_region(ax,stateL=stateL)
    ph.plot_gdf(ax,sub,color='green')
    
    ph.save_and_show_file(fig,func_name,scrub=True)

if __name__ == "__main__":
    test()