import pygame
from pygame.locals import *
import sys
import random

class FlappyBird():
    def __init__(self):
        self.screen = pygame.display.set_mode((960,960))
        self.walls = []
        
        self.background_pic = pygame.image.load('pic.jpg').convert() #placing background picture
        self.birdSprites = [  pygame.image.load('bird1.jpg').convert_alpha(), pygame.image.load('bird2.png').convert_alpha(), pygame.image.load('bird3.jpg').convert_alpha()  ]
        self.wallDown = pygame.image.load('down.png').convert_alpha()
        self.wallUp = pygame.image.load('up.png').convert_alpha()
        self.gap = -105
        self.wallX = 900
        self.birdY = 400
        self.bird = pygame.Rect(70, 70, 10, 10)
        self.jump = 0   
        self.gravity = 5
        self.jumpSpeed = 10
        self.counter = 0
        self.offset = 5
    def generateWalls(self):
        pass
    def updateWalls(self):
        self.wallX -=4
        if self.wallX <-200:
            self.wallX = 900
            self.counter += 1
            self.offset = random.randint(-150,150)
    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
            self.bird = pygame.Rect(70, self.birdY, 10, 10)
        else:
            self.birdY += self.gravity
            self.gravity += 0.05
        


    def run(self):
        screen_width=960
        screen_height=960
        screen=pygame.display.set_mode([screen_width,screen_height]) #adjusting the width and height
        
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    self.jump = 100
                    self.gravity = 1
                    self.jumpSpeed = 10
            
            
            self.screen.fill((255,255,255))# fill the screen
            self.screen.blit(self.background_pic, (0,0))#blits the image to the screen with these coordinates
            self.screen.blit(self.wallUp, (self.wallX, -80 + self.gap - self.offset))
            self.screen.blit(self.wallDown, (self.wallX, 400 -self.gap - self.offset))
            self.updateWalls()
            self.birdUpdate()
            pygame.draw.rect(self.screen, (250, 0, 0), self.bird)
            self.screen.blit(self.birdSprites[0], (70, self.birdY))


            upRect = pygame.Rect(self.wallX,
                             -80 + self.gap - self.offset,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
            downRect = pygame.Rect(self.wallX,
                               400 -self.gap - self.offset,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
            print(upRect,"----",downRect,"----", self.bird)
            
            if upRect.colliderect(self.bird) or downRect.colliderect(self.bird):
                self.screen.blit(pygame.image.load('fail.jpg').convert_alpha(), (70, self.birdY))
                    

            
            


            
            pygame.display.update()


if __name__ == "__main__":
    
    FlappyBird().run()