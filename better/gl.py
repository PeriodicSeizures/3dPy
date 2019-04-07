import pygame
import math
import random
import json

pi = math.pi

def rotate2d(pos,rad): x,y = pos; s,c = math.sin(rad), math.cos(rad); return x*c-y*s,y*c+x*s

class model:
    def __init__(self, name, pos, faces):
        self.name = name
        self.pos = pos
        self.faces = faces
        for face in faces:
            f = face["verts"]
            for vert in f:
                vert[0]+=1;vert[1]+=1;vert[2]+=1
        
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
            

    #def getVertsFromFace(self, face)
    
def get3dVert(vertex, camera):
    v = [vertex[0]-camera.x, vertex[1]-camera.y, vertex[2]-camera.z]
    
    v[0], v[2] = rotate2d((v[0],v[2]), camera.ry)
    v[1], v[2] = rotate2d((v[1],v[2]), camera.rx)

    return v

def get2dVert(vertex, display):
    f = 200/vertex[2]

    v = [(vertex[0]*f)+display.cx,
         (display.h-(vertex[1]*f)+display.cy)-display.h]

    return v

minZ = .4

class renderer:
    def __init__(self, w, h):
        self.objects = []
        pygame.event.get(); pygame.mouse.get_rel()
        self.currentInterval = 0
    
        self.w = w; self.h = h
        self.cx = w//2; self.cy = h//2

        self.display = pygame.display.set_mode((w,h))

        with open("map.json") as file:
            f = json.load(file)
            for mod in f:
                self.objects.append(model(mod["name"], mod["pos"], mod["faces"]))

    def render(self, clock, delta, camera):
        # clear screen before draw
        self.display.fill((255,255,255))
        
        #verts = [obj.getRawVerts() for obj in self.objects]
        for obj in self.objects:
            
            for face in obj.getRawFaces():
                verts3d = [get3dVert(vert, camera) for vert in face]
                
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

                #print(verts3d)

                if verts3d:
                    verts2d = [get2dVert(vert, self) for vert in verts3d]

                    verts2d.append(verts2d[0])

                #print(verts2d)

                try:
                    pygame.draw.polygon(self.display, (0,50,50), verts2d)
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

    def addObject(self, obj):
        self.objects.append(obj)



class camera:
    def __init__(self):
        self.x = 0; self.y = 0; self.z = 0
        self.rx = 0; self.ry = 0
        
    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel; x/=200; y/=200
            self.rx-=y; self.ry+=x
            
        # clamp rx rotation [-pi/2,pi/2]
        self.rx = clamp(self.rx, -pi/2, pi/2)
        
        #self.rx = max(min(self.rx, pi/2), -pi/2)
        
    def move(self, delta, key):
        speed = delta * 5

        x,y = speed*math.sin(self.ry), speed*math.cos(self.ry)
        
        if key[pygame.K_w]: self.x+=x; self.z+=y
        if key[pygame.K_s]: self.x-=x; self.z-=y
        if key[pygame.K_a]: self.x-=y; self.z+=x
        if key[pygame.K_d]: self.x+=y; self.z-=x
        
        if key[pygame.K_SPACE]: self.y+=speed
        if key[pygame.K_LSHIFT]: self.y-=speed

def clamp(num, small, big):
    return max(min(num, big), small)

def intersect(p0_x, p0_y, 
              p1_x, p1_y, 
              p2_x, p2_y, 
              p3_x, p3_y):

    s1_x = p1_x - p0_x
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x
    s2_y = p3_y - p2_y

    #float s, t;
    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
    t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)

    if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
        # Collision detected
        #if (i_x != None):
        #x = p0_x + (t * s1_x);
        #if (i_y != None):
        #y = p0_y + (t * s1_y);
        return (round(p0_x + (t * s1_x),3),
                round(p0_y + (t * s1_y),3))

    return None, None #false; # No collision

def getZ(A, B, newZ):
    if B[2]==A[2] or newZ<A[2] or newZ>B[2]: return None
    dx,dy,dz = B[0]-A[0],B[1]-A[1],B[2]-A[2]
    i=(newZ-A[2])/dz
    return A[0]+dx*i,A[1]+dy*i,newZ
