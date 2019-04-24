import pygame
import math
import math2d
import os
import objects as objs
import vector

pi = math.pi

"""
    Rotate a pt around
"""

def rotate2d(pos, rot): # new rotation is a float in radians for rotation
    x,y = pos
    s,c = math.sin(rot), math.cos(rot)
    return [x*c-y*s, y*c+x*s]

"""
def rotate2d(pos, rot):
    x,y = pos
    s,c = rot #math.sin(rot), math.cos(rot)
    return x*c-y*s, y*c+x*s
"""


def get3dVert(vertex, originPos, originRot, targetPos):
    # WAS - FOR x,y,z
    # translate vert based on its position
    x = vertex[0]-originPos[0]+targetPos[0]
    y = vertex[1]+originPos[1]+targetPos[1]
    z = vertex[2]-originPos[2]+targetPos[2]
	
    """
    rx = [math.sin(originRot[0]), math.cos(originRot[0])]
    ry = [math.sin(originRot[1]), math.cos(originRot[1])]
    """

    x,z = rotate2d([x,z], originRot[1]) #ry
    y,z = rotate2d([y,z], originRot[0]) #rx

    return [x, y, z]



def get2dVert(v, 
              cx, cy,
              projX, projY):
    
    #xr = v[2]*projX
    #yr = v[2]*projY
    #return cx+int(v[0]/xr), cy+int(v[1]/yr)
    
    if v[2]!=0:
        #print(v[2])
        x = cx+int(v[0]/v[2]*projX)
        y = cy+int(v[1]/v[2]*projY)
    else:
        x = 10000
        y = 10000
    
    return [x, y]
    
    
    #return cx+int(v[0]/v[2]*projX), cy+int(v[1]/v[2]*projY)



minZ = .1


"""
    Rendering possible:
        clamp - ok.
	auto trig get2dVert - ok?
	
"""

class Renderer:
    def __init__(self, w, h):
        self.w = w; self.h = h
        self.cx = w//2; self.cy = h//2
                        
        self.pos = vector.Vector3(); self.rot = vector.Vector2()

        self.half_w, self.half_h = w/2,h/2
        self.setFov(90)
        """
        self.fov = 90/180*math.pi; self.half_fov = self.fov/2
        self.half_w, self.half_h = w/2,h/2
        self.projY = self.half_h/math.tan(self.half_fov)
        self.projX = self.half_w/math.tan(self.half_fov)/(w/h)
        """

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.display = pygame.display.set_mode((w,h))
		
    def update(self, gameObjects): 
	
        self.rot[0] = math2d.clamp(self.rot[0], -pi/2, pi/2) #.5*pi, 1.5*pi)
        
        verts3d_faces = []
        verts2d_faces = []
        #verts3d = []
        #verts2d = []
        # Background color
        #colors = []
        self.display.fill((255,255,255))
        
        for gameObject in gameObjects:
            if gameObject.meshFaces:
                
                for face in gameObject.meshFaces:
                    verts3d = []
                    #colors.append(face["color"])
                    for vert in face["verts"]:
                        v = get3dVert(vert, self.pos, self.rot, gameObject.pos)
                        
                        verts3d.append(v)
                    
                    #verts3d = [get3dVert(vert, self.pos, self.rot, gameObject.pos) for vert in face["verts"]]
                    #print(verts3d[0])
                    i=0
                    while i<len(verts3d):
                        
                        # if clipping
                        if verts3d[i][2] < 0:
                            sides=[]

                            # left vert
                            left = verts3d[i-1]

                            # right vert
                            right = verts3d[(i+1) % len(verts3d)]

                            # if left vert is not clipping
                            if left[2]>=minZ:
                                sides += [getZ(verts3d[i],left,minZ)]

                            # if right vert is not clipping
                            if right[2]>=minZ:
                                sides += [getZ(verts3d[i],right,minZ)]
                            verts3d = verts3d[:i]+sides+verts3d[i+1:]
                            i+=len(sides)-1;
                        i+=1

                    # Somehow, add this list as 1 face to big objects draw list
                    verts3d.append((face["color"]))
                    verts3d_faces.append(verts3d)
                    

                    
        # IF THERE ARE FACES TO DRAW
        if verts3d_faces:

            # depth buffer:
            #verts3d_s = []
            #verts3d.sort(key=getZOrder, )
            #for vert in verts3d:
                # sort so that less z is drawn last to get displayed
                # closer to camera
                

                
            
            for face in verts3d_faces:
                if len(face)>=3:
                    verts2d=[]
                    #print(face)
                    for n in range(len(face)-1):
                        vert = face[n]
                        #print(vert)
                        #print(vert)
                        verts2d.append(get2dVert(vert,
                                                 self.cx, self.cy,
                                                 self.projX, self.projY))
                        #print(face)
                        
                        """
                        verts2d.append(get2dVert(vert,
                                                 self.cx, self.cy,
                                                 self.projX, self.projY))
                        """
                    #print(face)
                    verts2d.append(face[len(face)-1]) # color
                    #print(face[3])
                    verts2d_faces.append(verts2d)
                    #print(verts2d_faces)

        #print(verts2d_faces)
        for face in verts2d_faces:
            #try:
            #print(face)
            #print(face)
            color = pygame.Color(face[len(face)-1])
            #print(color)
            #color = pygame.Color(200, 20, 20)
            pygame.draw.polygon(self.display, color, face)
            #except: pass

        pygame.display.flip()

    def setFov(self, fov): # fov in degrees
        self.fov = fov/180*pi; self.half_fov = self.fov/2
        
        self.projY = self.half_h/math.tan(self.half_fov)
        self.projX = self.half_w/math.tan(self.half_fov)/(self.w/self.h)



def getZ(A, B, newZ):
    if B[2]==A[2] or newZ<A[2] or newZ>B[2]: return None
    dx,dy,dz = B[0]-A[0],B[1]-A[1],B[2]-A[2]
    i=(newZ-A[2])/dz
    return [A[0]+dx*i, A[1]+dy*i, newZ]

def getZOrder(i):
    return i[2]
