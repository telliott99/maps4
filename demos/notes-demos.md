#### Demos

The scripts in the ``demos/`` directory are just that.  The output can be viewed in ``figs-demos/<filename>``.

``box-demo.py`` shows the basic idea for how we clip routes to endpoints ``P`` and ``Q``.  We build a box of the same length as ``PQ`` and then rotate it so it has the same orientation as the ``P->Q`` vector.

``box-demo2.py`` uses the utility functions in ``box_helper.py``.

``cities.py`` exercises the dictionaries constructed by ``ustates.py`` that contain latitude and longitude data for cities.  Some of that code has been incorporated into ``file_helper.py``.

``colorus.py`` is a very simple demo of a plot.  The actual colors used have no particular meaning.

The others are (currently):

- ``gdf-clip.py``
- ``i-route-plot.py``
- ``names.py``
- ``outline_us.py``
- ``regional_roads.py``
- ``simple.py``

See the files, what the code does should be clear.
