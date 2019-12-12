import pygame as pg

SCREEN_SIZE = (1280, 760)
ORIGINAL_CAPTION = "WLCMTTHCMPS 2"

# pg.mixer.pre_init(44100, -16, 1, 512)

# pg.init()
# os.environ['SDL_VIDEO_CENTERED'] = "TRUE"

pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()