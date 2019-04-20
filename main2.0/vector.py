import math

class Vector3:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def magnitude(self):
        return math.sqrt(

            math.pow(vert1[0]-vert2[0], 2) +

            math.pow(vert1[1]-vert2[1], 2) +

            math.pow(vert1[2]-vert2[2], 2)
        )

    def normalized(self):
        m = self.magnitude()
        if m == 0: return self
        
        return Vector3(self.x/m, self.y/m, self.z/m)
        
    def __add__(self, vector):
        return Vector3(self.x+vector.x,self.y+vector.y,self.z+vector.z)

    def __str__(self):
        return ("(%f, %f, %f)" % (self.x, self.y, self.z))

def angle(
def distance(vector1, vector2):
    return math.sqrt(

        math.pow(vert1[0]-vert2[0], 2) +

        math.pow(vert1[1]-vert2[1], 2) +

        math.pow(vert1[2]-vert2[2], 2)


    )

def 
"""
vector1 = Vector3(0,1,1)
vector2 = Vector3(2,1,1)

print(vector1+vector2)
"""
