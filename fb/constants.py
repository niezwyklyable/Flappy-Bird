
import pygame

WIDTH = 500
HEIGHT = 800
PIPE_WIDTH = 100
GAP = 200
WHITE = (255, 255, 255)

BACKGROUND = pygame.transform.scale(pygame.image.load('imgs/bg.png'), (WIDTH, HEIGHT))
PIPE = pygame.image.load('imgs/pipe.png')
SCALE = PIPE_WIDTH / PIPE.get_width()
PIPE_DOWN = pygame.transform.scale(PIPE, (PIPE_WIDTH, int(SCALE * PIPE.get_height())))
PIPE_UP = pygame.transform.flip(PIPE_DOWN, False, True)
BASE = pygame.transform.rotozoom(pygame.image.load('imgs/base.png'), 0, SCALE)
BIRD_1 = pygame.transform.rotozoom(pygame.image.load('imgs/bird1.png'), 0, SCALE)
BIRD_2 = pygame.transform.rotozoom(pygame.image.load('imgs/bird2.png'), 0, SCALE)
BIRD_3 = pygame.transform.rotozoom(pygame.image.load('imgs/bird3.png'), 0, SCALE)
