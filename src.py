import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

class Player(pygame.sprite.Sprite) : 
    COLOR=(255,0,0)

    def __init___(self, x, y ,width, height):#Caractéristiques du personnage
        self.rect=pygame.Rect(x,y,width,height)
        self.x_vel=0
        self.y_vel=0
        self.mask=None
        self.direction="left"
        self.animation_count=0


    def move(self,dx,dy): #deplacement du personnage
        self.rect.x+=dx
        self.rect.y+=dy

    def move_left(self,vel):
        self.x_vel=-vel
        if(self.direction!="left"):
            self.direction="left"
            self.animation_count=0


    def move_right(self,vel):
        self.x_vel=vel
        if(self.direction!="right"):
            self.direction="right"
            self.animation_count=0
    
    def loop(self,fps):
        self.move(self.x_vel,self.y_vel)
    
    def draw(self, win):
        






pygame.init()

pygame.display.set_caption("PLATFORMER GAME")

WIDTH,HEIGHT,FPS,PLAYER_VEL=1000,800,60,5

window=pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name) :
    image = pygame.image.load(join("assets","Background",name))
    _,_,width,height=image.get_rect()
    tiles=[] #recouvrement du background

    for i in range(WIDTH // width + 1) :
        for j in range(HEIGHT // height+1):
            pos= (i*width,j*width) #position de chaque carreau
            tiles.append(pos)
    
    return tiles, image

def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()


def main(window) :
    playing = True
    clock = pygame.time.Clock()
    background,bg_image = get_background("Blue.png")

    while playing:
        clock.tick(FPS)
        draw(window, background, bg_image)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                playing=False
                break
        draw(window, background, bg_image)
                
    
    pygame.quit()
    quit()


if __name__=="__main__":
    main(window)


