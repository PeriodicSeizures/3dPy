import pygame
import gl_objects

pygame.init()
w = 800; h = 800; a = w//2; b = h//2
display = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

quads = [gl_objects.Quad(1,1,0,0,1,0,0,0)]

camera = gl_objects.Camera()

running = True
while(running):
    delta = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False; break

    display.fill((255,255,255))
    
    print(camera.z)
    
    
    # with quad Ry change, x,z (quad) is changed, 
    
    for quad in quads:

#       https://youtu.be/g4E9iq0BixA?t=107
#       https://www.siggraph.org/education/materials/HyperGraph/modeling/mod_tran/3drota.htm

        x = quad.x
        y = quad.y
        z = quad.z

        x-=camera.x; y-=camera.y; z-=camera.z # instance quad pt, is copied because changes dont need to be made to original

        f = 200/z # scale to transfer z_quad pt to x,y screen
        
        
        

        x1 = (x-(quad.width/2)) * f
        y1 = (y-(quad.height/2)) * f

        x2 = (x+(quad.width/2)) * f
        y2 = (y-(quad.height/2)) * f

        x3 = (x+(quad.width/2)) * f
        y3 = (y+(quad.height/2)) * f
        
        x4 = (x-(quad.width/2)) * f
        y4 = (y+(quad.height/2)) * f

        pygame.draw.aaline(display, (0,0,0), (x1+a,y1+b), (x2+a,y2+b), 1)
        pygame.draw.aaline(display, (0,0,0), (x2+a,y2+b), (x3+a,y3+b), 1)
        pygame.draw.aaline(display, (0,0,0), (x3+a,y3+b), (x4+a,y4+b), 1)
        pygame.draw.aaline(display, (0,0,0), (x4+a,y4+b), (x1+a,y1+b), 1)

    if running:
        pygame.display.flip()

        key = pygame.key.get_pressed()
        camera.move(delta, key)

pygame.quit()
