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
                    
                    for o2 in gl.gameObjects:
                        if o1.name != o2.name:
                            for face in o2.faces:
                                tri = face["verts"]

                                """

                                        GRAVITY

                                """
                                
                                if o1.useGravity:
                                    #print("Gravity applied to",o1.name)
                                    o1.velocity[1] += self.gravity*delta


                                    

                                """

                                        COLLISIONS
                                
                                """
                                
                                n = math3d.normalize(o1.velocity)
                                x = o1.pos[0]; y = o1.pos[1]; z = o1.pos[2]

                                # If line drawn towards
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
                            
                o1.pos[0] += .5*(o1.velocity[0])*delta
                o1.pos[1] += .5*(o1.velocity[1])*delta
                o1.pos[2] += .5*(o1.velocity[2])*delta



                            
