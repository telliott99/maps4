The project got big enought that it was essential to reorganize into directories.  In addition to ``data``, ``figs`` and ``notes``, we have  

- ``utils`` the basic "helpers"
- ``tests`` most of the tests
- ``scripts`` to exercise the helpers

Also, to keep the project footprint small, the big data files are in ``~/data``.

The working directory depends on where a script is called or imported from.  To make it possible to find everything, ``update_path.py`` adds ``project`` and ``project/utils`` to ``sys.path`` for each script. 

A copy of ``update_path.py`` is in each of the directories above.  Then we can do (for example):

```
import utils.geodata_helper as gh
```

#### todo

I found some advice about this issue [here](https://docs.python-guide.org/writing/structure/).  This can be done in a way that if the name of the overall project changes, things still work.

The structure is like:

```
project
	 tests
	     context.py
	     test1.py
	 utils
	     util1.py
```

``context.py`` has 

```
import sys,os 

parent = os.path.dirname(__file__)
nana = os.path.abspath(os.path.join(parent,'..'))
sys.path.insert(0,nana)

import utils.util1 as ut
```

And then since ``test1.py`` and ``context.py`` are in the same directory, from ``test1.py`` we can do

```
from context import ut

ut.f()
```
where ``f`` is somefunction defined in the file ``util1.py``.  And this works regardless of whether we do ``python3 tests/test1.py`` or ``cd`` into ``tests`` and then just do ``python3 test1.py``.

But when I tried to restructure the project in this way, I made a mess.  The problem is that the various utilities are interdependent so they import each other.

However I do like how the above method doesn't care what the name of the project is.

So at the least, I should change ``format_helper.py`` to be agnostic about the name.

#### helpers

The functions of the various helpers should be pretty obvious.  One that may not be is ``box_helper.py``.

Data is organized as 

- trip: a list of routes
- route: a list of segments
- segment P-highway-Q 
- P,Q are points with name, longitude, latitude

From the totality of points for any named highway, we select those of interest (from P to Q), by building a box that is used to clip or filter the points.  The box is oriented along the PQ vector and the cuts of interest occur on the skinny ends at P and Q.  See ``scripts/box-demo.py`` for an example.

The plot code has been reorganized to separate the functions to plot a GeoDataFrame, the regional outline, and any additional points.

This means that the caller must have done 

```
fig, ax = plt.subplots(figsize=(10,10))
```

and then pass ``ax`` into the plotter.

In some cases, (like ``colorus.py``) we use the built-in functionality of a geodataframe and just do ``gdf.plot()``.

revised 2023-06-12