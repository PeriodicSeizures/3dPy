import pygame
import math
import math2d
import os
import objects as objs

pi = math.pi

"""

    Rotate a pt around

"""

def rotate2d(pos, rot): # new rotation is a float in radians for rotation
    x,y = pos
    s,c = math.sin(rot), math.cos(rot)
    return round(x*c+y*s,2), round(y*c+x*s,2)

"""
def rotate2d(pos, rot):
    x,y = pos
    s,c = rot #math.sin(rot), math.cos(rot)
    return x*c-y*s, y*c+x*s
"""


def get3dVert(vertex, originPos, originRot, targetPos):
    # WAS - FOR x,y,z
    x = vertex[0]-originPos[0]+targetPos[0]
    y = vertex[1]-originPos[1]+targetPos[1]
    z = vertex[2]-originPos[2]+targetPos[2]
	
    """
    rx = [math.sin(originRot[0]), math.cos(originRot[0])]
    ry = [math.sin(originRot[1]), math.cos(originRot[1])]
    """

    x,z = rotate2d([x,z], originRot[0]) #ry
    y,z = rotate2d([y,z], originRot[1]) #rx

    return [x,y,z]



def get2dVert(v, 
              cx, cy,
              projX, projY):
    
    #xr = v[2]*projX
    #yr = v[2]*projY
    #return cx+int(v[0]/xr), cy+int(v[1]/yr)
    """
    try:
        x = cx+int(v[0]/v[2]*projX)
    except:
        x = 10000

    try:
        y = cy+int(v[1]/v[2]*projY)
    except:
        y = 10000
    
    return x, y
    """
    
    return cx+int(v[0]/v[2]*projX), cy+int(v[1]/v[2]*projY)



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
                        
        self.pos = [0,0,0]; self.rot = [0,0]

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
	
        self.rot[0] = math2d.clamp(self.rot[0], 0, pi) #.5*pi, 1.5*pi)
	
        # Background color
        self.display.fill((255,255,255))
        
        for gameObject in gameObjects:
            if gameObject.meshFaces:
                
                for face in gameObject.meshFaces:
                    
                    verts3d = [get3dVert(vert, self.pos, self.rot, gameObject.pos) for vert in face["verts"]]
                    
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

                    if verts3d:
                        verts2d=[]
                        for vert in verts3d:
                            verts2d.append(get2dVert(vert,
                                                     self.cx, self.cy,
                                                     self.projX, self.projY))
                            
                    try:
                        color = pygame.Color(face["color"])
                        pygame.draw.polygon(self.display, color, verts2d)
                    except: pass

        pygame.display.flip()

    def setFov(self, fov): # fov in degrees
        self.fov = fov/180*pi; self.half_fov = self.fov/2
        
        self.projY = self.half_h/math.tan(self.half_fov)
        self.projX = self.half_w/math.tan(self.half_fov)/(self.w/self.h)



def getZ(A, B, newZ):
    if B[2]==A[2] or newZ<A[2] or newZ>B[2]: return None
    dx,dy,dz = B[0]-A[0],B[1]-A[1],B[2]-A[2]
    i=(newZ-A[2])/dz
    return A[0]+dx*i,A[1]+dy*i,newZ
