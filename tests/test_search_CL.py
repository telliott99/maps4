import sys,os,subprocess

import update_path
import utils.ufile as fh

def test1():
    func_name = 'scripts/search_CL.py'
    state = 'CA'
    targetL = 'US Hwy 101'
    cmd = ['python3', func_name, 
        state, targetL,'strict']
    subprocess.run(cmd)

# non-strict search
def test2():
    func_name = 'scripts/search_CL.py'
    state = 'CO'
    targetL = '40,50,160'
    cmd = ['python3', func_name, 
        state, targetL]
    subprocess.run(cmd)

# strict search
def test3():
    func_name = 'scripts/search_CL.py'
    state = 'CO'
    targetL = 'US Hwy 40'
    cmd = ['python3', func_name, 
        state, targetL,'strict']
    subprocess.run(cmd)

def test4():
    func_name = 'scripts/search_CL.py'
    state = 'AZ'
    # a real problematic one
    targetL = '89A'
    cmd = ['python3', func_name, 
        state, targetL]
    subprocess.run(cmd)

def test_all():
    test1()
    test2()
    test3()
    test4()
    
if __name__ == "__main__":
    func_name = fh.get_name(__file__)
    print(func_name)

    test_all()
    #test2()
                
