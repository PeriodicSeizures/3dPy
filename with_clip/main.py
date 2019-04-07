import gl
import math
import pygame

pygame.init()
clock = pygame.time.Clock()

renderer = gl.renderer(400, 400)
camera = gl.camera()

pygame.event.get(); pygame.mouse.get_rel()
def lock_mouse():
    pygame.mouse.set_visible(0); pygame.event.set_grab(1)

focus = True

run = True
while(run):
    delta = clock.tick()/1000
    #print(camera.x,camera.y,camera.z)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False; break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit()

            if event.key == pygame.K_f:
                if focus:
                    pygame.event.set_grab(0)
                    pygame.mouse.set_visible(1)
                else:
                    lock_mouse()
                focus = not focus
        if focus:
            camera.events(event)
            
    if run:
        key = pygame.key.get_pressed()
        camera.move(delta, key)

        renderer.render(clock, delta, camera)
