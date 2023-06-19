import sys, os, subprocess, time

def print_usage():
    print('usage:  python3 test.py arg')
    print('arg = basic, plot, scripts or all')
    sys.exit()

try:
    which = sys.argv[1]
except IndexError:
    print_usage()
    
def do_basic_tests():
    script = 'test_search_CL.py'
    cmd = ['python3','tests/' + script]
    subprocess.run(cmd)
    
    cmd = ['python3','tests/test_save.py']
    subprocess.run(cmd)
    
    cmd = ['python3','tests/test_search.py']
    subprocess.run(cmd)
    
    cmd = ['python3',
        'tests/test_multi_road_search.py']
    subprocess.run(cmd)

def do_plot_tests():
    cmd = ['python3',
        'tests/test_plot_region.py']
    subprocess.run(cmd)
    cmd = ['python3',
        'tests/test_plot_points.py']
    subprocess.run(cmd)
    cmd = ['python3',
        'tests/test_plot_gdf.py']
    subprocess.run(cmd)
    cmd = ['python3',
        'tests/test_plot_segment.py']
    subprocess.run(cmd)

def run_scripts():
    cmd = ['python3',
        'demos/colorus.py']
    subprocess.run(cmd)

    cmd = ['python3',
        'demos/regional_roads.py']
    subprocess.run(cmd)

    
if __name__ == "__main__":
    if which == 'basic':
        do_basic_tests()
        
    elif which == 'plot':
        do_plot_tests()
        
    elif which == 'scripts':
        run_scripts()

    elif which == 'all':
        do_basic_tests()
        do_plot_tests()
        run_scripts()
        
    else:
        print_usage()
    
    time.sleep(2)
    cmd = ['killall','Preview']
    subprocess.run(cmd)

