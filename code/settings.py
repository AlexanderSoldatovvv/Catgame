import pygame
from path import resource_path

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500
TILE_SIZE = 50
ANIMATION_SPEED = 6

CAMERA_BORDERS = {
    'left': 200,
    'right': 200,
    'top': 100,
    'bottom': 150
}

pygame.font.init()
FONT = pygame.font.Font(resource_path('NotoSans-Bold.ttf'), 16)
FONTGO = pygame.font.Font(resource_path('NotoSans-Bold.ttf'), 40)
FONTS = pygame.font.Font(resource_path('NotoSans-Bold.ttf'), 20)

muted = False
pygame.mixer.init()
pygame.mixer.set_num_channels(3)

cat = pygame.mixer.Channel(2)
meow = pygame.mixer.Sound(resource_path("../audio/meow.mp3"))
meow.set_volume(0.08)

jump = pygame.mixer.Sound(resource_path("../audio/jump.mp3"))
jump.set_volume(0.6)

saved_settings = {"muted": False}

score_settings = {"score":  0}