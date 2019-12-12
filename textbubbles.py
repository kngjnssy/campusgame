import sys
import os
import pygame as pg
import settings
import classes
from pygame.sprite import Group
from pygame.sprite import Sprite

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.join(os.getcwd())
    return os.path.join(datadir, filename)

ada = pg.image.load(find_data_file('img/text_ada.png'))
ada_rect = ada.get_rect()
ada_rect.centerx = 193
ada_rect.bottom = 393

warp = pg.image.load(find_data_file('img/text_warp.png'))
warp_rect = warp.get_rect()
warp_rect.centerx = 272
warp_rect.bottom = 365

# bit = pg.image.load(find_data_file('img/text_8bit.png'))
# bit_rect = bit.get_rect()
# bit_rect.centerx = 68
# bit_rect.top = 508

rock = pg.image.load(find_data_file('img/text_rock.png'))
rock_rect = rock.get_rect()
rock_rect.centerx = 358
rock_rect.top = 508

lizard = pg.image.load(find_data_file('img/text_lizard.png'))
lizard_rect = lizard.get_rect()
lizard_rect.centerx = 675
lizard_rect.top = 508

# zuse	228	382

# echo	316	349
# roomy	849	173
# rick	849	290
# morty	849	334
# kitchen	915	420
# jungle	1031	420
# hally	915	193
# peace	915	153
# AFF	1145	110
# NYMERIA	1145	201
# COGNITO	1145	247
# 6 MIN	1145	293
# OUTER	1209	94
# SPACE	1209	143
# ENTRANCE LEFT	1217	400

# upper left	ada	193	393
# class TextBubbles():
#     def __init__(self, screen):
#         super().__init__()
#         self.screen = screen
#         self.image = pg.image.load(find_data_file('img/text_ada.png'))
#         self.rect = self.image.get_rect()
#         self.rect.centerx = 193
#         self.rect.bottom = 393

#     def blitme(self):
#         self.screen.blit(self.image, self.rect)