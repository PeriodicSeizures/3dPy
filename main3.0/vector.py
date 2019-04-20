import math

class Vector2:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def magnitude(self):
        return math.sqrt( ((self.x)**2) + ((self.y)**2) )

    def normalized(self):
        m = self.magnitude()
        if m == 0: return self
        
        return Vector2(self.x/m, self.y/m)

    """--------------

        OVERLOADED
         OPERATOR

    --------------"""
    
    """ MATH """

    # Vector3 + n
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x+other,self.y+other)
        elif isinstance(other, Vector3):
            return Vector2(self.x+other.x,self.y+other.y)
        return None

    # Vector3 - n
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x-other,self.y-other)
        elif isinstance(other, Vector3):
            return Vector2(self.x-other.x,self.y-other.y)
        return None

    # Vector3 * n
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x*other,self.y*other)
        elif isinstance(other, Vector2):
            return Vector2(self.x*other.x,self.y*other.y)
        return None

    # Vector3 / n
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x/other,self.y/other)
        elif isinstance(other, Vector2):
            return Vector2(self.x/other.x,self.y/other.y)

    # Vector3 % n
    def __mod__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x%other,self.y%other)
        elif isinstance(other, Vector2):
            return Vector2(self.x%other.x,self.y%other.y)
        return None

    #############################

    # -Vector3
    def __neg__(self):
        return Vector2(-self.x,-self.y,-self.z)

    # Vector3 += n
    def __iadd__(self, other):
        return self+other
    
    # Vector3 -= n
    def __isub__(self, other):
        return self-other

    """
    # n + Vector3
    def __radd__(self, other):
        return self+other

    # n - Vector3
    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(other-self.x,other-self.y)
        elif isinstance(other, Vector2):
            return -self+other
    """

    """ EQUALITY """

    # Vector3 == n
    def __ne__(self, other):
        if isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        else:
            return False

    """ MISC """

    # Vector3[i]
    def __getitem__(self, i):
        if i==0: return self.x
        elif i==1: return self.y
        else: return None

    def __setitem__(self, i, v):
        if i==0: self.x = v
        elif i==1: self.y = v

    # print(Vector3)
    def __str__(self):
        return ("(%f, %f)" % (self.x, self.y))

    
class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x=x
        self.y=y
        self.z=z

    def magnitude(self):
        return math.sqrt( ((self.x)**2) + ((self.y)**2) + ((self.z)**2) )

    def normalized(self):
        m = self.magnitude()
        if m == 0: return self
        
        return Vector3(self.x/m, self.y/m, self.z/m)

    """--------------

        OVERLOADED
         OPERATOR

    --------------"""
    
    """ MATH """

    # Vector3 + n
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(self.x+other,self.y+other,self.z+other)
        elif isinstance(other, Vector3):
            return Vector3(self.x+other.x,self.y+other.y,self.z+other.z)
        return None

    # Vector3 - n
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(self.x-other,self.y-other,self.z-other)
        elif isinstance(other, Vector3):
            return Vector3(self.x-other.x,self.y-other.y,self.z-other.z)
        return None

    # Vector3 * n
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(self.x*other,self.y*other,self.z*other)
        elif isinstance(other, Vector3):
            return Vector3(self.x*other.x,self.y*other.y,self.z*other.z)
        return None

    # Vector3 / n
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(self.x/other,self.y/other,self.z/other)
        elif isinstance(other, Vector3):
            return Vector3(self.x/other.x,self.y/other.y,self.z/other.z)
        return None

    # Vector3 % n
    def __mod__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(self.x%other,self.y%other,self.z%other)
        elif isinstance(other, Vector3):
            return Vector3(self.x%other.x,self.y%other.y,self.z%other.z)
        return None

    #############################

    # -Vector3
    def __neg__(self):
        return Vector3(-self.x,-self.y,-self.z)

    # Vector3 += n
    def __iadd__(self, other):
        return self+other
    
    # Vector3 -= n
    def __isub__(self, other):
        return self-other

    """
    # n + Vector3
    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(other+self.x,other+self.y,other+self.z)
        elif isinstance(other, Vector3):
            return Vector3(other.x+self.x,other.y+self.y,other.z+self.z)

    # n - Vector3
    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3(other-self.x,other-self.y,other-self.z)
        elif isinstance(other, Vector3):
            return -self+other
    """

    """ EQUALITY """

    # Vector3 == n
    def __ne__(self, other):
        if isinstance(other, Vector3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    """ MISC """

    # Vector3[i]
    def __getitem__(self, i):
        if i==0: return self.x
        elif i==1: return self.y
        elif i==2: return self.z
        else: return None

    def __setitem__(self, i, v):
        if i==0: self.x = v
        elif i==1: self.y = v
        elif i==2: self.z = v

    # print(Vector3)
    def __str__(self):
        return ("(%f, %f, %f)" % (self.x, self.y, self.z))


def distance(vector_1, vector_2):
    if isinstance(vector_1, Vector2) and isinstance(vector_2, Vector2):
        return math.sqrt(
            ((vector_1.x-vector_2.x)**2) +

            ((vector_1.y-vector_2.y)**2)
        )
    
    if isinstance(vector_1, Vector3) and isinstance(vector_2, Vector3):
        return math.sqrt(
            ((vector_1.x-vector_2.x)**2) +

            ((vector_1.y-vector_2.y)**2) +

            ((vector_1.z-vector_2.z)**2)
        )

"""
v1 = Vector3(1,1,1)
v1[1]-=5

print(v1[1])
"""
