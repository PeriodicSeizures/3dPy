#f1 = 300

#points = []
import pygame
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

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self.fov = 70

    def move(self, delta, key):
        speed = delta * 10
        
        if key[pygame.K_w]: self.z+=speed
        if key[pygame.K_s]: self.z-=speed
        if key[pygame.K_a]: self.x-=speed
        if key[pygame.K_d]: self.x+=speed

        if key[pygame.K_SPACE]: self.y+=speed
        if key[pygame.K_LSHIFT]: self.y-=speed

class Quad:
    """
    def __init__(self, vert1=None, vert2=None, vert3=None, vert4=None):
        self.rect = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self.rect[0][0] = vert1.get_x(); self.rect[0][1] = vert1.get_y(); self.rect[0][2] = vert1.get_z()
        self.rect[1][0] = vert1.get_x(); self.rect[0][1] = vert1.get_y(); self.rect[0][2] = vert1.get_z()
        self.rect[2][0] = vert1.get_x(); self.rect[0][1] = vert1.get_y(); self.rect[0][2] = vert1.get_z()
        self.rect[3][0] = vert1.get_x(); self.rect[0][1] = vert1.get_y(); self.rect[0][2] = vert1.get_z()
    def get_vertice(self, vert=None):
        return self.rect[vert][0], self.rect[vert][1], self.rect[vert][2]
    """
    def __init__(self, w, h, x, y, z, rx, ry, rz):
        self.width = w; self.height = h
        self.x = x; self.y = y; self.z = z
        self.rx = rx; self.ry = ry; self.rz = rz
        
