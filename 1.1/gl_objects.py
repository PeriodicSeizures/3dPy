#f1 = 300

#points = []
import pygame
import math
"""
class Vertice:
    def __init__(self, x=None, y=None, z=None):
        try:
            self.x = x
            self.y = y
            self.z = z
        except:
            print("[Err] while creating new Vertice()")
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
"""

pi = math.pi

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.rx = 0
        self.ry = 0
        self.fov = 70

    def events(self,event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel; x/=200; y/=200
            self.rx-=y; self.ry+=x
            #print("%.0f %.0f" %(round(self.rx*180/pi),(self.ry*180/pi)))
        self.rx = max(min(self.rx, pi/2), -pi/2)

    def move(self, delta, key):
        speed = delta * 10

        x,y = speed*math.sin(self.ry), speed*math.cos(self.ry)
        
        if key[pygame.K_w]: self.x+=x; self.z+=y
        if key[pygame.K_s]: self.x-=x; self.z-=y
        if key[pygame.K_a]: self.x-=y; self.z+=x
        if key[pygame.K_d]: self.x+=y; self.z-=x
        
        if key[pygame.K_SPACE]: self.y+=speed
        if key[pygame.K_LSHIFT]: self.y-=speed



class Quad:
    def __init__(self, size, _x, _y, _z, rx, ry):
        self.size = size
        self.x = _x; self.y = _y; self.z = _z
        self.rx = rx; self.ry = ry

        self.base_2d_verts = [
            [-(self.size/2), -(self.size/2)],
            [ (self.size/2), -(self.size/2)],
            [ (self.size/2),  (self.size/2)],
            [-(self.size/2),  (self.size/2)]
        ]
        
    def update_verts(self):
        self.rotated_base_verts = []
        self.verts = []

        # upper-left vert:
        # will always be at
        for v in range(4):
            x = self.base_2d_verts[v][0]; y = self.base_2d_verts[v][1]; z = 0

            # find the location of vert rotated around 0,0,0
            vert = [
                x*math.cos(self.ry) - y*math.sin(self.rx)*math.sin(self.ry),# - z*math.cos(rx)*math.sin(ry),
                y*math.cos(self.rx),# - z*math.sin(rx),
                x*math.sin(self.ry) + y*math.sin(self.rx)*math.cos(self.ry)# + z*math.cos(rx)*math.cos(ry)
                ]

            # add to base rotated list
            self.rotated_base_verts.append(vert)


        # find real location of vert on grid
        for v in range(4):
            x = self.rotated_base_verts[v][0]; y = self.rotated_base_verts[v][1]; z = self.rotated_base_verts[v][2]

            vert = [
                x+self.x,
                y+self.y,
                z+self.z
                ]

            self.verts.append(vert)

    def get_verts_transformed(self, _x, _y, _z):
        final_verts = []

        # find real location of vert on grid
        for v in range(4):
            x = self.verts[v][0]; y = self.verts[v][1]; z = self.verts[v][2]

            vert = [
                x+_x,
                y+_y,
                z+_z
                ]

            final_verts.append(vert)

        return final_verts
