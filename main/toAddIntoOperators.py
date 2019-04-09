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

if pointInTri(0, 0, 20, 0, 10, 30, 10, 15): 
    print('pt inside tri') 
else: 
    print('pt not inside tri')
    
    
#1/3 * (area of base tri) * (h^3)
def volumeOfTetrahedron(vert, vert2, vert3, vert4):
    h = #heighest pt to base
    


def pointIn3dTri(args):
    x∗(P1−P0)+y∗(P2−P0)=P−P0
    # https://math.stackexchange.com/questions/4322/check-whether-a-point-is-within-a-3d-triangle
    
    
# possible
# https://stackoverflow.com/questions/995445/determine-if-a-3d-point-is-within-a-triangle
