import gl
import math
import pygame
import json

pygame.init()
clock = pygame.time.Clock()

game = gl.gl_engine(600, 600)
camera = gl.camera()

file_name = "map.json"
objects = []
with open(file_name) as file:
    objects = json.load(file)
    print(objects)

run = True
while(run):
    delta = clock.tick()/1000
    game.update(clock, delta)
    
