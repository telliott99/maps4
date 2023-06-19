import update_path
from utils.ustates import *

def test():
    for state in states:
        fips = state_to_fips[state]
        abbrev = state_to_abbrev[state]
        print(','.join([state, abbrev, fips]))
        assert fips_to_abbrev[fips] == state_to_abbrev[state]
        
if __name__ == "__main__":
    test()        

'''
> p3 tests/test_ustates.py 
Alabama,AL,01
Alaska,AK,02
Arizona,AZ,04
Arkansas,AR,05
California,CA,06
Colorado,CO,08
Connecticut,CT,09
Delaware,DE,10
District of Columbia,DC,11
Florida,FL,12
Georgia,GA,13
Hawaii,HI,15
Idaho,ID,16
Illinois,IL,17
Indiana,IN,18
Iowa,IA,19
Kansas,KS,20
Kentucky,KY,21
Louisiana,LA,22
Maine,ME,23
Maryland,MD,24
Massachusetts,MA,25
Michigan,MI,26
Minnesota,MN,27
Mississippi,MS,28
Missouri,MO,29
Montana,MT,30
Nebraska,NE,31
Nevada,NV,32
New Hampshire,NH,33
New Jersey,NJ,34
New Mexico,NM,35
New York,NY,36
North Carolina,NC,37
North Dakota,ND,38
Ohio,OH,39
Oklahoma,OK,40
Oregon,OR,41
Pennsylvania,PA,42
Rhode Island,RI,44
South Carolina,SC,45
South Dakota,SD,46
Tennessee,TN,47
Texas,TX,48
Utah,UT,49
Vermont,VT,50
Virginia,VA,51
Washington,WA,53
West Virginia,WV,54
Wisconsin,WI,55
Wyoming,WY,56
> 
'''
