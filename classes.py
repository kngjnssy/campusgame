import pygame as pg
import settings 
from pygame.sprite import Sprite
import sys, os

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.join(os.getcwd())
    return os.path.join(datadir, filename)

class Fogtile(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pg.image.load(find_data_file('img/15x15blacktile.bmp'))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # self.image.set_alpha(240)

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Player():
    def __init__(self, screen):
        self.screen = screen
        # self.image = pg.image.load(find_data_file('img/comp/17_copy.png'))
        self.image = pg.image.load(find_data_file('img/observer43x43.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # self.compass_imgs = ["img/comp/00.png", "img/comp/01.png", "img/comp/02.png", "img/comp/03.png", "img/comp/04.png", 
        #              "img/comp/05.png", "img/comp/06.png", "img/comp/07.png", "img/comp/08.png", "img/comp/09.png", 
        #              "img/comp/10.png", "img/comp/11.png", "img/comp/12.png", "img/comp/13.png", "img/comp/14.png", 
        #              "img/comp/15.png", "img/comp/16.png", "img/comp/17_copy.png"]
        # self.all_imgs = {}
        # for img in self.compass_imgs:
        #     self.all_imgs[img] = pg.image.load(img)

        # self.compass_img_1 = pg.image.load(self.compass_imgs[1])
        # self.rect = self.compass_img_1.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery - 40

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        speed = 20
        dx = self.rect.centerx
        dy = self.rect.centery

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= speed
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += speed

    def blitme(self):
        # for img in self.compass_imgs:
        #     self.screen.blit(self.all_imgs[img], self.rect)
        self.screen.blit(self.image, self.rect)

class Floorplan():
    def __init__(self, screen):
        # Initialize the object and set its starting position.
        self.screen = screen

        self.image = pg.image.load(find_data_file('img/campus_map_black.bmp'))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)        

class Outline():
    def __init__(self, screen):
        # Initialize the object and set its starting position.
        self.screen = screen

        self.image = pg.image.load(find_data_file('img/outline-thin.png'))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image.set_alpha(100)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)      
      