import vector

def cross(a, b):
    c = vector.Vector3(a.y*b.z - a.z*b.y,
                       a.z*b.x - a.x*b.z,
                       a.x*b.y - a.y*b.x)
    return c


def dot(a, b):
    return a.x*b.x + a.y*b.y + a.z*b.z


class Triangle3d:
    # creates empty values
    def __init__(self, p1, p2, p3):
        self.equation = [0,0,0,0]
        self.origin = vector.Vector3()
        self.normal = vector.Vector3()
        
        self.normal = cross(p2-p1, p3-p1)
        self.normal = self.normal.normalized()
        self.origin = p1
        self.equation[0] = self.normal.x
        self.equation[1] = self.normal.y
        self.equation[2] = self.normal.z
        self.equation[3] = -(self.normal.x * self.origin.x +
                             self.normal.y * self.origin.y +
                             self.normal.z * self.origin.z)
        
    # bool of whether direction intersects tri
    def isFrontFacingTo(self, direction):
        dot_product = dot(self.normal, direction)
        #print(dot_product)
        return dot_product <= 0

    def signedDistanceTo(self, point):
        #print(self.equation[3])
        return dot(point, self.normal) + self.equation[3]


tri = Triangle3d(vector.Vector3(1,1,0), # 0,0,0
                 vector.Vector3(2,1,0), # 1,0,0
                 vector.Vector3(2,2,0)) # 1,0,1


#print(tri.isFrontFacingTo(vector.Vector3(-1,0,0)))
print(tri.signedDistanceTo(vector.Vector3(743,5000,-96)))
