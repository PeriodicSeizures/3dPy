import math
import numpy as np




"""

A(0,0,0), B(1,0,0), C(0,1,1)

D(0,1/2,0), and E(1,1/2,1)

"""


def lineXTriPlane(T, L): # If intersects infinite plane defined by tri
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


def dist(vert1, vert2):
    d = math.sqrt(

            math.pow(vert1[0]-vert2[0], 2) +

            math.pow(vert1[1]-vert2[1], 2) +

            math.pow(vert1[2]-vert2[2], 2)


        )
    return d


def areaOfTri(vert1,vert2,vert3):
	a = dist(vert1,vert2)
	b = dist(vert2,vert3)
	c = dist(vert3,vert1)
	
	s = (a+b+c)/2
	
	area = math.sqrt(
	
		s*(s-a)*(s-b)*(s-c)
	
	)
	
	return area


def pointInTri(x1,y1,z1,    # P
               x2,y2,z2,    # A
               x3,y3,z3,    # B
               x4,y4,z4):   # C

    ABC = areaOfTri([x2,y2,z2],[x3,y3,z3],[x4,y4,z4])
    APB = areaOfTri([x2,y2,z2],[x1,y1,z1],[x3,y3,z3])
    APC = areaOfTri([x2,y2,z2],[x1,y1,z1],[x4,y4,z4])
    BPC = areaOfTri([x3,y3,z3],[x1,y1,z1],[x4,y4,z4])

    sum = round(APB+APC+BPC,1) # precise up to 5 digits
    ABC = round(ABC,1)

    if sum == ABC:
        return True
    return False
    

#def lineXTri(line, vert1, vert2, vert3):
#    if 


def normalize(vector):
    if vector[0]==0 and vector[1]==0 and vector[2]==0:
        return 0
    
    d = dist([0,0,0], vector)
    v = [vector[0]/d, vector[1]/d, vector[2]/d]
    return v


def uVectNorm(x1,y1,z1,    # P
              x2,y2,z2,    # Q
              x3,y3,z3):   # R
    """
    PQ = [x2-x1,y2-y1,z2-z1]
    PR = [x3-x1,y3-y1,z3-z1]

    x = np.array([[PQ[1], PQ[2]],
                  [PR[1], PR[2]]])
    y = np.array([[PQ[0], PQ[2]],
                  [PR[0], PR[2]]])
    z = np.array([[PQ[0], PQ[1]],
                  [PR[0], PR[1]]])
    
    x = np.linalg.det(x)
    y = np.linalg.det(y)
    z = np.linalg.det(z)

    return x,y,z
    """
    p1 = np.array([x1,y1,z1])
    p2 = np.array([x2,y2,z2])
    p3 = np.array([x3,y3,z3])

    v1 = p3-p1
    v2 = p2-p1

    cp = np.cross(v1,v2)
    a,b,c = cp

    d = np.dot(cp, p3)

    print(a,b,c)

"""
print(uVectNorm(1,-1,1,
                4,3,7,
                0,0,0))
"""
"""
print(uVectNorm(3,-1,2,
                1,-1,-3,
                4,-3,1))
"""
"""
print(uVectNorm(1,2,3,
                4,6,9,
                12,11,9))
"""
print(uVectNorm(-1,0,-1,
                0,0,1,
                0,0,0))
