import pygame
import gl_objects

pygame.init()

class Display:
    def __init__(self):
        self.display = pygame.display.set_mode((800,600))
        pygame.display.set_caption("test3dGraphics")
        self.display.fill((255,255,255))

def render(display, quads, camera):
    for quad in quads:
        scale = 300 / (300 + quad.get_z())

        x1 = (quad.get_x()-(quad.get_width()/2)) * scale
        y1 = (quad.get_y()-(quad.get_height()/2)) * scale

        x2 = (quad.get_x()+(quad.get_width()/2)) * scale
        y2 = (quad.get_y()-(quad.get_height()/2)) * scale

        x3 = (quad.get_x()+(quad.get_width()/2)) * scale
        y3 = (quad.get_y()+(quad.get_height()/2)) * scale
        
        x4 = (quad.get_x()-(quad.get_width()/2)) * scale
        y4 = (quad.get_y()+(quad.get_height()/2)) * scale

                
        pygame.draw.aaline(display.display, (0,0,0), (x1,y1), (x2,y2), 1)
        pygame.draw.aaline(display.display, (0,0,0), (x2,y2), (x3,y3), 1)
        pygame.draw.aaline(display.display, (0,0,0), (x3,y3), (x4,y4), 1)
        pygame.draw.aaline(display.display, (0,0,0), (x4,y4), (x1,y1), 1)


        pygame.display.flip()


    
display = Display()
quads = [gl_objects.Quad(1,1,0,0,1,0,0,0)]
camera = gl_objects.Camera()

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
    if running:
        render(display, quads, camera)

