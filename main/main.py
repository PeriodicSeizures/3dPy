import gl
import math
import pygame
import physics

pygame.init()
clock = pygame.time.Clock()

game = gl.Renderer(800, 600)
#camera = gl.Camera()
player = gl.Player([1,1,1])
physix = physics.physics()

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
            #player.camera.events()
        if focus:
            #camera.events(event)
            player.events(event)
            
    if run:
        key = pygame.key.get_pressed()
        #camera.move(delta, key)
        player.move(delta, key)
        # Just move all key events for testing into Player loop if
        # are player specific
        

        game.render(clock, delta, player.camera)
        physix.update(delta)
