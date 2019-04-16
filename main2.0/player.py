import pygame

class Player:
    def __init__(self):        
        self.pos = [0,0,0]
        
        self.rot = [0,0]
        self.update_rot()

    def update(self):
        #key = pygame.key.get_pressed()
		if self.isKinetic:
			move(self, pygame.key.get_pressed())
	
    def move(self, key):
        #speed = delta * 5
        speed = 2
    
        if key[pygame.K_SPACE] and self.grounded:
            self.velocity[1] = 3
        
        x,y = speed*math.sin(self.rot[1]), speed*math.cos(self.rot[1])
        
        if key[pygame.K_w]: self.velocity[0]=-x; self.velocity[2]=-y
        if key[pygame.K_s]: self.velocity[0]=x;  self.velocity[2]=y
        if key[pygame.K_a]: self.velocity[0]=-y; self.velocity[2]=x
        if key[pygame.K_d]: self.velocity[0]=y;  self.velocity[2]=-x