import pygame
import math
import random

pi = math.pi

def rotate2d(pos,rad): x,y = pos; s,c = math.sin(rad), math.cos(rad); return x*c-y*s,y*c+x*s

#print(rotate2d([], ))

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
                z_data = []
                isFirstLogged = False
                first = []

                for vert in tri:
                #for i in range(0,len(tri)):
                    vertex = [vert[0],vert[1],vert[2]]
                    #print(vertex)
                    vertex[0] -= camera.x; vertex[1] -= camera.y; vertex[2] -= camera.z

                    vertex[0], vertex[2] = rotate2d((vertex[0],vertex[2]), camera.ry)
                    vertex[1], vertex[2] = rotate2d((vertex[1],vertex[2]), camera.rx)

                    f = 200/vertex[2]

                    z_data.append(vertex[2])
                    #vertex[3] = f
                                            
                    # +self.cx,(self.h-screen_verts[0][1]+self.cy)-self.h

                    v = [
                        (vertex[0]*f)+self.cx,
                        #clamp((vertex[0]*f)+self.cx,0,self.w),

                        (self.h-(vertex[1]*f)+self.cy)-self.h
                        #clamp((self.h-(vertex[1]*f)+self.cy)-self.h,0,self.h)
                    ]
                    
                    if True: #f > 0:
                        if not isFirstLogged:
                            first = v
                            isFirstLogged = True

                        screen_verts.append(v)

                """
                # If at least partially in camera view
                if not ( (screen_verts[0][0] < 0 and screen_verts[1][0] < 0 and screen_verts[2][0] < 0) or
                    (screen_verts[0][0] > self.w and screen_verts[1][0] > self.w and screen_verts[2][0] > self.w) or
                    (screen_verts[0][1] < 0 and screen_verts[1][1] < 0 and screen_verts[2][1] < 0) or
                    (screen_verts[0][1] > self.h and screen_verts[1][1] > self.h and screen_verts[2][1] > self.h) ):

                    # If there are verts whose f is negative:
                    for vert in screen_verts:
                        if vert[2] < 0:
                            abs(vert[0]) > 
                    
                    if ( (screen_verts[0][0] < 0 and screen_verts[1][0] < 0 and screen_verts[2][0] < 0) or
                        (screen_verts[0][0] > self.w and screen_verts[1][0] > self.w and screen_verts[2][0] > self.w) or
                        (screen_verts[0][1] < 0 and screen_verts[1][1] < 0 and screen_verts[2][1] < 0) or
                        (screen_verts[0][1] > self.h and screen_verts[1][1] > self.h and screen_verts[2][1] > self.h) ):



                """
                """
                for i in range(len(z_data)):
                    if z_data[i] < 0:
                        # Find the largest distance to horizontal screen\
                        _x = screen_verts[i][0]
                        _x = max(screen_verts[i][0],
                                 screen_verts[i][0]-self.w)
                        
                        _y = max(screen_verts[i][1],
                                 screen_verts[i][1]-self.h)

                        screen_verts[i][0]=_x
                        screen_verts[i][1]=_y
                """

                        

                        
                    
                print(vertex[2], round(camera.ry*180/3.1415926,1))    

                screen_verts.append(first)
                if len(screen_verts)>4:
                    pygame.draw.polygon(self.display, (0,50,50), screen_verts)
                    #pygame.draw.circle(self.display, (255,0,0), (int(screen_verts[0][0]),int(screen_verts[0][1])), 5, 0)
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

"""

var = {"a":"4"}

"""

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
