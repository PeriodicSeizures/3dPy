"""

How to wrap several classes under 1 type:

like a camera + gl_screen under 1 larger *game*


"""


import gl
import math
import pygame
import json

pygame.init()
clock = pygame.time.Clock()

renderer = gl.renderer(600, 600)
camera = gl.camera()

with open("map-example0.json") as f:
    objects = json.load(f)
    renderer.addObjectArray(objects)

pygame.event.get(); pygame.mouse.get_rel()
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
                    pygame.event.set_grab(1)
                    pygame.mouse.set_visible(0)
                focus = not focus
        if focus:
            camera.events(event)
            
    if run:
        key = pygame.key.get_pressed()
        camera.move(delta, key)

        renderer.render(clock, delta, camera)
