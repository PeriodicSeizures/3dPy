"""

    Data file for storing files

    will be using this over json because:

        json is an added extension

        can achieve same thing in python file

        multiple files like mesh, collider, object is too much confusion,
        and is ugly in a way

    
 
"""
import math

class Vector3:
    def __init__(x,y,z):
        self.x=x; self.y=y; self.z=z

    def normalized(self):
        d = self.dist([0,0,0], [self.x,self.y.self.z])
        
        if d==0: return Vector3(0,0,0)
        return Vector3(self.x/d, self.y/d, self.z/d)

    def normalize(self):
        d = self.dist([0,0,0], [self.x,self.y.self.z])
        
        if d==0: self.x=0; self.x=0; self.y=0
        else: self.x/=d; self.y/=d; self.z/=d

    def magnitude(self, vector):
        return math.sqrt(
            math.pow(self.x-vector.x, 2) +

            math.pow(self.y-vector.y, 2) +

            math.pow(self.z-vector.z, 2)
        )
    

class Object:
    def __init__(self, name, o):
        self.name = name
        self.pos = o["pos"]
        
        self.meshFaces = []
        self.colliderFaces = []
        
        self.isKinetic = o["isKinetic"]
        self.velocity = [0,0,0]
        self.useGravity = True
        self.grounded = False
        
        if "mesh" in o:
            self.meshFaces = o["mesh"]
        if "collider" in o:
            self.colliderFaces = o["collider"]
			

    def getRawVerts(self):
        v = []
        for face in self.meshFaces:
            for vert in face["verts"]:
                v.append(vert)
        return v


objectList = {

    "floor" : {

        "pos" : [0,0,0],
        "isKinetic" : False,
        "enableMesh" : True,
        "enableCollider" : True,
        "mesh" : [					# VISUAL
            {
                "color" : "0x00AAAA",
                "verts" : [			
                    [0,0,0],
                    [0,0,5],
                    [5,0,5]
                ]
            },
            {
                "color" : "0x009999",
                "verts" : [			
                    [0,0,0],
                    [5,0,5],
                    [5,0,0]
                ]
            }
        ],
        "collider" : [				# PHYSICAL
            [
                [0,0,0],
                [0,0,5],
                [5,0,5]
            ],
            [
                [0,0,0],
                [5,0,5],
                [5,0,0]
            ]
        ]
    }
}

objects = []
for name, value in objectList.items():
    objects.append(Object(name, objectList[name])) 
