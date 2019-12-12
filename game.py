import sys
import os
import pygame as pg
import settings
import classes
import textbubbles as tb
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

def create_tile(screen, tiles, tile_number, row_number):
    # Create a tile and place it in the row.
    tile = classes.Fogtile(screen)
    tile_width = tile.rect.width
    tile.x = tile_width + 1 * tile_width * tile_number
    tile.rect.x = tile.x
    tile.rect.y = tile.rect.height + 1 * tile.rect.height * row_number
    # print(tile.rect.x)
    tiles.add(tile)

def create_all_tiles(screen, tiles):
    tile = classes.Fogtile(screen)
    number_tiles_x = settings.SCREEN_RECT.width / tile.rect.width
    number_rows = settings.SCREEN_RECT.height / tile.rect.width
    # print(number_tiles_x)
    # print(number_rows)
    # print(number_tiles_x * number_rows)
    for row_number in range(int(number_rows)):    
        for tile_number in range(int(number_tiles_x)):
            create_tile(screen, tiles, tile_number, row_number)

def check_tile_player_collisions(screen, player, tiles):
    fog_lifted = pg.sprite.spritecollide(player, tiles, True)
    # if pg.sprite.spritecollide(player, tiles, True):
    #     pass


# text_ada = pg.image.load(find_data_file('img/text_ada.png'))
# text_ada_rect = text_ada.get_rect()

# text_ada_rect.centerx = 193
# text_ada_rect.bottom = 393

def show_textbubbles(screen, player, textbubbles):
    text_ada = tb.TextAda(screen)
    textbubbles = Group()


    if tb.text_ada_rect.colliderect(player):
        screen.blit(tb.text_ada, tb.text_ada_rect)
            

                
def campus_game():
    pg.init()
    screen = pg.display.set_mode((settings.SCREEN_SIZE))    
    pg.display.set_caption(settings.ORIGINAL_CAPTION)
    bg_color = (0, 0, 0)

    plan = classes.Floorplan(screen)
    player = classes.Player(screen)
    tile = classes.Fogtile(screen)
    tiles = Group() 

    # text_ada = tb.TextAda(screen)
    # textbubbles = Group()

    create_all_tiles(screen, tiles)

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                position = pg.mouse.get_pos()
                print(position)

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    player.moving_right = True
                elif event.key == pg.K_LEFT:
                    player.moving_left = True
                elif event.key == pg.K_UP:
                    player.moving_up = True
                elif event.key == pg.K_DOWN:
                    player.moving_down = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    player.moving_right = False
                elif event.key == pg.K_LEFT:
                    player.moving_left = False
                elif event.key == pg.K_UP:
                    player.moving_up = False
                elif event.key == pg.K_DOWN:
                    player.moving_down = False

        screen.fill(bg_color)
        plan.blitme()
        tiles.draw(screen)
        player.blitme()
        check_tile_player_collisions(screen, player, tiles)
        player.update()

        if tb.ada_rect.colliderect(player):
            screen.blit(tb.ada, tb.ada_rect)
        if tb.warp_rect.colliderect(player):
            screen.blit(tb.warp, tb.warp_rect)
        if tb.rock_rect.colliderect(player):
            screen.blit(tb.rock, tb.rock_rect)
        if tb.lizard_rect.colliderect(player):
            screen.blit(tb.lizard, tb.lizard_rect)
            
        pg.display.flip()

campus_game()