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
                isFirstLogged = False
                first = []
                """

                Possible solution to clipping:

                    go through every face:
					
						if face has at least 1 vert where f > 0:
						
							draw verts with clamp adjusted in screen
							
						else:
						
							dont draw the face
                """
				
                for vert in tri:
                    draw = True
                    vertex = [vert[0],vert[1],vert[2]]
                    #print(vertex)
                    vertex[0] -= camera.x; vertex[1] -= camera.y; vertex[2] -= camera.z

                    # clipping issue
                    
                    vertex[0], vertex[2] = rotate2d((vertex[0],vertex[2]), camera.ry)
                    vertex[1], vertex[2] = rotate2d((vertex[1],vertex[2]), camera.rx)

                    #print(math.degrees(camera.ry))

                    f = 200/vertex[2]
                    #print(f)

                    
                    ####################################
                    #################################### START (of test; not)
                    ####################################       (actual plot)


                    vt = [tri[0][0],tri[0][1],tri[0][2]]
                    #print(vertex)
                    vt[0] -= camera.x; vt[1] -= camera.y; vt[2] -= camera.z

                    # clipping issue
                    
                    vt[0], vt[2] = rotate2d((vt[0],vt[2]), camera.ry)
                    vt[1], vt[2] = rotate2d((vt[1],vt[2]), camera.rx)

                    #print(math.degrees(camera.ry))

                    f = 200/vt[2]

                    print(f)
                    
                    """

                    As the vertex rotates around the camera, the f value will reach +/- infinity if
                    it continues rotating.

                    When the angle reaches a quadrantal angle in a special case, it will toggle the
                    sign of the f and continue on from there, changing the appearance and
                    visual location of the vertex.
                    

                    """

                    
                    ####################################
                    ####################################  END
                    ####################################

                    
                    if f>0:
                        pass
                    else:
                        pass
                        #draw = False
        
                if draw:
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
                            #clamp((vertex[0]*f)+self.cx,0,self.w),

                            (self.h-(vertex[1]*f)+self.cy)-self.h
                            #clamp((self.h-(vertex[1]*f)+self.cy)-self.h,0,self.h)
                        ]
                        
                        #if f > 0:
                        if True:
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
                    if len(screen_verts)>3:
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

# undefined, but should be called only if invalid vert is found
def screenClamp(verts, renderer):
    #m = (y1-y0)/(x1-x0)
    #m = ()/()

    # ALL of below just correctly assigns x/y to work with
    for i in range(0,len(verts)-1):
        if verts[i][0] < 0:
            m=(poly[i][1]-poly[i+1][1])/poly[i][0]-poly[i+1][0]
        elif poly[i][0] > renderer.w:
            
    if tri[0][0]<0 or <0: # vert consists of
        if x<0:
            x = x0; y = y0
        else:
            x = x1; y = y1

    elif x0>renderer.w or x1>renderer.w:
        if x0>renderer.w:
            y = x0; y = y0
        else:
            x = x1; y = y1
    b = y - s*x
    # set x
    #x = 0 if x0<=0 or x1<=0 elif x0>=renderer.w or x1>=renderer.w renderer.w else 
    x = 0 if x0<=0 or x1<=0 elif x0>=renderer.w or x1>=renderer.w renderer.w

    # get variating y-pos
    y = y0-((y1-y0)/(x1-x0)) * x0

    # set to 0 or renderer.w ; depends on line end

    # reprerer.w correct position being MAX or 0
    # limit clip to position
	
    # no else for verticalbecause  camera rotation is limited vertically?
    # unless face does clip vertically, then include an elif...
	
    
