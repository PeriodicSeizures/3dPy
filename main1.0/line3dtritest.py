import numpy as np

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

    print(np.linalg.det(abcd))
    print(np.linalg.det(abce))

    if _abcd == -_abce:
        
        return True
    
    return False

t = [

    [0,0,0],
    [0,0,2],
    [2,0,0]

    ]

line = [ # does normally intersect

    [.5,-1,.5],
    [.5,1,.5]

    ]

line = [ # 

    [0,-2,1],
    [0,1,1]

    ]

print(lineIntersect3dTri(t,line))
