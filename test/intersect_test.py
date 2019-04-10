def intersect(p0_x, p0_y, 
              p1_x, p1_y, 
              p2_x, p2_y, 
              p3_x, p3_y):

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
        return (round(p0_x + (t * s1_x),2),
                round(p0_y + (t * s1_y),2))

    return None, None #false; # No collision

def main():
    x,y = intersect(15,10,49,25,
                    29,5,37,15)
    
    print("Intersection of 2 lines at:",x,y)
    
main()
