import json
import copy
import gl
import math2 as math2
import physicsMath as phyMath
import numpy as np

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
                
                for gameObject in gl.gameObjects:
                    if gameObject.name!=rb.name:
                    #if gameObject != rb:
                        for face in gameObject.faces:
                            tri = face["verts"]

                            """

                                    COLLISIONS
                            
                            """
                            
                            n = phyMath.normalize(rb.velocity)
                            
                            if rb.useGravity and not rb.grounded:
                                rb.velocity[1] += self.gravity*delta
                                    
                            # If line drawn towards
                            if phyMath.lineIntersect3dTri(tri,
                                                          [[rb.pos[0]-n[0]/10,rb.pos[1],rb.pos[2]], # was just rb.pos, instead of list
                                                          [rb.pos[0]+n[0]/10,
                                                           rb.pos[1],
                                                           rb.pos[2]]]):
                                rb.velocity[0] = 0

                            if phyMath.lineIntersect3dTri(tri,
                                                          [[rb.pos[0],rb.pos[1]-n[1]/10,rb.pos[2]],
                                                          [rb.pos[0],
                                                           rb.pos[1]+n[1]/10,
                                                           rb.pos[2]]]):
                                if n[1] < 0:
                                    grounded = True
                                #rb.velocity[1] += delta
                                rb.velocity[1] = math2.clamp(rb.velocity[1], 0, -rb.velocity[1])
                                #print("Collide vertically :",rb.name)
                            else:
                                rb.grounded = False

                            if phyMath.lineIntersect3dTri(tri,
                                                          [[rb.pos[0], rb.pos[1], rb.pos[2]-n[2]/10],
                                                          [rb.pos[0],
                                                           rb.pos[1],
                                                           rb.pos[2]+n[2]/10]]):
                                rb.velocity[2] = 0
                            #
                            """

                                    FRICTION ON GROUND

                            """

                            """
                            # TEST THIS AFTER VEL MOVE
                            if rb.grounded:
                                if isWithin(rb.velocity[0], -.1,.1):
                                    rb.velocity[0] = 0
                                else:
                                    rb.velocity[0] -= np.sign(rb.velocity[0])*delta

                                if isWithin(rb.velocity[2], -.1,.1):
                                    rb.velocity[2] = 0
                                else:
                                    rb.velocity[2] -= np.sign(rb.velocity[2])*delta

                            """
                            
                """

                        MOVE OBJECT BY VELOCITY

                """
                            
                rb.pos[0] += .5*(rb.velocity[0])*delta
                rb.pos[1] += .5*(rb.velocity[1])*delta
                rb.pos[2] += .5*(rb.velocity[2])*delta



                            
