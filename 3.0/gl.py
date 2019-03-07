import pygame
import math

pi = math.pi

class gl_engine:
    def __init__(self, w, h):
        self.objects = []
        self.size = [w,h]
        self.w = w; self.h = h
        self.cx = w//2; self.cy = h//2

        self.display = pygame.display.set_mode((w,h))

        self.currentInterval=0
    def update(self, clock, delta):
        # draw all objects
        for obj in self.objects:
            for tri in obj:
                screen_verts = []
                # modify this here
                for vert in tri:
                    f = 200/vert[0]
                    screen_verts.append([
                        vert[0]*f,
                        vert[1]*f
                    ])
                    
                pygame.draw.polygon(display, (255*(q/len(quads)),0,50), [
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

        self.currentInterval+=delta
        if self.currentInterval>=1:
            self.currentInterval=0
            pygame.display.set_caption("3dQuadDrawing | %.00f fps" % (clock.get_fps()))

    def addObject(obj):
        self.objects.append(obj)
##    def addObjectArray(obj):
##        for i in obj:
##            self.objects.append(i)


class object:
    def __init__(self, tris):
        self.tris = tris

class tri:
    def __init__(self, verts):
        self.verts = verts

class camera:
    def __init__(self):
        self.x = 0; self.y = 0; self.z = 0
        self.rx = 0; self.ry = 0
    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel; x/=200; y/=200
            self.rx-=y; self.ry+=x
        self.rx = max(min(self.rx, pi/2), -pi/2)
    def move(self, delta, key):
        speed = delta * 5

        x,y = speed*math.sin(self.ry), speed*math.cos(self.ry)
        
        if key[pygame.K_w]: self.x+=x; self.z+=y
        if key[pygame.K_s]: self.x-=x; self.z-=y
        if key[pygame.K_a]: self.x-=y; self.z+=x
        if key[pygame.K_d]: self.x+=y; self.z-=x
        
        if key[pygame.K_SPACE]: self.y+=speed
        if key[pygame.K_LSHIFT]: self.y-=speed
