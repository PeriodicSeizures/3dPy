import gl
import math
import pygame
import json

pygame.init()
clock = pygame.time.Clock()

renderer = gl.renderer(600, 600)
camera = gl.camera()

with open("map.json") as f:
    objects = json.load(f)
    renderer.addObjectArray(objects)
    #print(objects)

run = True
while(run):
    delta = clock.tick()/1000
    renderer.render(clock, delta)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False; break
        
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
