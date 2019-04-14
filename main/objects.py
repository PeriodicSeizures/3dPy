"""

    Data file for storing files

    will be using this over json because:

        json is an added extension

        can achieve same thing in python file

        multiple files like mesh, collider, object is too much confusion,
        and is ugly in a way

    
 
"""

objects = {

    "floor" : {

        "pos" : [0,0,0],
        "isRigid" : False,
        "enableMesh" : True,
        "enableCollider" : True,
        "mesh" : [
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
        "collider" : 
    }
}
