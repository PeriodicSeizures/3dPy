import math
import numpy as np

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

"""

A(0,0,0), B(1,0,0), C(0,1,1)

D(0,1/2,0), and E(1,1/2,1)

"""

def lineIntersect3dTri(T, L):
    a = T[0]; b = T[1]; c = T[2]
    d = L[0]; e = L[1]
    
    abcd = np.array([[a[0], a[1], a[2], 1],
                     [b[0], b[1], b[2], 1],
                     [c[0], c[1], c[2], 1],
                     [d[0], d[1], d[2], 1]])

    abce = np.array([[a[0], a[1], a[2], 1],
                     [b[0], b[1], b[2], 1],
                     [c[0], c[1], c[2], 1],
                     [e[0], e[1], e[2], 1]])

    _abcd = np.sign(np.linalg.det(abcd))
    _abce = np.sign(np.linalg.det(abce))

    if _abcd == -_abce:
        return True
    
    return False

def dist3d(vert1, vert2):
    d = math.sqrt(

            math.pow(vert1[0]-vert2[0], 2) +

            math.pow(vert1[1]-vert2[1], 2) +

            math.pow(vert1[2]-vert2[2], 2)


        )
    return d

                                
def normalize(vector):
    if vector[0]==0 and vector[1]==0 and vector[2]==0:
        return [0,0,0]
    
    d = dist3d([0,0,0], vector)
    v = [vector[0]/d, vector[1]/d, vector[2]/d]
    return v
