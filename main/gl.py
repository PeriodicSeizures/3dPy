import pygame
import math
import random
import json
import math2d
import os
import copy

pi = math.pi

def rotate2d(pos, rot):
    x,y = pos
    s,c = rot #math.sin(rot), math.cos(rot)
    return x*c-y*s, y*c+x*s

class GameObject:
    #def __init__(self, name, pos, faces):
    def __init__(self, gameObject):
        self.name = gameObject["name"]
        self.pos = gameObject["pos"]
        self.faces = []
        
        self.isKinetic = gameObject["isKinetic"]
        self.velocity = [0,0,0]
        self.useGravity = True
        self.isKinematic = False
        self.grounded = False
        
        if "faces" in gameObject:
            self.faces = gameObject["faces"]
            
    def getRawVerts(self):
        v = []
        for face in self.faces:
            for vert in face["verts"]:
                v.append(vert)
        return v

    def getRawFaces(self):
        r_faces = []
        for face in self.faces:
            r_faces.append(face["verts"])
        return r_faces



gameObjects = []
with open("objects.json") as file:
    f = json.load(file)
    for gameObject in f:
        gameObjects.append(GameObject(gameObject)) #["name"], mod["pos"], mod["faces"]))



def get3dVert(v, camera, gameObjectPos):
    # WAS - FOR x,y,z
    x,y,z = v[0]-camera.pos[0]+gameObjectPos[0], v[1]-camera.pos[1]+gameObjectPos[1], v[2]-camera.pos[2]+gameObjectPos[2]

    x,z = rotate2d([x,z], camera.ry)
    y,z = rotate2d([y,z], camera.rx)

    return [x,y,z]



def get2dVert(v, 
              cx, cy,
              projX, projY):
    
    #xr = v[2]*projX
    #yr = v[2]*projY
    #return cx+int(v[0]/xr), cy+int(v[1]/yr)
    
    return cx+int(v[0]/v[2]*projX), cy+int(v[1]/v[2]*projY)



minZ = .1


class Renderer:
    def __init__(self, w, h):
        
        pygame.event.get(); pygame.mouse.get_rel()
        self.currentInterval = 0

        self.fov = 90/180*math.pi; self.half_fov = self.fov/2
        self.half_w, self.half_h = w/2,h/2
        self.projY = self.half_h/math.tan(self.half_fov)
        self.projX = self.half_w/math.tan(self.half_fov)/(w/h)

        self.w = w; self.h = h
        self.cx = w//2; self.cy = h//2

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.display = pygame.display.set_mode((w,h))


    def render(self, clock, delta, caster):
        # clear screen before draw
        self.display.fill((255,255,255))
        
        for gameObject in gameObjects:
            if gameObject.faces:
                
                for face in gameObject.getRawFaces():
                    verts3d = [get3dVert(vert, caster, gameObject.pos) for vert in face]                    
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
                        pygame.draw.polygon(self.display, (0, 127, 50), verts2d)
                    except: pass

        self.currentInterval+=delta
        if self.currentInterval>=1:
            self.currentInterval=0
            pygame.display.set_caption("3dTriEngine | %.00f fps" % (clock.get_fps()))

        pygame.display.flip()


    def lockMouse(self):
        pygame.mouse.set_visible(0); pygame.event.set_grab(1)

        
    def unlockMouse(self):
        pygame.mouse.set_visible(1); pygame.event.set_grab(0)


    def addObject(self, gameObject):
        self.objects.append(gameObject)



class Camera:
    def __init__(self):
        for o in gameObjects:
            if o.name == "Player":
                self.gameObject = o; break
        
        self.pos = copy.deepcopy(self.gameObject.pos)
        
        self.rot = [0,0]
        self.update_rot()

    def update(self):
        self.rot[0] = math2d.clamp(self.rot[0], .5*pi, 1.5*pi)
        #print(self.rot[0])
        
        self.pos = [self.gameObject.pos[0],
                    self.gameObject.pos[1]+1,
                    self.gameObject.pos[2]]
        #print(self.gameObject.velocity[1])
        
    def update_rot(self):
        # THIS IS ONLY FOR PRE COMPUTED VALUES FOR rotate2d
        self.rx = [math.sin(self.rot[0]), math.cos(self.rot[0])]
        self.ry = [math.sin(self.rot[1]), math.cos(self.rot[1])]
      
    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel; x/=200; y/=200
            self.rot[0]+=y; self.rot[1]-=x ########################## rx was - ########################
            self.update_rot()

    def move(self, delta, key):
        print(self.gameObject.pos)
        #speed = delta * 5
        speed = 2

        #print(self.gameObject.grounded)
    
        if key[pygame.K_SPACE] and self.gameObject.grounded:
            self.gameObject.velocity[1] = 1
            print("Jumped")
        
        x,y = speed*math.sin(self.rot[1]), speed*math.cos(self.rot[1])
        
        if key[pygame.K_w]: self.gameObject.velocity[0]=-x; self.gameObject.velocity[2]=-y
        if key[pygame.K_s]: self.gameObject.velocity[0]=x;  self.gameObject.velocity[2]=y
        if key[pygame.K_a]: self.gameObject.velocity[0]=-y; self.gameObject.velocity[2]=x
        if key[pygame.K_d]: self.gameObject.velocity[0]=y;  self.gameObject.velocity[2]=-x

        """
        if key[pygame.K_SPACE]: self.gameObject.pos[1]+=speed
        if key[pygame.K_LSHIFT]: self.gameObject.pos[1]-=speed
        
        x,y = speed*math.sin(self.rot[1]), speed*math.cos(self.rot[1])
        if key[pygame.K_w]: self.gameObject.pos[0]-=x; self.gameObject.pos[2]-=y
        if key[pygame.K_s]: self.gameObject.pos[0]+=x; self.gameObject.pos[2]+=y
        if key[pygame.K_a]: self.gameObject.pos[0]-=y; self.gameObject.pos[2]+=x
        if key[pygame.K_d]: self.gameObject.pos[0]+=y; self.gameObject.pos[2]-=x
        """
        


def getZ(A, B, newZ):
    if B[2]==A[2] or newZ<A[2] or newZ>B[2]: return None
    dx,dy,dz = B[0]-A[0],B[1]-A[1],B[2]-A[2]
    i=(newZ-A[2])/dz
    return A[0]+dx*i,A[1]+dy*i,newZ
