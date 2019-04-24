import json
import copy
import gl
import math2d
import math3d
import copy

def sign(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    return 0

def computeCollide(delta, obj1, obj2):
    a = obj1.velocity
    #b = obj2.velocity

    n = a.normalized()
    x,y,z = obj1.pos.x,obj1.pos.y,obj1.pos.z

    if a.magnitude() > 0: # and obj2.isKinetic: # or b.magnitude > 0:
        

        for tri in obj2.colliderFaces:

            #print(obj2.pos.x + "\n")
            if math3d.pointInTri(x+sign(n[0])*.1, y, z,
                             tri[0][0]+obj2.pos[0],tri[0][1]+obj2.pos[1],tri[0][2]+obj2.pos[2],
                             tri[1][0]+obj2.pos[0],tri[1][1]+obj2.pos[1],tri[1][2]+obj2.pos[2],
                             tri[2][0]+obj2.pos[0],tri[2][1]+obj2.pos[1],tri[2][2]+obj2.pos[2],
                             "low_med"):
                # set component to 0
                obj1.pos[0] += -sign(a.x)*(delta/10)
                
                a.x = 0
                
            
            if math3d.pointInTri(x, y+sign(n[1])*.2, z,
                             tri[0][0]+obj2.pos[0],tri[0][1]+obj2.pos[1],tri[0][2]+obj2.pos[2],
                             tri[1][0]+obj2.pos[0],tri[1][1]+obj2.pos[1],tri[1][2]+obj2.pos[2],
                             tri[2][0]+obj2.pos[0],tri[2][1]+obj2.pos[1],tri[2][2]+obj2.pos[2],
                             "low_med"):
                # set component to 0
                obj1.pos[1] += -sign(a.y)*(delta/10)
                a.y = 0
                obj1.grounded = True
                
            else:
                obj1.grounded = False

            if math3d.pointInTri(x, y, z+sign(n[2])*.1,
                             tri[0][0]+obj2.pos[0],tri[0][1]+obj2.pos[1],tri[0][2]+obj2.pos[2],
                             tri[1][0]+obj2.pos[0],tri[1][1]+obj2.pos[1],tri[1][2]+obj2.pos[2],
                             tri[2][0]+obj2.pos[0],tri[2][1]+obj2.pos[1],tri[2][2]+obj2.pos[2],
                             "low_med"):
                # set component to 0
                obj1.pos[2] += -sign(a.z)*(delta/10)
                a.z = 0


class physics:
    def __init__(self):
        self.gravity = -1
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

                            computeCollide(delta, o1,o2)
                            
                            """

                                    FRICTION ON GROUND
                                    
                                        might or might not work currently

                            """

                            if o1.grounded:
                                cf = 10
                                #print("Applying friction")
                                if math2d.isWithin(o1.velocity[0], -.1,.1):
                                    o1.velocity[0] = 0
                                else:
                                    o1.velocity[0] -= sign(o1.velocity[0])*delta*cf

                                if math2d.isWithin(o1.velocity[2], -.1,.1):
                                    o1.velocity[2] = 0
                                else:
                                    o1.velocity[2] -= sign(o1.velocity[2])*delta*cf
                            



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

                        
