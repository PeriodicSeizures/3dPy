
def cross(x1,y1,x2,y2): return x1*y2 - y1*x2

def intersect(x1,y1, x2,y2, x3,y3, x4,y4, renderer):
    x = cross(x1,y1, x2,y2)
    y = cross(x3,y3, x4,y4)
    det = cross(x1-x2, y1-y2, x3-x4, y3-y4)
    x = cross(x, x1-x2, y, x3-x4) / det
    y = cross(x, y1-y2, y, y3-y4) / det
