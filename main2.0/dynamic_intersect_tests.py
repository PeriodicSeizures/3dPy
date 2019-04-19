# dynamic pt tri intersect test:

import math3d

intersects = math3d.pointInTri(.99,.99,.99,
                               1,1,1,
                               10,1,1,
                               10,10,10,
                               "high")

if intersects:
    print("They intersect")
