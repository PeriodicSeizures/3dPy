import gl
import pygame
import physics

pygame.init()
clock = pygame.time.Clock()

game = gl.Renderer(800, 600)
camera = gl.Camera()
#player = gl.Player([1,1,1])
physix = physics.physics()

focus = True

game.lockMouse()

run = True
while(run):
    delta = clock.tick()/1000

    # Events
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
            camera.events(event)
            #player.events(event)

    # Updates/mEvents:
    if run:
        #player.move(delta, key)
        # Just move all key events for testing into Player loop if
        # are player specific
        
        key = pygame.key.get_pressed()
        camera.move(delta, key)
        camera.update()

        game.render(clock, delta, camera)#player.camera)
        physix.update(delta)
