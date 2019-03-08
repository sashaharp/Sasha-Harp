import pygame
import numpy as np
pygame.init()

_WIDTH = 800
_HEIGHT = 600

class Color:
    BLACK = (0  , 0  , 0  )
    RED   = (255, 15 , 15 )
    GREEN = (15 , 255, 15 )
    BLUE  = (15 , 15 , 255)
    WHITE = (255, 255, 255)
    
class runState:
    exited = False
    paused = False
    def isRunning(self):
        if self.exited:
            return False
        return True
    def isPaused(self):
        return paused

class monster:
    HP = 10
    SPD = 1
    INIT = 0.5
    ATK = 3
    PHRES = 1
    MRES = 1
    RNG = 1

Recources = {}

def init():
    Recources["testImage"] = pygame.image.load("testImage.png")

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.exited = True

def draw():
    Disp.fill(Color.WHITE)
    Disp.blit(Recources["testImage"], (50, 50))
    pygame.display.update()


Disp = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("The Necromancers Backyard")
clock = pygame.time.Clock()

init()

state = runState()

while state.isRunning():
    if not state.isPaused():
        update()
        draw()
    clock.tick(60)

pygame.quit()
quit()


