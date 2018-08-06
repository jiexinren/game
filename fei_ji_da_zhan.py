import pygame
import time
from pygame.locals import *


class FeiJi(object):

    def __init__(self, screen_temp):
        self.x = 200
        self.y = 250
        self.screen = screen_temp
        self.image = pygame.image.load("./image/fj.png")
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_down(self):
        self.y += 5

    def move_up(self):
        self.y -= 5

class DiJi(object):

    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.fangxiang = 'right'
        self.image = pygame.image.load("./image/dj1.png")
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def fire(self):
        self.bullet_list.append(Bullet_2(self.screen,self.x,self.y))

    def move(self):
        if self.x >= 260:
            self.fangxiang = 'left'
        elif self.x <= 0:
            self.fangxiang = 'right'
        if self.fangxiang == 'right':
            self.x += 1
        elif self.fangxiang == 'left':
            self.x -= 1

class Bullet_2(object):
    def __init__(self, screen_temp, x, y):
        self.x = x+20
        self.y = y+40
        self.screen = screen_temp
        self.image = pygame.image.load("./image/zd2.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y+=3


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x+34
        self.y = y-5
        self.screen = screen_temp
        self.image = pygame.image.load("./image/zd.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=5

def key_control(hero):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    hero.move_left()
                if event.key == K_RIGHT:
                    hero.move_right()
                if event.key == K_DOWN:
                    hero.move_down()
                if event.key == K_UP:
                    hero.move_up()
                if event.key == K_SPACE:
                    hero.fire()


def main():
    scream = pygame.display.set_mode((300, 500), 0, 32)
    background = pygame.image.load("./image/bj.png")
    hero = FeiJi(scream)
    diren = DiJi(scream)
    i=0
    while True:
        scream.blit(background, (0, 0))
        hero.display()
        diren.display()
        diren.move()
        if i%50==0:
            diren.fire()
        i+=1
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()