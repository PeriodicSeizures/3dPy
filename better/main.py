import gl
import math
import pygame

pygame.init()
clock = pygame.time.Clock()

game = gl.renderer(400, 400)
camera = gl.camera()

focus = True

game.lockMouse()

run = True
while(run):
    delta = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.display.quit(); pygame.quit(); run = False; break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.display.quit(); pygame.quit(); run = False; break
            
            if event.key == pygame.K_f:
                if focus:
                    game.unlockMouse()
                else:
                    game.lockMouse()
                focus = not focus
        if focus:
            camera.events(event)
            
    if run:
        key = pygame.key.get_pressed()
        camera.move(delta, key)

        game.render(clock, delta, camera)
