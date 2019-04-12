import json
import copy
import gl
import math2 as math2
import physicsMath as phyMath

##class rigidbody:
##    def __init__(self, obj, useGravity=True, useFriction=True, priority=1):  # Parameters are:
##                                # object, useGravity, 
##        # player = rigidbody(examplemodel) # more of method to use
##        # OR
##        # player = model(obj, rb = true) # preferably not to use
##
##        # player = rigidbody(examplemodel)
##        # player is a rigidbody with a collider of model
##        self.obj = obj;
##        self.useGravity = useGravity;
##        self.useFriction = useFriction;
##
##        self.gravity = -9.81
##        self.friction = .4
##        self.mass = 1
##        self.velocity = [0,0,0]
##        self.isKinematic = False

rigidbodies = []
for gameObject in gl.gameObjects:
    if gameObject.isRigid:
        rigidbodies.append(gameObject)

class physics:
    def __init__(self):
        self.gravity = -.1
        self.isActive = True
                            
    def update(self, delta):
        if self.isActive:
            for rb in rigidbodies:

##                rb.pos[0] += .5*(rb.velocity[0])*delta
##                rb.pos[1] += .5*(rb.velocity[1])*delta
##                rb.pos[2] += .5*(rb.velocity[2])*delta
##                
##                if rb.useGravity:
##                    rb.velocity[1] += self.gravity*delta

##                if rb.useFriction
##                # Somewhere here in determining friction, need to test for
##                # collision
##                    if (isOutside(rb.velocity[0], -.1, .1) and
##                        isOutside(rb.velocity[1], -.1, .1) and
##                        isOutside(rb.velocity[2], -.1, .1)):
##                        
##                        rb.velocity += -rb.friction

                """
                # Collisions
                # this will probably be hell to calc for every vert/face
                # combination + rotations included and fast velocities without
                # object passing through colliders,
                # so rotations will be COMPLETELY ignored, and objects
                # dont have rotations anyways, because they are weird af to
                # calculate.
                
                # In short, calculate collisions with no ratations.
                """




                #for _rb in gl.gameObjects:
                #    pass
                    

                # Need to iterate every object, and test if rb collides
                #for gameObject in gl.gameObjects:

                    # Since gameObjects are made up of tris,

                    # calculate a rotation created by verts in the tris


                # Collisions are only tested between
                # all rigidbodies, and all gameObjects
                intersect = False
                for gameObject in gl.gameObjects:
                    if gameObject.name!=rb.name:
                    #if gameObject != rb:
                        for face in gameObject.faces:
                            tri = face["verts"]
                            
    ##                        for i in range(len(tri)):
    ##                            for j in range(len(tri[i])):
    ##                                tri[i][j] += gameObject.pos[j]
                            
                            # returns the normalized vector in order to do
                            # comparisons ...
                            """
                            To get a box collider from an object,
                            that object has to have at least 1 concave (pair) of faces
                            
                            I say (pair) because the nearby faces dont need to be *attached*.
                            
                            This shoouldn't be used because its weird.
                            
                            Just get box-collider of complex objects if they have a collider
                            
                            NEW :: IMPLEMENT A BOX COLLIDER bool to ALL objects
                            
                            
                            """
                            n = phyMath.normalize(rb.velocity)
                            

                            # If line drawn towards
                            if phyMath.lineIntersect3dTri(tri,[rb.pos,
                                                              [rb.pos[0]+n[0]/10,
                                                               rb.pos[1]+n[1]/10,
                                                               rb.pos[2]+n[2]/10]]):

                                intersect = True
                                #print("collide:",gameObject.name,rb.name)
                                #rb.velocity[0]=0;rb.velocity[1]=0;rb.velocity[2]=0
                                break;
                            else:
                                rb.pos[0] += .5*(rb.velocity[0])*delta
                                rb.pos[1] += .5*(rb.velocity[1])*delta
                                rb.pos[2] += .5*(rb.velocity[2])*delta
                                
                                if rb.useGravity:
                                    rb.velocity[1] += self.gravity*delta

                        else:
                            continue
                        break

                
                
##################### ADD THIS BX COLLISION:::

def boxBoxIntersect(box1, box2):
    x1 = box1.pos[0] - .5*box1.collider[0]; x2 = box1.pos[0] + .5*box1.collider[0]
    y1 = box1.pos[1] - box1.collider[1]; 
    if box1.collider['x']
    """
    
    Instead of exactly defining the 8 box verts, 
    
    define a (x, y, z)
    
        where:
        x: xscale
        y: yscale
        z: zscale
        
        center will be at (pos)
        
    Ex:
    
    collider = {'x' : 2, 'y' : 3, 'z' : 4}
    
    referencing coord:
    
        a_variable = collider['x']
    
    
    """
