import gl
import pygame
import physics
import objects as objs
import copy
import math
import vector

class Player:
    def __init__(self):
        self.pos = vector.Vector3(1,1,1)
        
        self.rot = vector.Vector2()

        self.meshFaces = []
        self.colliderFaces = []
        
        self.isKinetic = True
        self.velocity = vector.Vector3()
        self.useGravity = True
        self.grounded = False

        self.fixedTime = .01
        self.t = 0

    def update(self): #, delta):
        #key = pygame.key.get_pressed()
        print(round(self.pos[1],5),self.velocity[1])
        self.move(pygame.key.get_pressed())
        """
        self.move(delta, pygame.key.get_pressed())
        if self.t >= self.fixedTime:
            print("pos_y: %.04f, vel_y: %.04f, isGrounded: %s" % (self.pos[1], self.velocity[1], self.grounded))
            self.t = 0
        
        self.t += delta
        """

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            # scales translation of mouse to camera rotation
            x,y = event.rel; x/=game.cx; y/=game.cy
            game.rot[0]+=y; game.rot[1]+=x ### ry was (-) ###
	
    def move(self, key): #, delta, key):
        #speed = delta * 5
        speed = 3
    
        

        """
            MOVE PLAYER:
        """

        if self.isKinetic: # if physics enabled on object
            x,y = speed*math.sin(self.rot[1]), speed*math.cos(self.rot[1])
            # by physics
            if key[pygame.K_SPACE] and self.grounded:
                self.velocity[1] = 1
                self.grounded = False
                
            if key[pygame.K_w]: self.velocity[0]=x;  self.velocity[2]=y
            if key[pygame.K_s]: self.velocity[0]=-x; self.velocity[2]=-y
            if key[pygame.K_a]: self.velocity[0]=-y; self.velocity[2]=x
            if key[pygame.K_d]: self.velocity[0]=y;  self.velocity[2]=-x

        else: # if physics disabled on object
            x,y = speed*math.sin(self.rot[1])*delta, speed*math.cos(self.rot[1])*delta
            # by position
            if key[pygame.K_SPACE]: self.pos[1] += delta*speed
            if key[pygame.K_LSHIFT]: self.pos[1] -= delta*speed
           
                
            if key[pygame.K_w]: self.pos[0]+=x; self.pos[2]+=y
            if key[pygame.K_s]: self.pos[0]-=x;  self.pos[2]-=y
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
physix = physics.physics()
player = Player()

focus = True

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
fixedUpdateTime = 0

while(run):
    #delta = clock.tick(60)/1000 # time it took last frame
    delta = clock.tick_busy_loop(60)/1000 #14% cpu usage

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
                
        if focus:
            player.events(event)

    if run:
        if fixedUpdateTime>=.01333333: # 60 tps
            player.update() #delta)

            # player velocity changes as result of move:

            # physics engine processes velocities and collisions...
            
            physix.update(delta, objs.objects)
            game.update(objs.objects)
            
            fixedUpdateTime=0
        
        
        
        if fpsInterval>=1:
            #print("disp")
            fpsInterval=0
            pygame.display.set_caption("Game engine | %.00f fps" % (clock.get_fps()))

        fixedUpdateTime+=delta
        fpsInterval+=delta
