import pygame
import time
from pygame.locals import *

def main():
    scream = pygame.display.set_mode((300,500),0,32)
    background = pygame.image.load("./image/bj.png")
    feiji = pygame.image.load("./image/fj.png")
    x=200
    y=250
    sep=6
    while True:
        scream.blit(background,(0,0))
        scream.blit(feiji,(x,y))
        pygame.display.update()
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x-=sep
                if event.key == K_RIGHT:
                    x+=sep
if __name__=="__main__":
    main()