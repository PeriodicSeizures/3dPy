import gl
import pygame
#import physics
import objects as objs
import copy
import math

class Player:
    def __init__(self):
        self.pos = [0,0,0]
        
        self.rot = [0,0]

        self.meshFaces = []
        self.colliderFaces = []
        
        self.isKinetic = False
        self.velocity = [0,0,0]
        self.useGravity = True
        self.grounded = False

    def update(self):
        #key = pygame.key.get_pressed()
        self.move(pygame.key.get_pressed())

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            # scales translation of mouse to camera rotation
            x,y = event.rel; x/=200; y/=200
            game.rot[0]+=y; game.rot[1]+=x ### ry was (-) ###
	
    def move(self, key):
        #speed = delta * 5
        speed = 2
    
        

        """
            MOVE PLAYER:
        """

        if self.isKinetic: # if physics enabled on object
            x,y = speed*math.sin(self.rot[1]), speed*math.cos(self.rot[1])
            # by physics
            if key[pygame.K_SPACE] and self.grounded:
                self.pos[1] = 3
                self.grounded = False
                
            if key[pygame.K_w]: self.velocity[0]=-x; self.velocity[2]=-y
            if key[pygame.K_s]: self.velocity[0]=x;  self.velocity[2]=y
            if key[pygame.K_a]: self.velocity[0]=-y; self.velocity[2]=x
            if key[pygame.K_d]: self.velocity[0]=y;  self.velocity[2]=-x
        else: # if physics disabled on object
            x,y = speed*math.sin(self.rot[1])*delta, speed*math.cos(self.rot[1])*delta
            # by position
            if key[pygame.K_SPACE] and self.grounded:
                self.pos[1] += delta*speed
                self.grounded = False
                
            if key[pygame.K_w]: self.pos[0]-=x; self.pos[2]-=y
            if key[pygame.K_s]: self.pos[0]+=x;  self.pos[2]+=y
            if key[pygame.K_a]: self.pos[0]-=y; self.pos[2]+=x
            if key[pygame.K_d]: self.pos[0]+=y;  self.pos[2]-=x

        """
            MOVE CAMERA from Player
        """

        game.pos = copy.deepcopy(self.pos)

        """
            ROTATE PLAYER from Renderer
	    
	    should be changed to when camera rotated enough, and relative rotation is far enough, then rotate player
        """

        self.rot = copy.deepcopy(game.rot)



pygame.init()
clock = pygame.time.Clock()

game = gl.Renderer(800, 600)
#physix = physics.physics()
player = Player()

focus = True
fixedUpdateTime = 0

objs.objects.append(player)

def lockMouse():
    pygame.event.get(); pygame.mouse.get_rel()
    pygame.mouse.set_visible(0); pygame.event.set_grab(1)

	
def unlockMouse():
    pygame.event.get(); pygame.mouse.get_rel()
    pygame.mouse.set_visible(1); pygame.event.set_grab(0)

lockMouse()

run = True
fpsInterval = 0
while(run):
    delta = clock.tick()/1000   # time it took last frame

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.display.quit(); pygame.quit(); run = False; break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.display.quit(); pygame.quit(); run = False; break
            
            if event.key == pygame.K_f:
                if focus:
                    unlockMouse()
                else:
                    lockMouse()
                focus = not focus
            #player.camera.events()
        if focus:
            player.events(event)
            #player.events(event)

    if fixedUpdateTime>=.01333333: # 60 tps
        #physix.fixedUpdate(delta, objs.objects)
        game.update(objs.objects)
        fixedUpdateTime=0
    
    
    fixedUpdateTime+=delta
    
    player.update()
    fpsInterval+=delta
    #print("this is being printed to simulate lagg")
    if fpsInterval>=1:
        #print("disp")
        fpsInterval=0
        pygame.display.set_caption("Game engine | %.00f fps" % (clock.get_fps()))
