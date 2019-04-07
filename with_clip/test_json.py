import json

class object:
    def __init__(self, name, pos, faces):
        self.name = name
        self.pos = pos
        self.faces = faces

with open("test.json") as file: # Need to redo the key finds in drawing
                                # methods
    f = json.load(file)
    objects = []
    for obj_name, value in f.items():
        objects.append(object(obj_name, f[obj_name]["pos"], f[obj_name]["faces"]))
    print(objects[0].faces,"\n")




for obj in objects:
    
    vert_list=[]
    for face in obj.faces:
        for vert in face["verts"]:
            vert_list.append(vert)
    
    #print(vert_list)
    #vert_list = [(getWorldCoord(v, camera) for v in face["verts"]) for face in obj.faces]
    #vert_list = [(v for v in face["verts"]) for face in obj.faces]
    #print(vert_list[0][0])
    #print(vert_list)
    #print(vert_list,"\n")
    for f in range(len(obj.faces)):

        verts = [(vert_list[v] for v in face) for face in obj.faces[f]["verts"]]



