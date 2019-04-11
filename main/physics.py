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
                for gameObject in gl.gameObjects:
                    if gameObject.name!=rb.name:
                    #if gameObject != rb:
                        for face in gameObject.faces:
                            tri = face["verts"]
                            
    ##                        for i in range(len(tri)):
    ##                            for j in range(len(tri[i])):
    ##                                tri[i][j] += gameObject.pos[j]

                            n = normalize(rb.velocity)
                            if phyMath.lineIntersect3dTri(tri,[rb.pos,
                                                              [rb.pos[0]+n[0]/10,
                                                               rb.pos[1]+n[1]/10,
                                                               rb.pos[2]+n[2]/10]]):
                                
                                print("collide:",gameObject.name,rb.name)
                                rb.velocity[0]=0;rb.velocity[1]=0;rb.velocity[2]=0
                            else:
                                rb.pos[0] += .5*(rb.velocity[0])*delta
                                rb.pos[1] += .5*(rb.velocity[1])*delta
                                rb.pos[2] += .5*(rb.velocity[2])*delta
                                
                                if rb.useGravity:
                                    rb.velocity[1] += self.gravity*delta





                                
def normalize(vector):
    if vector[0]==0 and vector[1]==0 and vector[2]==0:
        return [0,0,0]
    
    d = phyMath.dist3d([0,0,0], vector)
    v = [vector[0]/d, vector[1]/d, vector[2]/d]
    return v
