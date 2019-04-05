# http://www.ambrsoft.com/MathCalc/Line/TwoLinesIntersection/TwoLinesIntersection.htm

class Line:
    def __init__(self, x1,y1,x2,y2):
        self.verts = [{},{}]
        self.verts[0] = {'x1' : x1, 'y1' : y1}
        self.verts[1] = {'x2' : x2, 'y2' : y2}
    def get_vert(v):
        return self.verts[v]
        
def cross(x1,y1,x2,y2): return x1*y2 - y1*x2

def intersect(x1,y1, x2,y2, x3,y3, x4,y4):
    x = cross(x1,y1, x2,y2)
    y = cross(x3,y3, x4,y4)
    det = cross(x1-x2, y1-y2, x3-x4, y3-y4)
    x = cross(x, x1-x2, y, x3-x4) / det
    y = cross(x, y1-y2, y, y3-y4) / det
    return x,y

def main():
    lines = []
    lines.append(Line(4,49,27,2))
    lines.append(Line(4,25,51,22))

    vert1 = lines[0].get_vert(0)
    vert2 = lines[0].get_vert(1)
    vert3 = lines[1].get_vert(0)
    vert4 = lines[1].get_vert(1)
    
    x,y = intersect(vert1['x1'], vert1[0]['y1'],
                 vert2[0]['x2'], vert2[0]['y2'],
                 vert3[1]['x1'], vert3[1]['y1'],
                 vert4[1]['x2'], vert4[1]['y2'])
    
    print("Intersection of 2 lines at: %.03f, %.03f" % (x,y))
    
main()

"""
char get_line_intersection(float p0_x, float p0_y, float p1_x, float p1_y, 
    float p2_x, float p2_y, float p3_x, float p3_y, float *i_x, float *i_y)
{
    float s1_x, s1_y, s2_x, s2_y;
    s1_x = p1_x - p0_x;     s1_y = p1_y - p0_y;
    s2_x = p3_x - p2_x;     s2_y = p3_y - p2_y;

    float s, t;
    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y);
    t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y);

    if (s >= 0 && s <= 1 && t >= 0 && t <= 1)
    {
        // Collision detected
        if (i_x != NULL)
            *i_x = p0_x + (t * s1_x);
        if (i_y != NULL)
            *i_y = p0_y + (t * s1_y);
        return 1;
    }

    return 0; // No collision
}



"""
