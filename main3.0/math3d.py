import math
import numpy as np
import math2d

"""

A(0,0,0), B(1,0,0), C(0,1,1)

D(0,1/2,0), and E(1,1/2,1)

"""

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
"""

def areaOfTri(vert1,vert2,vert3):
	a = dist(vert1,vert2)
	b = dist(vert2,vert3)
	c = dist(vert3,vert1)
	
	s = (a+b+c)/2

	f = s*(s-a)*(s-b)*(s-c)

	if math2d.isWithin(f, 0, .01) or f<0:
            f = 0

            #print("val formatted")
            
	area = math.sqrt(f)
	
	return area


def pointInTri(x1,y1,z1,    # P
               x2,y2,z2,    # A
               x3,y3,z3,    # B
               x4,y4,z4,
               precision):   # C

    ABC = areaOfTri([x2,y2,z2],[x3,y3,z3],[x4,y4,z4])
    APB = areaOfTri([x2,y2,z2],[x1,y1,z1],[x3,y3,z3])
    APC = areaOfTri([x2,y2,z2],[x1,y1,z1],[x4,y4,z4])
    BPC = areaOfTri([x3,y3,z3],[x1,y1,z1],[x4,y4,z4])

    prec = {'low' : 0, 'low_med' : 1, 'med' : 2, 'med_high' : 3, 'high' : 4}

    sum = APB+APC+BPC # precise up to 5 digits
    ABC = ABC

    #print("%.05f %.05f" % (sum, ABC))

    if prec[precision]==0 and abs(sum-ABC) <= 3:
        #sum = int(sum)
        #ABC = int(ABC)
        return True

    elif prec[precision] == 1 and abs(sum-ABC) <= 1.5:
        #sum = round(sum,prec[precision]) # precise up to 5 digits
        #ABC = round(ABC,prec[precision])
        return True

    elif prec[precision] == 2 and abs(sum-ABC)<=.75:
        return True

    elif prec[precision] == 3 and abs(sum-ABC)<=.25:
        return True

    elif prec[precision] == 4 and abs(sum-ABC)<=.1:
        return True    

    return False

    """
    if sum == ABC:
        return True
    return False
    """
