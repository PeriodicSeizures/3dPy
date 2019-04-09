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
    

def distOf3dVertPair(vert1, vert2):
    d = math.sqrt(

            math.pow(vert1[0]-vert2[0], 2) +

            math.pow(vert1[1]-vert2[1], 2) +

            math.pow(vert1[2]-vert2[2], 2)


        )
    return d

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
    
