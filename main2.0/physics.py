import json
import copy
import gl
import math2d
import math3d
import numpy as np
import copy

def objectCollide(obj1, obj2):
    vector1 = obj1.velocity
    vector2 = obj2.velocity

    if math3d.normalize(vector1) > 0:
        if math3d.pointInTri(x+n[0]/10, y, z,
                         tri[0][0],tri[0][1],tri[0][2],
                         tri[1][0],tri[1][1],tri[1][2],
                         tri[2][0],tri[2][1],tri[2][2],
                         "low_med"):
            


class physics:
    def __init__(self):
        self.gravity = -9.8
        self.isActive = True
    
    
    
    """
    
    
        The issue here is that when objects have more faces, it takes longer to calculate collision,
        
        and then the move-velocity is delayed by that time?
        
        
        Need to get a new delta after loop to maintain timestep
    
    
    """
    
    def update(self, delta, objects):
        
        if self.isActive:
            for o1 in objects:
                





                if o1.isKinetic:
                    n = math3d.normalize(o1.velocity)
                    #print(n)
                    x = o1.pos[0]; y = o1.pos[1]; z = o1.pos[2]

        
                    """

                            GRAVITY

                    """
                    
                    if o1.useGravity:
                        o1.velocity[1] += self.gravity*delta




                    """

                    CHECK FOR COLLISIONS, Time will vary

                    """
                    
                    for o2 in objects:
                        if not o1 is o2:
                       
                            for face in o2.colliderFaces:
                                tri = copy.deepcopy(face)
                                
                                """

                                calculate next position from velocity vector

                                take position, and add velocity/4

                                to imitate the quarter frame detection in sm640

                                if math3d.pointInTri()

                                """
##
##                                if math3d.pointInTri(x+n[0]/10, y, z,
##                                    tri[0][0],tri[0][1],tri[0][2],
##                                    tri[1][0],tri[1][1],tri[1][2],
##                                    tri[2][0],tri[2][1],tri[2][2]):
##                                
                                if n!=0:
                                    if o1.velocity[0]!=0:
                                        
                                        if math3d.pointInTri(x+n[0]/10, y, z,
                                                             tri[0][0],tri[0][1],tri[0][2],
                                                             tri[1][0],tri[1][1],tri[1][2],
                                                             tri[2][0],tri[2][1],tri[2][2],
                                                             "low_med"):
                                            
                                            o1.velocity[0] = math2d.clamp(o1.velocity[0], 0, -o1.velocity[0])

                                            
                                    if o1.velocity[1]!=0:
                                        if math3d.pointInTri(x, y+n[0]/10, z,
                                                             tri[0][0],tri[0][1],tri[0][2],
                                                             tri[1][0],tri[1][1],tri[1][2],
                                                             tri[2][0],tri[2][1],tri[2][2],
                                                             "low_med"):
                                            # if velocity is downwards
                                            # when object is collided with,
                                            # then is on a surface; grounded
                                            if n[1] < 0:
                                                o1.grounded = True
                                                #print("grounding")
                                            else:
                                                o1.grounded = False
                                            
                                            o1.velocity[1] = math2d.clamp(o1.velocity[1], 0, -o1.velocity[1])
                                            print(math2d.clamp(o1.velocity[1], 0, -o1.velocity[1]))
                                            

                                        
                                    if o1.velocity[2]!=0:
                                        if math3d.pointInTri(x, y, z+n[0]/10,
                                                             tri[0][0],tri[0][1],tri[0][2],
                                                             tri[1][0],tri[1][1],tri[1][2],
                                                             tri[2][0],tri[2][1],tri[2][2],
                                                             "low_med"):
                                            
                                            o1.velocity[2] = math2d.clamp(o1.velocity[2], 0, -o1.velocity[2])

                                    """

                                            FRICTION ON GROUND
                                            
                                                might or might not work currently

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
        
                if o1.velocity[0]!=0:
                    o1.pos[0] += .5*(o1.velocity[0])*delta
                if o1.velocity[1]!=0:
                    o1.pos[1] += .5*(o1.velocity[1])*delta
                    #print(o1.velocity[1])
                if o1.velocity[2]!=0:
                    o1.pos[2] += .5*(o1.velocity[2])*delta

                        
