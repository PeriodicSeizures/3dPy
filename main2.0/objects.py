"""

    Data file for storing files

    will be using this over json because:

        json is an added extension

        can achieve same thing in python file

        multiple files like mesh, collider, object is too much confusion,
        and is ugly in a way

    
 
"""

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

    def getRawColliderFaces(self):
        faces = []
        for face in self.colliderFaces:
            faces.append(face)
        return faces


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
                "color" : "0x00AAAA",
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
