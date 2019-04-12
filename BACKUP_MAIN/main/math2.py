# operators
import math
import numpy as np

def isWithin(val, _min, _max):
    if val > _min and val < _max:
        return True
    return False


def isOutside(val, _min, _max):
    if val < _min and val > _max:
        return True
    return False


def clamp(num, small, big):
    return max(min(num, big), small)





"""
def pointIn3dTri(point, tri):
    # x∗(P1−P0)+y∗(P2−P0)=P−P0
    # https://math.stackexchange.com/questions/4322/check-whether-a-point-is-within-a-3d-triangle

    

    AreaABC = areaOfTri(tri[0][0])

    P = [point[0],point[1],point[2]]

    A = tri[0]; B = tri[1]; C = tri[2]

    a = (
        (distOf3dVertPair(P, B) * distOf3dVertPair(P, C)) /
        (2 * )
        )
"""


"""

    Instead of finding exact collisions with weird math,
    just use raycasts at fixed intervals,
    and fool-proof collisions
    (as in :

        ray was casted, and found a tri X units ahead, which means that

        object will collide within some time.

        After continued casting, object usually and repeatedly found by cast

        is no longer located after a raycast.

        This most likely means that :

            the object moved out of the raycast,
            the rays origin passed the object
            ...
        
        )



    ::::::::::::::::::::::
    Pseudocode::::

        cast ray and extend from there, testing for collisions
        If collide, then record distance traveled,

            pros:

                *easiest* method of collsiions to implement

            cons:

                *very innacurate, ray might pass object/tri's

        OR:::::

        test for wall approximately X units ahead,
        which is equal to velocity as a vector

        so, the faster self is moving, the greater distance away to check
        and the slower, the smaller distance to check for object/tri...

        OR:::::::

        just test like .1   OR   1 units
        


"""
    

##def intersect(p0_x, p0_y, 
##              p1_x, p1_y, 
##              p2_x, p2_y, 
##              p3_x, p3_y):
##
##    s1_x = p1_x - p0_x
##    s1_y = p1_y - p0_y
##    s2_x = p3_x - p2_x
##    s2_y = p3_y - p2_y
##
##    #float s, t;
##    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
##    t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)
##
##    if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
##        # Collision detected
##        #if (i_x != None):
##        #x = p0_x + (t * s1_x);
##        #if (i_y != None):
##        #y = p0_y + (t * s1_y);
##        return (round(p0_x + (t * s1_x),3),
##                round(p0_y + (t * s1_y),3))
##
##    return None, None #false; # No collision
