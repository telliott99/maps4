#### Extras

``hawaii.py`` is interesting.  First of all, it's Hawaii!  

Second, it uses a new Geopandas method called ``explode`` that "explodes" "Multi-Polygons" into individual Polygons.

It is then easy to plot the individual polygons.

The original data gives no indication of the identities of the islands (no names, no FIPS, no nothing).  See below for a solution.

Although the handwork makes it look interesting, what took me a very long time to figure out was how to simply extract the row index for each row:

```
i = row.name[1]
```

The proof of concept code is:

```
import pandas as np

D = {'a':list('pqr'),'b':list('xyz')}
df = np.DataFrame.from_dict(D)
print(df)
print()

def f(row):
    print(row['a'],row.name)

df.apply(f,axis=1)
```

which prints

```
> p3 script.py 
   a  b
0  p  x
1  q  y
2  r  z

p 0
q 1
r 2
>
```

except that, in the case of the Hawaii dataframe, row.name is a tuple.  Not sure why.

#### Getting the names from positions

See [her](shapely_intro.md) (last part of the doc).
