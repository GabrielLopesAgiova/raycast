from turtle import width
import pygame as pg
from pygame.locals import *
import numpy as np
from sys import exit


pg.init()
pg.display.set_caption("Raycast")

def mapMultiplier(x,width):
    return 2*(x/width)-1

width, height= (320,200)

screen = pg.display.set_mode((width,height))
screen.fill((190,190,255), rect=(0,0,width,height/2))
screen.fill((102,102,102), rect=(0,height/2,width,height))

running = True

gameMap = np.array([
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1]
    ])

playerPos = np.array([4,4])
playerRot = np.array([0,-1])
playerPlane = np.array([0.66,0])

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
    
    for i in range(width):
        multiplier = mapMultiplier(i,width)
        cameraPixel = np.multiply(playerPlane, multiplier)
        rayDir = np.add(playerPos, cameraPixel)
        print(cameraPixel)
        
    pg.display.update()