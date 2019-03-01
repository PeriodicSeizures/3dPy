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
    
    for quad in quads:

#       https://youtu.be/g4E9iq0BixA?t=107

        x = quad.x
        y = quad.y
        z = quad.z

        x-=camera.x; y-=camera.y; z-=camera.z

        f = 200/z

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
