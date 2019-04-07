import pygame
import math
import random
import json

pi = math.pi

def rotate2d(pos,rad): x,y = pos; s,c = math.sin(rad), math.cos(rad); return x*c-y*s,y*c+x*s

class object:
    def __init__(self, name, pos, faces):
        self.name = name
        self.pos = pos
        self.faces = faces

with open("test.json") as file: # Need to redo the key finds in drawing
                                # methods
    f = json.load(file)
    objects = []
    for obj_name, value in f.items():
        objects.append(object(obj_name, f[obj_name]["pos"], f[obj_name]["faces"]))
    file.close()
    #print(objects[0].faces)

class renderer:
    def __init__(self, w, h):
        self.w = w; self.h = h
        self.cx = w//2; self.cy = h//2

        self.display = pygame.display.set_mode((w,h))

        self.currentInterval = 0
    def render(self, clock, delta, camera):
        # clear screen before draw
        self.display.fill((255,255,255))
        minZ = .4
	
        # draw all objects
        for obj in objects:

            vert_list=[]
            for face in obj.faces:
                for v in face["verts"]:
                    #print(v)
                    vert_list.append(getWorldCoord(v, camera))

            #vert_list = [(getWorldCoord(v, camera) for v in face["verts"]) for face in obj.faces]
            #print(vert_list)
            
            #for f in range(len(obj.faces)):
            for face in obj.faces:
                
                verts = []
                #for face in obj.faces[f]:
                for v in face["verts"]:
                    print(v)
                    verts.append(vert_list[v])

                #verts = [(vert_list[v] for v in face) for face in obj.faces[f]["verts"]]
                print(verts)
                # clip verts

                # iterate the verts in faces
                i=0
                while i<len(verts):
                    # if vert is clipping
                    if verts[i][2] < minZ:
                        sides=[]

                        # left vert
                        left = verts[i-1]

                        # right vert
                        right = verts[(i+1) %len(verts)]

                        # if left vert is not clipping
                        if left[2] >= minZ:
                            sides += [getZ(verts[i], left, minZ)]

                        # if right vert is not clipping
                        if right[2] >= minZ:
                            sides += [getZ(verts[i], right, minZ)]
                        verts = verts[:i]+sides+verts[i+1:]
                        i+=len(sides)-1;
                    i+=1

                screen_verts.append(screen_verts[0])
                if len(screen_verts)>4:
                    try:
                        pygame.draw.polygon(self.display, (0,50,50), screen_verts)
                    except:
                        print("didnt draw; some error occurred :/")
					
        self.currentInterval+=delta
        if self.currentInterval>=1:
            self.currentInterval=0
            pygame.display.set_caption("3dQuadDrawing | %.00f fps" % (clock.get_fps()))

        pygame.display.flip()
    def addObject(obj):
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

def getDisplayCoord(vertex, display):
    f = 200/vertex[2]

    v = [ (vertex[0]*f)+display.cx, (display.h-(vertex[1]*f)+display.cy)-display.h ]
    
    return v

def getWorldCoord(vertex, camera):
    v = [vertex[0], vertex[1], vertex[2]]
    
    v[0] -= camera.x; v[1] -= camera.y; v[2] -= camera.z

    v[0], v[2] = rotate2d((v[0],v[2]), camera.ry)
    v[1], v[2] = rotate2d((v[1],v[2]), camera.rx)
    return v
    
