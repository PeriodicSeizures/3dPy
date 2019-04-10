# operators
import math

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


def intersect(line1, line2):
    p0_x, p0_y = line1[0][0], line1[0][1]
    p1_x, p1_y = line1[1][0], line1[1][1]
    p2_x, p2_y = line2[0][0], line2[0][1]
    p3_x, p3_y = line2[1][0], line2[1][1]

    s1_x = p1_x - p0_x
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x
    s2_y = p3_y - p2_y

    #float s, t;
    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
    t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)

    if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
        # Collision detected
        #if (i_x != None):
        #x = p0_x + (t * s1_x);
        #if (i_y != None):
        #y = p0_y + (t * s1_y);
        return (round(p0_x + (t * s1_x),3),
                round(p0_y + (t * s1_y),3))

    return None, None #false; # No collision


def pointInTri(tri, point):
    s=0
    for vert in tri:
        y = (vert[1]-point[1])
        x = (vert[0]-point[0])

        s+=(math.atan2(y,x)*180/math.pi)
        #s*=180/math.pi

    #s*=180/math.pi
    print(s)
    s=abs(s)
    if isWithin(s, 359.5, 360.5):
        return True
    return False


def areaOfTri(x1, y1, x2, y2, x3, y3): 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 


def pointIn2dTri(x1, y1, x2, y2, x3, y3, x, y): 
    # Calculate area of triangle ABC 
    A = areaOfTri (x1, y1, x2, y2, x3, y3)
  
    # Calculate area of triangle PBC  
    A1 = areaOfTri (x, y, x2, y2, x3, y3) 
      
    # Calculate area of triangle PAC
    A2 = areaOfTri (x1, y1, x, y, x3, y3) 
      
    # Calculate area of triangle PAB  
    A3 = areaOfTri (x1, y1, x2, y2, x, y) 
      
    # Check if sum of A1, A2 and A3  
    # is same as A 
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False


def hitHoriz3dTri(pos, tri): #Tri must be like a floor
    # Calculate area of triangle ABC
    x1 = tri[0][0]; y1 = tri[0][2]
    x2 = tri[1][0]; y2 = tri[1][2]
    x3 = tri[2][0]; y3 = tri[2][2]
    

    x = pos[0]; y = pos[2]
    
    
    A = areaOfTri (x1, y1, x2, y2, x3, y3)
  
    # Calculate area of triangle PBC  
    A1 = areaOfTri (x, y, x2, y2, x3, y3) 
      
    # Calculate area of triangle PAC
    A2 = areaOfTri (x1, y1, x, y, x3, y3) 
      
    # Calculate area of triangle PAB  
    A3 = areaOfTri (x1, y1, x2, y2, x, y) 
      
    # Check if sum of A1, A2 and A3  
    # is same as A 
    if (A == A1 + A2 + A3) and isWithin(pos[1], tri[0][1] - .5, tri[0][1] + .5):
        return True
    else: 
        return False

    
"""
#1/3 * (area of base tri) * (h^3)
def volumeOfTetrahedron(vert, vert2, vert3, vert4):
    h = #heighest pt to base
"""

def distOf3dVertPair(vert1, vert2):
    d = math.sqrt(

            math.pow(vert1[0]-vert2[0], 2) +

            math.pow(vert1[1]-vert2[1], 2) +

            math.pow(vert1[2]-vert2[2], 2)


        )
    return d


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
