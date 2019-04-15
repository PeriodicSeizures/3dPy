import json
import copy
import gl
import math2d
import math3d
import numpy as np

class physics:
    def __init__(self):
        self.gravity = -1
        self.isActive = True
                            
    def update(self, delta):
        if self.isActive:
            for o1 in gl.gameObjects:
                if o1.isKinetic:
                    xBreak = False; yBreak = False; zBreak = False
                    
                    n = math3d.normalize(o1.velocity)
                    x = o1.pos[0]; y = o1.pos[1]; z = o1.pos[2]

                    if o1.useGravity:
                        o1.velocity[1] += self.gravity*delta
                    
                    for o2 in gl.gameObjects:
                        
                        if o1.name != o2.name:
                            for face in o2.faces:
                                tri = face["verts"]

                                """

                                        GRAVITY

                                """
                                



                                    

                                """

                                        COLLISIONS
                                
                                """
                                if xBreak and yBreak and zBreak:
                                    break
                                

                                if n != -1:
                                    if not xBreak:
                                        if math3d.pointInTri(x+n[0]/10, y, z,
                                                             tri[0][0],tri[0][1],tri[0][2],
                                                             tri[1][0],tri[1][1],tri[1][2],
                                                             tri[2][0],tri[2][1],tri[2][2]):
                                            
                                            xBreak = True

                                            
                                    if not yBreak:
                                        if math3d.pointInTri(x, y+n[0]/10, z,
                                                             tri[0][0],tri[0][1],tri[0][2],
                                                             tri[1][0],tri[1][1],tri[1][2],
                                                             tri[2][0],tri[2][1],tri[2][2]):
                                            
                                            if n[1] < 0:
                                                o1.grounded = True
                                            else:
                                                o1.grounded = False
                                            
                                            yBreak = True

                                        
                                    if not zBreak:
                                        if math3d.pointInTri(x, y, z+n[0]/10,
                                                             tri[0][0],tri[0][1],tri[0][2],
                                                             tri[1][0],tri[1][1],tri[1][2],
                                                             tri[2][0],tri[2][1],tri[2][2]):
                                            
                                            zBreak = True



                                """
                                if math3d.lineXTriPlane(tri,
                                                              [[x-n[0]/10, y, z], # was just rb.pos, instead of list
                                                              [x+n[0]/10, y, z]]):
                                    o1.velocity[0] = math2d.clamp(o1.velocity[0], 0, -o1.velocity[0])

                                    

                                if math3d.lineXTriPlane(tri,
                                                              [[x, y-n[1]/10, z],
                                                              [x, y+n[1]/10, z]]):
                                    if n[1] < 0:
                                        o1.grounded = True
                                    else:
                                        o1.grounded = False
                                    
                                    o1.velocity[1] = math2d.clamp(o1.velocity[1], 0, -o1.velocity[1])


                                else:
                                    o1.grounded = False

                                if math3d.lineXTriPlane(tri,
                                                              [[x, y, z-n[2]/10],
                                                              [x, y, z+n[2]/10]]):
                                    o1.velocity[2] = math2d.clamp(o1.velocity[2], 0, -o1.velocity[2])

                                """



                                """

                                        FRICTION ON GROUND

                                """

                                """
                                if o1.grounded:
                                    print("Applying friction")
                                    if isWithin(o1.velocity[0], -.1,.1):
                                        o1.velocity[0] = 0
                                    else:
                                        o1.velocity[0] -= np.sign(o1.velocity[0])*delta

                                    if isWithin(o1.velocity[2], -.1,.1):
                                        o1.velocity[2] = 0
                                    else:
                                        o1.velocity[2] -= np.sign(o1.velocity[2])*delta
                                """


                            
                    """

                            MOVE OBJECT BY VELOCITY

                    """

                    if xBreak:
                        o1.velocity[0] = 0 #math2d.clamp(o1.velocity[0], 0, -o1.velocity[0])
                    if yBreak:
                        o1.velocity[1] = 0 #math2d.clamp(o1.velocity[1], 0, -o1.velocity[1])
                    if zBreak:
                        o1.velocity[2] = 0 #math2d.clamp(o1.velocity[2], 0, -o1.velocity[2])

                    if o1.velocity[0]!=0:
                        o1.pos[0] += .5*(o1.velocity[0])*delta
                    if o1.velocity[1]!=0:
                        o1.pos[1] += .5*(o1.velocity[1])*delta
                    if o1.velocity[2]!=0:
                        o1.pos[2] += .5*(o1.velocity[2])*delta



                            
