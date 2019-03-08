import pygame
import math
import random

pi = math.pi

def rotate2d(pos,rad): x,y = pos; s,c = math.sin(rad), math.cos(rad); return x*c-y*s,y*c+x*s

# renderer
#   is the gameplay screen
#   will get a list of objects to render
#   caption: fps
#   
class renderer:
    def __init__(self, w, h):
        self.objects = []
        self.size = [w,h]
        self.w = w; self.h = h
        self.cx = w//2; self.cy = h//2

        self.display = pygame.display.set_mode((w,h))

        self.currentInterval = 0
    def render(self, clock, delta, camera):
        # clear screen before draw
        self.display.fill((255,255,255))
        
        # draw all objects
        for obj in self.objects:
            for tri in obj:
                screen_verts = []
                isFirstLogged = False
                first = []
                for vert in tri:
                #for v in range(0,len(tri)):
                    vertex = [vert[0],vert[1],vert[2]]
                    #print(vertex)
                    vertex[0] -= camera.x; vertex[1] -= camera.y; vertex[2] -= camera.z

                    # clipping issue
                    
                    vertex[0], vertex[2] = rotate2d((vertex[0],vertex[2]), camera.ry)
                    vertex[1], vertex[2] = rotate2d((vertex[1],vertex[2]), camera.rx)

                    f = 200/vertex[2]
                    
                    # +self.cx,(self.h-screen_verts[0][1]+self.cy)-self.h

                    v = [
                        (vertex[0]*f)+self.cx,
                        (self.h-(vertex[1]*f)+self.cy)-self.h
                    ]
                    
                    if f > 0:
                        if not isFirstLogged:
                            first = v
                            isFirstLogged = True

                        screen_verts.append(v)
                            
                        

                    """
                    f = 200/vertex[2] # z distance reciprocal

                    screen_verts.append([
                        vertex[0]*f,
                        vertex[1]*f
                    ])

                    # In order to fix clipping / mirroring problem,
                    # need to remove vert which f < 0
                    """
                # random.randint(1,21)*5,
                r = random.randint(100,255)
                g = random.randint(100,255)
                b = random.randint(100,255)
                #255*(q/len(quads)),0,50

                screen_verts.append(first)
                if len(screen_verts)>=3:
                    pygame.draw.polygon(self.display, (0,50,50), screen_verts)
                    #print("drawing poly")
                    
                """
                pygame.draw.polygon(self.display, (r,g,b), [
                    (
                        screen_verts[0][0]+self.cx,(self.h-screen_verts[0][1]+self.cy)-self.h
                    ),
                    (
                        screen_verts[1][0]+self.cx,(self.h-screen_verts[1][1]+self.cy)-self.h
                    ),
                    (
                        screen_verts[2][0]+self.cx,(self.h-screen_verts[2][1]+self.cy)-self.h
                    ),
                    (
                        screen_verts[0][0]+self.cx,(self.h-screen_verts[0][1]+self.cy)-self.h
                    ),
                ], 0)
                """
        self.currentInterval+=delta
        if self.currentInterval>=1:
            self.currentInterval=0
            pygame.display.set_caption("3dQuadDrawing | %.00f fps" % (clock.get_fps()))

        pygame.display.flip()
    def addObject(obj):
        self.objects.append(obj)
        
    def addObjectArray(self, objects): # take a list of objects:
        for obj in objects: # add each object
            self.objects.append(obj)

# https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
            

### object contains a list of tri
##class object:
##    def __init__(self, tris):
##        self.tris = tris
##
### tri is the basic shape
### has 3 verts
##class tri:
##    def __init__(self, verts):
##        self.verts = verts

# world navigator
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
